# WinCraft 原型工程交接

版本：0.1.0-alpha.1。目标平台：Windows 优先。正式名称尚未冻结。

## 交接目标

从**已经写好的源码**得到能够在用户 Windows 机器上真实运行并复验的开发版与 release 原型。第一目标不是扩组件市场或桌宠，而是让不懂前端的外部程序通过协议使用原生窗口，且所有权、断线、动作与救援都可靠。

最短入口是根目录 `CODEX_PROMPT.md`。产品约束见 `docs/product/DECISIONS.md`，协议细节见 `docs/protocol.md`，事实基线见 `docs/engineering/VALIDATION.md`。

## 初始交接状态，不能误读

| 对象 | 交接时状态 |
|---|---|
| TypeScript 共享 renderer | 严格构建和 Node 测试通过 |
| 浏览器交互 | Chromium 中使用实际编译模块 + 模拟提供者通过部分 DOM 测试 |
| Rust 内核、Axum 服务、Tauri 适配 | 有实现与测试源码；没有 Rust 编译或原生执行证据 |
| Python 提供者 | 语法检查通过；真实连接待运行 |
| 外心桥接 | 已核对源码接口；默认只读；真实 RT 未连接 |
| 依赖锁定 | 尚无 Cargo.lock/package-lock.json，必须实际解析生成 |
| 可执行文件 | 本包不含已构建 Windows EXE，不声称可直接安装 |

22 个 Rust 测试定义不等于 22 个通过；JSON schema 检查不等于服务实际按 schema 行为；截图不等于 Tauri 窗口通过。

## 当前验证与仓库状态（2026-11-02）

- 源码基线 `43b804b`，remote 为 `exomind-team/WinCraft`，分支 `dev`。所有者于 2026-10-31 改为公开；2026-11-02 检查仍无 GitHub Release 或 tags。当前阶段性提交只包含已扫描的 WinCraft 实现和文档；临时 handoff review 目录留在本地。
- 最新 [Windows Actions run 41226574451](https://github.com/exomind-team/WinCraft/actions/runs/41226574451) 对 `43b804b` success。当前相关门禁：Agent Activity/总览/收件箱 Python 56 项通过、Rust server 65 项通过（1 ignored）、Windows 受管子进程 start/stop/restart 测试 1 项通过；Tauri cargo check、严格 Clippy、UI 构建及合同检查通过。本轮工作未推送 CI。
- 当前本机 release 为 `target/release/wincraft-desktop.exe`，14,402,560 bytes，SHA-256 `A2642924DC770A1B8B6C6E92921D42399A97C5D80379C98F8BEEE9D8F5EA40AB`，从 `43b804b` 加当前未提交工作区构建；未签名、非安装器、非 GitHub Release。
- Computer Use 在本轮已恢复：`@oai/sky` 窗口枚举、管理器展开、截图/UIA、字号 110%/恢复、App 来源切换均有原生观察。一次 input geometry 失败通过重新选择/激活恢复。不能再把过去 native pipe 失败当作当前统一阻碍。
- 真实 App/Claude 只读 Provider 在当前 release 运行 240 秒，16 次聚合快照，App online、Claude offline，逐会话 unknown；当前项目会话名称/项目出现在原生页，部分其他卡片有 Agent 输出。本项目输出仍缺失，UUID-only 导航未点，stale/failure 未注入；B08-02-A4/A5 均 PARTIAL。退出码 0，临时世界确认清理。
- Agent Activity 已接入管理器一键 start/stop/restart，使用当前 Host descriptor，常驻到用户停止，且先清理临时 world 再退出；Python/依赖或 Provider 源码不可用时管理器显示 unavailable。总览把有界条数标为历史记录，活跃数只统计权威已知状态，并分开展示最近读取时间、来源文件更新时间和逐会话记录更新时间。
- B10-03 窗口组为 preview 逐成员独立结果，非原子且不授予新权限；真实 headless 17 项检查和 Tauri 协议 demo 已通过，组原生救援/关闭/减少动画仍 PARTIAL，捕获排除未实现。B09-03 统一收件箱为合成投影；B08-04 决策卡为状态机，尚无真实 Harness 批准适配器。三项均 `IMPLEMENTED_UNVERIFIED`。
- 模型额度不依赖 TeamSense 服务：本机 Codex rollout 只读事件；DeepSeek/MiniMax 固定只读 GET 和 Codex live 实验源均独立 opt-in。双击来源配置、增删和内存 Key UI 已有实现，真实账号与原生完整流程仍待验收。Obsidian 公共示例仅为通用 Workspace 插件；本轮当前用户默认快照目录不存在，没有部署或修改真实 Vault。
- Agent Activity manager lifecycle 的 Windows 子进程测试和真实 release headless Provider/Rust WebSocket 停止清理通过。新桌面 manager 窗口已启动并被窗口枚举发现，但本轮 Computer Use 两次激活失败；管理器 start/stop/restart 原生点击仍 PARTIAL，B08-02-A6 为 PARTIAL。来源数据卡片、托盘、穿透、多屏/DPI、IME/UIA、线程导航、配置包和 Provider bundle 原生门仍 NOT_RUN。
- SysTorch、TouchAI、浏览器桥接和 Android 的真实来源/权限缺口继续局部记录；Windows 全虚拟桌面 pinning 尚未实现。Linux WSL2 Tauri ELF/tests/Clippy 有历史证据，Linux GUI/X11/Wayland 和 macOS 原生行为仍 NOT_RUN。远期集成不自动阻挡有限 Windows 日用版本。
- 历史与逐层事实以 [VALIDATION](docs/engineering/VALIDATION.md)、[当前中文验收指南](docs/release/WINCRAFT_ALPHA1_ACCEPTANCE_CN.md) 和策略任务账本为准。旧摘要中的 build/hash/CU 失败只属于其时间点；`evidence/local/` 保持忽略，不提交 descriptor、用户文本或原始截图。历史定向脱敏保留了全部 114 个原始提交的作者与时间，后续继续逐项审查新增公开内容。

## 必须保留的设计不变量

1. 稳定协议 0.3 同一世界最多一个活跃写租约；显式 0.4 preview 的不相交 scope 各自独占，并由独立 authority 管理。所有远程写入验证会话、lease ID、epoch、单调时钟到期和预期版本。
2. 读取是权限受限的不可变快照，不是 Rust `&T` 与 `&mut T` 的跨进程复制。发现只返回摘要，场景读取仍需加入。
3. 批量组件 patch 全部成功或全部失败；不支持的组件/属性明确报错。
4. 业务真相不落入宿主数据库；运行中暂存、输入草稿、缓存和会话状态不冒充业务记录。
5. 正常动作回到当前写者；发送成功不是业务成功。动作有 pending/ok/error/timeout；拒绝来自旧 revision 的点击。
6. 窗口配置接受与原生属性应用分开；原生失败显示为错误，不谎报已应用。
7. 人类几何模式不被普通 provider 坐标更新覆盖；本地管理器接管设置 hold，需要显式解除，不能下一次 join 就夺回。
8. 一个窗口一个共享 renderer 实例，不按提供者另建 WebView；管理与设置也是组件声明。
9. 没有固定端口、没有匿名档案 fallback、没有跨重启永久绑定。
10. 保留 ExoMind 来源许可、固定 SHA 和修改说明。

## 实施顺序与命令

### A. 静态基线和依赖

使用 Node 22、Python 3.11+、当前可用的 Rust stable。先确认工作目录，不覆盖其他同名项目。保存初始文件清单与 SHA256；`MANIFEST.sha256` 是交接快照，不要求修改后仍匹配。

```powershell
npm ci
python -m pip install -r requirements-dev.txt -r examples/python/requirements.txt
npm run check:local
```

`check:local` 覆盖 UI 行为与离线契约、Rust workspace（包括 Tauri crate）的 fmt/check/test/clippy，以及 Python provider 单测和 Skill 校验。锁文件必须来自真实依赖解析；常规 checkout 使用 `npm ci`，调整依赖时才运行 `npm install` 并审阅 lockfile 差异。分层命令和 CI 边界见 [`docs/engineering/DEVELOPMENT_TOOLCHAIN.md`](docs/engineering/DEVELOPMENT_TOOLCHAIN.md)。

### B. 无界面真实协议

终端 A：

```powershell
cargo run -p wincraft-server --bin wincraft-headless
```

终端 B（复制实际输出的描述文件路径）：

```powershell
python examples/python/lease_probe.py --runtime "<实际描述文件>"
python examples/python/focus_demo.py --runtime "<实际描述文件>"
```

headless 不画窗口；它只证明真实 Rust 状态机和 WebSocket 行为。给 `lease_probe.py` 扩充断网/超时场景时，使用不同连接，不模拟成同一 session。不要让客户端提供 host 时钟。

### C. Windows 桌面

按 Tauri 官方 prerequisites 安装 Windows C++ 工具链与 WebView2；不要安装 Electron。

```powershell
npm run desktop:dev
```

预期：主进程常驻托盘，无默认主窗口；托盘打开“世界管理器”。为本机自动化联调，构建后的 EXE 也接受显式 `--open-manager` 参数，启动时打开管理器；不带参数仍保持 tray-only。管理器显示实际描述文件路径。启动 Python 示例，检查是否出现真正可置顶、可移动的窗口，而非浏览器卡片。

检查 Tauri `beforeDevCommand` / `beforeBuildCommand` 工作目录、应用自定义命令 ACL、动态 `world-*` labels 的 capability、`WebviewWindow` 调用者注入、`Image::from_bytes`、tray 回调和原生窗口 setter 的精确版本签名。这里是优先定位区，不是预先断言必然有错误。

### D. 独立 release

```powershell
npm run desktop:build
```

实际产物通常位于 Cargo target 的 release 子目录，但必须先确认真实路径再报告。关闭仅用于本项目的 dev 实例后，直接启动生成 EXE；不要通过 Vite 代理声称 release 成功。也要测试两个宿主实例同时运行：不同 host_id、端口、描述文件，不互删对方令牌文件。

### E. 外心只读集成

```powershell
python examples/python/exomind_readonly.py --runtime "<WinCraft 实际描述文件>" --exomind "http://127.0.0.1:<实际 RT 端口>" --profile "<明确档案 ID>"
```

详细边界见 `docs/integration-exomind.md`。已有源码支持 `GET /timeblocks/active?user_id=...`，但真实返回结构/鉴权/运行端口都需要当前现场核验。不得把 404 直接当成“用户没有时间块”；它也可能是端点不匹配。

### F. 本机试用与 `.wcp` 提供者包

- 世界管理器中可以复制 runtime descriptor 路径；双击 `examples/launchers/start-model-quota.cmd` 会让用户粘贴路径并点选已实现的额度来源。
- Obsidian 通用插件、Provider 和双语说明见 `examples/obsidian-plugin/`、`examples/python/obsidian_workspace.py`、[中文指南](docs/integration-obsidian.zh-CN.md)与[English guide](docs/integration-obsidian.en-US.md)。它只呈现本机文件/工作区元数据和本地专注计时；不读笔记正文。
- 配置型 `wincraft.pack.draft` 与 `wincraft.provider-bundle` 是不同 `.wcp` manifest kind。代码包拖入只预览，安装只解包，最终运行单独确认；不自动安装依赖，不使用 shell。运行包会得到 runtime descriptor，因此必须确认来源与代码。
- 当前合成代码包由 `python scripts/build_provider_bundle.py` 生成；插件 ZIP 由 `python scripts/package_obsidian_plugin.py` 生成。两者输出在 ignored `target/`，不可把 `evidence/local` 或真实 descriptor 放入提交。

## 代码地图与优先审查点

| 入口 | 最该看什么 |
|---|---|
| core/model.rs、engine.rs | 写租约、防旧写 fencing、revision/sequence 区分、operator hold |
| core/scene.rs | 克隆候选再提交、ID 唯一、移入自身拒绝、资源上限 |
| server/hub.rs | 所有外部 method 与内部 provider 共用 dispatch；锁不得跨 await |
| server/transport.rs | Upgrade 前鉴权、Origin 拒绝、握手/限流/断线处理、描述文件权限 |
| server/self_provider.rs | 内部管理器不能暗建第二套 UI；受信本地管理权限与普通 lease 区分 |
| desktop/src-tauri/src/windows.rs | UI 线程与回调、DPI 坐标、关闭拦截、应用回执、拖动回声抑制 |
| desktop/src/main.ts、renderer.ts | 先订阅后快照、sequence fencing、键控节点、IME、原生/预览分离 |
| Python client.py | 并发请求回包匹配、心跳、超时不盲重试、lease epoch、host_id 校验 |

已知工程债：50ms 全快照扫描与完整快照通知不是最终性能架构；内核锁中克隆场景；组件级租约仅在显式 preview，尚无稳定协议承诺；没有 origin 白名单/TLS 和生产级跨用户鉴权；Windows descriptor ACL、多屏/DPI、click-through 救援、IME 原生路径和休眠恢复仍需专门验收。它们不应被隐瞒，也不要求本地 Codex 一口气实现所有后续愿景。

## 验收、回滚与交付

执行 `docs/engineering/ACCEPTANCE.md` 的分层用例。某层失败时保留可独立完成的其他层结果，不能把“不具备 Windows 环境”写成全部成功。修改后重新运行与变更相关的回归。

不要改用户外心的安装/数据库；试验世界可由托盘关闭或退出本宿主清理。需要重置时关闭本项目的宿主，只清理本项目生成的运行描述文件。不要全盘删除 AppData、不要结束全部 WebView2 进程。

本地最终报告必须包含：环境及依赖版本、真实命令/退出码、修复摘要、三层测试矩阵、脱敏截图、实际构建路径、已知问题。记录保存在 `evidence/local/`；源证据不可覆盖。未明确授权时，不远程发布或推送。
