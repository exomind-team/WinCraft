# WinCraft readiness for everyday use

Reviewed: 2026-11-01. Source baseline: `43b804b`. This is an evidence-based assessment and proposed order of work, not a completed-feature announcement. [中文主文](DAILY_USE_READINESS.zh-CN.md).

## Assessment

WinCraft can display real data and acknowledge interactions in native Windows floating windows. Assisted personal trials are practical. Independent everyday use still needs a coherent journey through installation, app selection, launch, reading, temporary hiding, recovery and reconstruction after restart.

The task ledger mixes contracts, unit checks, native acceptance and future integrations. Its PASS count is not a product completion percentage. Android, voice and other platforms need not block a limited Windows daily-use candidate.

## The intended daily journey

Open WinCraft, select an installed app, review its identity and runtime requirements, and explicitly confirm each code launch. The Host passes its current connection descriptor to that selected Provider. Read a compact summary, reveal source lists or details only when needed, and hide or fold the window while working.

After a source stops, show offline history with its age. After Host restart, recreate worlds, sessions and leases from the approved configuration instead of restoring old authority. The user should not have to locate scripts, copy connection paths or identify old processes. This journey is a proposal; several steps remain unimplemented.

## Evidence from this review

- The existing standalone release responded. Computer Use recovered with `@oai/sky`; window enumeration, UIA, screenshots and native button input worked. One input-geometry failure recovered after fresh selection and activation.
- The EXE is 14,345,728 bytes with SHA-256 `D5BF7A251ECE376AD48A099A44492A61F225CBE316FEBE5DFC30D5934301FAC2`. The latest commit changing app/core/server is `bf87fd2`; Python Providers run separately.
- Manager Ctrl+Shift+Plus reported 110% text zoom; Ctrl+0 restored the theme setting. Other keyboard layouts and native IME were not covered.
- A read-only Provider ran for 240 seconds and produced 16 aggregate snapshots. Codex App was process-online; Claude Code was process-offline with readable bounded history. This run excluded CLI and started no target Harness.
- The current project session appeared in the native source page. Source switching received an acknowledgement. Some cards had Agent output; the current project's output was missing, and all per-session states remained unknown. Thread navigation was not clicked.
- Read age and data-health labels were visible. No stale/failure injection was performed, and reading a file now does not establish when its source event happened.
- The Provider exited 0 and confirmed deletion of its own temporary world. The manager returned to zero business worlds. The existing Host and other applications were preserved.
- The generic Obsidian plugin's default snapshot directory did not exist for the current user; this does not establish the state of other paths or private plugins.
- Actions run `41226574451` for `43b804b` succeeded. The repository's Release list was empty. Source CI is not native release acceptance.

Local evidence contains command templates, versions, exit codes and aggregate observations only. No screenshots, session text, title lists, descriptor or credentials were saved.

## Existing applications and remaining work

| Application | Existing basis | Remaining daily-use gap |
|---|---|---|
| TrafficMonitor | Previous real x64 bridge → Rust/Tauri verification | Installable app, bridge/source selection, launch and stale detection; this review observed the source process only |
| Agent Activity | Real local process/disk reading and native single-window navigation | No-terminal startup, history labels, source event time, missing output, filters and honest per-session uncertainty |
| Model quota | Double-click launcher, source chooser, masked keys, bounded Codex events and fixed vendor adapters | Real-source interpretation and native chooser acceptance; keys are memory-only and need re-entry after restart; account-login adapters are absent |
| Obsidian Workspace | Generic metadata plugin, independent focus timer, fixed actions and setup form | Real plugin load/snapshot, multi-instance count, timer acknowledgement and window activation |
| ExoMind workbench | Read-only active-timeblock GET, three local layouts and an earlier real read smoke | Sustained real-source/native layout acceptance; no ExoMind start/pause/end writes are implemented |
| Popup and tutorial | Temporary-question lifecycle and five lesson implementations | Native Chinese input, continuous clicks, success/cancel and position reuse; Popup Provider remains owned by its skill |
| Inbox, decisions and groups | Synthetic logic or real protocol POCs | Real sources and native journeys remain incomplete; no real Harness approval endpoint is connected |

Public examples stay generic. Private dashboards remain with their owning projects. Independently released apps belong in `wincraft-XXX` repositories. Packages never contain user business state or credentials.

## Six gaps

1. **App delivery.** A double-click script still exposes paths and Python dependencies. Provider bundles already separate preview, extraction and final execution confirmation, but the manager retains only the selected/installed bundle in memory. A disk store is not yet a recoverable app library. The launcher discards stdout/stderr, leaving little user-facing diagnosis after an immediate child failure. Agent Activity still has a demo lifetime: 600 seconds by default, at most 3,600 seconds, then it cleans its world. It is not yet a persistent application. Ship one synthetic package and one real app through a dependency preflight, explicit launch, stop and relaunch journey. Do not silently install dependencies or execute unknown code.
2. **Reconstruction and identity.** Multiple Hosts can run independently. Most worlds, leases and settings are memory-only; locale and text zoom already have limited persistence. Save explicit local UI preferences and clean recipes, recreate authority on restart, and retain per-launch code confirmation. This does not require a Host business database or permanent world binding. Persistent secrets need a separate local secret-store design.
3. **Readability and space.** Overlapping translucent windows were difficult to read. `surface_opacity` is applied to the entire frame, including text. Zoom exists; Alt+wheel opacity does not. Separate background opacity from text contrast, expose a discoverable local setting, keep the agreed 0.8 default, and offer clearer reading/input presets. Use compact summaries and progressive disclosure.
4. **Trustworthy information.** Process presence, read success, source event time and per-session activity are different facts. The bounded Claude history count was still labelled “background Agents”; 128 is neither the running count nor the complete archive total. Show read limits explicitly, distinguish source time from collection time, hide unqueried sources from the main overview, and explain missing output without reading full conversations or inventing activity.
5. **Return to the source.** Restricted native app actions and UUID-only thread navigation have implementation support; actual targeting, ambiguous windows and foreground denial need native acceptance. Observation does not confer approval authority. Finish the view → click → correct-source journey before adding business controls.
6. **A real working day.** Existing 5/15/30-minute soaks and crash probes do not establish current-build sleep/wake, multi-monitor, click-through rescue or clean shutdown behavior. All-desktop display is a separate Windows adaptation gap and must not be represented by a no-op switch.

## Proposed next milestone

| Order | Deliverable | Observable gate |
|---|---|---|
| A | Current build, app library and one real app package | User launches through selection/import and confirmation without a terminal or descriptor copying; missing dependencies have actionable explanations |
| B | Honest Agent overview and readable surfaces | Offline history is not active work; read/source times are distinct; current-project output has a valid excerpt or a clear reason for absence |
| C | Single-instance behavior and workspace reconstruction | Repeated launch focuses the same manager; installed apps survive restart; confirmation creates new worlds/leases and restores user preferences |
| D | One or two useful apps, then generic Obsidian | Each app passes installation-to-stop, source disconnect and correct-source navigation independently |
| E | Controlled everyday-use candidate | Several real work periods cover launch, fold/hide/restore, sleep, disconnect, recovery and exit; measure resources and fix observed failures |

These are proposals, not completed work or time estimates. The milestone should be judged by independent use after setup, no command line on ordinary launches, and clear recovery steps. Android, SysTorch, TouchAI, voice, desktop avatars and macOS become blockers only for scenarios that actually depend on them.

## Progress in this iteration (2026-11-01)

Agent Activity now has bilingual manager controls to start, stop and restart its local Provider. Stop first asks the Provider to clean its temporary world. The overview labels bounded record counts as history, counts active work only when status is authoritative, and separates collector read age from SQLite/session-file update time. Codex App output appears only after its rollout `session_meta` UUID matches the thread.

The current EXE is 14,402,560 bytes with SHA-256 `A2642924DC770A1B8B6C6E92921D42399A97C5D80379C98F8BEEE9D8F5EA40AB`. It was launched with `--open-manager` and enumerated by the local window helper; Computer Use failed twice to activate it, so native manager buttons/cards remain unverified. Lifecycle behavior passed Windows child-process and real release-headless Host checks. Provider source still lives in the core checkout; the independent `wincraft-agent-activity` package is future work.

## References and method

Rainmeter connects double-clicking `.rmskin` to an installation dialog through file association. This suggests a package-based user entry without adopting its plugin model. [Official documentation](https://docs.rainmeter.net/manual/installing-skins/).

PowerToys Workspaces provides a saved desktop launch workflow and reports each app's launch outcome. This informs the proposed reconstruction experience; WinCraft still negotiates fresh permissions and confirms code launches. [Microsoft documentation](https://learn.microsoft.com/en-us/windows/powertoys/workspaces).

Tauri explicitly marks `set_visible_on_all_workspaces` unsupported on Windows. A separate native solution needs validation. [Tauri Window documentation](https://docs.rs/tauri/latest/tauri/window/struct.Window.html#method.set_visible_on_all_workspaces).

The review follows user intent → implementation → observed behavior → counterexample → acceptance → smallest revision. Planning assets, synthetic tests, real protocol, native UI and sustained use remain distinct. See [validation](../engineering/VALIDATION.md) and the [current Chinese acceptance guide](../release/WINCRAFT_ALPHA1_ACCEPTANCE_CN.md).
