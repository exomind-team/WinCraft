---
title: WinCraft release gate and claims boundary
updated_at: 2026-11-02
last_verified_at: 2026-11-02
protocol_baseline: 0.3
status: pre-release-gate
audience: maintainer, release-validator
---

# Release gate and claims boundary

This is a pre-release audit for WinCraft `0.1.0-alpha.1`. It is not release approval. The repository is now public (the user changed visibility on 2026-10-31); no GitHub Release, tag, installer or public announcement was created.

## Claims allowed from current evidence

- Latest source CI: [Actions run 41226574451](https://github.com/exomind-team/WinCraft/actions/runs/41226574451) succeeded for `43b804b`. Recent recorded local checks include 30 UI, 165 Rust workspace (one ignored), and 270 Python tests (one skipped), across separate checkpoints. They were not rerun in this documentation/native-readiness review.
- Current local EXE: `target/release/wincraft-desktop.exe`, 14,402,560 bytes, SHA-256 `A2642924DC770A1B8B6C6E92921D42399A97C5D80379C98F8BEEE9D8F5EA40AB`, built from `43b804b` plus uncommitted Agent Activity changes. It is unsigned and is not an installer or GitHub Release.
- The manager can start/stop/restart its local Agent Activity child without a descriptor path or terminal. Windows manager action routing, an actual managed Python child start/ready/stop/restart cycle, and a real release-headless App/Claude source smoke passed. Computer Use enumerated the newly launched manager but failed twice to activate it (`failed to activate captured window`), so the manager buttons and current rendered cards still need native visual acceptance.
- Synthetic performance evidence includes 5-, 15- and 30-minute visible refresh runs (60/180/360 updates), provider-crash reacquisition, headless Host disconnect and one forced Tauri Host shutdown. In the Tauri crash sample, six WebView descendants exited within three seconds. The 30-minute sample's private-byte median declined while working set increased about 20 MB; this is not a long-term leak guarantee or a cross-machine performance claim. Full context and boundaries are in [`docs/performance.md`](performance.md).
- A pre-refactor Tauri release accepted a three-second synthetic Codex/MiniMax/DeepSeek scene and cleaned its world. After the current B05-02 source refactor, the reproducible synthetic smoke runs the Provider against the release headless Rust Host; no real rollout/auth file, provider key, TeamSense service or external quota endpoint is read. Current quota HUD pixels and live Codex/DeepSeek/MiniMax source freshness remain NOT_RUN.
- `B06-03` stale-grant logic and `B06-04` export hygiene have automated checks. Manager preview/grant/apply/rollback pixels and two-user import remain NOT_RUN/PARTIAL; detailed steps are in the [Chinese acceptance guide](release/WINCRAFT_ALPHA1_ACCEPTANCE_CN.md).
- Repository identity remains `exomind-team/WinCraft`, on branch `dev`. The repository is public as of 2026-10-31 (visibility changed by the repository owner, not by this release gate). No release or tags exist. The current license files, product/package names and ownership were not changed from baseline; `WinCraft` and `窗构` remain explicitly provisional names.
- The Chinese Windows acceptance guide is versioned for `0.1.0-alpha.1` and updated `2026-11-01`; this English gate states the same claim limits and pending native checks. Neither document declares the prototype ready for public release.

## Claims forbidden until manual gates pass

- current-build manager preview/grant/re-preview/apply/cancel/rollback and tray reopen behavior;
- current-build provider-bundle drag/drop, unpack-only install, two-step launch confirmation, and descriptor clipboard copy;
- live Obsidian Workspace plugin snapshot, multi-instance switch, timer action receipt, and native window activation;
- the quota source chooser/key prompt in a real Host window; synthetic state and ACK tests are not pixel acceptance;
- screenshot-level fit, collapse, hidden-window restoration, click-through rescue and z-order;
- multi-monitor/DPI, monitor detach, Windows virtual desktop and native hotkey behavior;
- real Popup user success/cancel/position reuse, WebView2 UIA/IME and screen-reader operation;
- generic Obsidian Workspace activation of an existing window, TrafficMonitor actions and UUID-only Codex App navigation;
- live Codex/DeepSeek/MiniMax quota sources, browser bridge, voice, TouchAI, SysTorch, ExoMind or Android sources;
- long-term leak freedom, sleep/wake, resource thresholds, signed installer, ACL isolation or production security certification.

Computer Use enumerated the current manager but failed twice to activate it with `failed to activate captured window`. Agent Activity's manager buttons and rendered fields therefore remain PARTIAL/NOT_RUN until a user clicks them on this build. The headless smoke does not replace native UI acceptance. See the [daily-use assessment](product/DAILY_USE_READINESS.en-US.md) and [2026-11-01 validation section](engineering/VALIDATION.md).

## Manual gate packet

Run these in one controlled Windows session against the final isolated release, recording only redacted screenshots/exit codes:

1. `W01/W02/W07/W09/W11/W12/W13/W15/W17/W18/W19/W20/W22/W23/W25/W27` from `docs/engineering/ACCEPTANCE.md` against the exact EXE hash above.
2. `R01/R02/R03/R06` after closing any previous WinCraft host.
3. B03-02 Popup success/cancel/position/keyboard/IME/UIA.
4. B04-03 native hotkey only after explicit user authorization.
5. B06-03 synthetic `.wcp` preview, permission grant/re-preview, explicit apply, directed Provider event, cancellation and two-step rollback; then B06-04 import the same config-only pack in two independent user environments and re-authorize each local Provider.

If a gate cannot run because the source, account, device or user authorization is missing, record `BLOCKED` or `NOT_RUN` with the exact reason. Do not convert a browser preview, headless probe or compile result into a native PASS.
