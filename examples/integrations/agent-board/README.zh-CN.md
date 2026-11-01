# Agent Activity · 本机会话总览

Agent Activity 只读呈现 Codex CLI、Codex App 与 Claude Code。Codex App 和 Claude Code 的在线状态根据进程元数据判断，会话详情来自受限的本机文件；没有权威逐会话状态时显示“未知”。本功能不启动 Codex App 或 Claude Code，不读取完整对话、thinking、用户提示或工具输出，不批准任务，也不继续执行。

## 从世界管理器启动

1. 打开 WinCraft 桌面 Host，再从托盘打开“世界管理器”。
2. 在管理器的“Agent 总览”区域点击“启动总览”。Host 自动把当前连接交给内置 Provider；无需复制描述符、粘贴路径或打开终端。
3. 状态显示“运行中”后，Agent Activity 窗口会定期更新 Codex CLI、Codex App 与 Claude Code 的本机摘要。
4. 在同一区域可点击“停止总览”或“重启总览”。停止会请求 Provider 清理自己的临时世界；8 秒仍无正常退出时，Host 才会强制结束该子进程并显示失败状态。

Agent Activity 在 Host 关闭时停止。再次打开 Host 后，在管理器点一次“启动总览”；它会建立新的会话和窗口。每个来源都分别显示进程状态、最近一次成功读取时间、数据读取质量、会话状态和来源记录更新时间。这些时间分别说明“程序是否运行”“何时读取”和“本地来源记录何时更新”。历史读取有上限；显示数量不是活跃 Agent 数。来源没有权威逐会话状态时，界面保留“状态未知”。

## 来源与数据边界

- **Codex CLI**：独立的本机 `app-server` 状态库来源，固定 `useStateDbOnly=true`；按最近记录读取，并在受限数量内提取 Agent 输出。
- **Codex App**：从只读 `state_*.sqlite` 中筛选 `originator=Codex Desktop`，以线程 UUID 匹配 `session_meta` 后读取有限 rollout 尾部。标题点击只触发 Host 限制的 UUID-only Codex 深链。
- **Claude Code**：只读取已知项目 JSONL 及其 `subagents/agent-*.jsonl` 子 Agent 路径，并核验父会话和 Agent 身份。

会话标题、项目和输出都是不可信的本机文本，先做长度限制和脱敏，再只留在 Provider/Host 内存。本机过程摘要只记录健康和状态计数，不记录会话身份、路径或正文。

当前 Windows 原型从 WinCraft checkout 启动随仓库提供的 Provider 源码；独立的 `wincraft-agent-activity` 应用包尚未交付。Python 或所需模块不可用时，管理器会显示不可用状态，不会静默安装依赖。

## 行为场景

**Given** 桌面 Host 正常运行且 Agent Activity 依赖可用，**When** 用户从世界管理器点击“启动总览”，**Then** Host 用本次真实 descriptor 启动一个无终端子进程；Provider 完成本机读取、连接握手并提交第一份窗口快照后，状态才变为“运行中”。

**Given** 总览正在运行，**When** 用户点击“停止总览”，**Then** Host 通过本机输入通道发送停止请求；Provider 清理自己的 world 并退出后，状态变为“已停止”。**When** 清理超过 8 秒，**Then** Host 强制结束该子进程、明确显示失败，并允许用户重新启动。

英文说明见 [README](README.md)。
