"""Exercise the managed Agent Activity provider against a real release Rust Host.

The isolated descriptor and Host output live in a temporary directory. Provider
stdout is reduced in memory to aggregate source/status counts; no session text is
printed or written to evidence.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HOST_EXE = ROOT / "target" / "release" / "wincraft-headless.exe"
PROVIDER = ROOT / "examples" / "integrations" / "agent-board" / "live_provider.py"
START_TIMEOUT = 30
RUN_SECONDS = 17
STOP_TIMEOUT = 15


def _environment(runtime_dir: Path) -> dict[str, str]:
    allowed = (
        "PATH", "SYSTEMROOT", "WINDIR", "USERPROFILE", "APPDATA", "LOCALAPPDATA",
        "TEMP", "TMP", "CODEX_HOME", "CLAUDE_CONFIG_DIR",
    )
    result = {key: value for key, value in os.environ.items() if key in allowed}
    result["WINCRAFT_RUNTIME_DIR"] = str(runtime_dir)
    return result


def _wait_for_descriptor(runtime_dir: Path, host: subprocess.Popen[Any]) -> Path:
    deadline = time.monotonic() + START_TIMEOUT
    while time.monotonic() < deadline:
        if host.poll() is not None:
            raise RuntimeError("HOST_EXITED_BEFORE_READY")
        matches = list(runtime_dir.glob("*.runtime.json"))
        if len(matches) == 1:
            return matches[0]
        time.sleep(0.1)
    raise RuntimeError("HOST_READY_TIMEOUT")


def run() -> dict[str, Any]:
    if not HOST_EXE.is_file():
        raise RuntimeError("RELEASE_HEADLESS_HOST_MISSING")
    if not PROVIDER.is_file():
        raise RuntimeError("AGENT_ACTIVITY_PROVIDER_MISSING")
    with tempfile.TemporaryDirectory(prefix="wincraft-agent-activity-smoke-") as temporary:
        runtime_dir = Path(temporary) / "runtime"
        runtime_dir.mkdir()
        environment = _environment(runtime_dir)
        host = subprocess.Popen(
            [str(HOST_EXE)], cwd=ROOT, env=environment,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        provider: subprocess.Popen[str] | None = None
        snapshots: list[dict[str, Any]] = []
        ready = threading.Event()
        stopped = threading.Event()

        def read_provider_events(stream: Any) -> None:
            for line in stream:
                try:
                    value = json.loads(line)
                except (json.JSONDecodeError, TypeError):
                    continue
                if not isinstance(value, dict):
                    continue
                if value.get("event") == "agent-activity-ready":
                    ready.set()
                elif value.get("event") == "agent-activity-stopped":
                    stopped.set()
                elif value.get("event") == "live-source-snapshot":
                    snapshots.append({
                        "source_health": value.get("source_health", {}),
                        "status_counts": value.get("status_counts", {}),
                    })

        try:
            descriptor = _wait_for_descriptor(runtime_dir, host)
            provider = subprocess.Popen(
                [
                    sys.executable, str(PROVIDER), "--runtime", str(descriptor),
                    "--until-stopped", "--refresh-seconds", "15",
                    "--sources", "codex-app", "claude-code",
                    "--title", "Agent Activity lifecycle smoke",
                ],
                cwd=ROOT, env=environment, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                text=True, encoding="utf-8", errors="replace", bufsize=1,
            )
            assert provider.stdout is not None
            reader = threading.Thread(target=read_provider_events, args=(provider.stdout,), daemon=True)
            reader.start()
            if not ready.wait(START_TIMEOUT):
                raise RuntimeError("PROVIDER_DID_NOT_REACH_READY_WORLD")
            time.sleep(RUN_SECONDS)
            assert provider.stdin is not None
            provider.stdin.write("stop\n")
            provider.stdin.flush()
            exit_code = provider.wait(timeout=STOP_TIMEOUT)
            if exit_code != 0:
                raise RuntimeError("PROVIDER_STOP_EXITED_WITH_ERROR")
            if not stopped.wait(2):
                raise RuntimeError("PROVIDER_CLEANUP_ACK_MISSING")
            if len(snapshots) < 2:
                raise RuntimeError("INSUFFICIENT_REFRESH_SNAPSHOTS")
            return {
                "host": "release_headless_rust",
                "provider_exit_code": exit_code,
                "ready_world_confirmed": True,
                "clean_stop_acknowledged": True,
                "snapshot_count": len(snapshots),
                "last_aggregate_snapshot": snapshots[-1],
                "target_harness_started": False,
                "business_writes": False,
                "raw_session_text_retained": False,
            }
        finally:
            if provider is not None and provider.poll() is None:
                provider.kill()
                provider.wait(timeout=5)
            if host.poll() is None:
                host.terminate()
                try:
                    host.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    host.kill()
                    host.wait(timeout=5)


if __name__ == "__main__":
    try:
        print(json.dumps(run(), ensure_ascii=False, separators=(",", ":")))
    except Exception as error:
        print(json.dumps({"status": "FAIL", "reason": type(error).__name__}, separators=(",", ":")))
        raise SystemExit(1)
