# Ant Design X 组件场景映射

按需选用。抽象模式对齐「SanJin-设计专家」AI 规则；组件名来自 [@ant-design/x](https://x.ant.design/) / [技能列表](https://x.ant.design/x-skills/skills-cn/)。
实现前以官网 API 为准。

## 对话壳与布局

| 场景 | 推荐组件 | 说明 | 规则级别 |
| --- | --- | --- | --- |
| 整体主题 / 配置下发 | `XProvider` | 包裹 AI 区域，统一 locale / 主题 | 推荐规则 |
| 欢迎与能力说明 | `Welcome` | 首次进入：能力边界、示例任务 | 硬规则（对应 ai-trust 初次使用） |
| 会话列表 / 多会话 | `Conversations` | 历史会话切换、新建会话 | 推荐规则 |
| 消息气泡 | `Bubble` | 用户/助手消息、角色区分 | 硬规则 |
| 输入发送 | `Sender` | 输入框、发送、停止生成 | 硬规则 |
| 快捷提示词 | `Prompts` | 示例问题、模板入口 | 推荐规则 |
| 输入联想 | `Suggestion` | 输入中的建议项 | 可选模式 |
| 附件上传 | `Attachments` / `FileCard` | 文件上下文 | 推荐规则（有附件时） |
| 全局通知 | `Notification` | 非阻断反馈 | 可选模式 |

## 生成中与可解释性

| 场景 | 推荐组件 | 说明 | 规则级别 |
| --- | --- | --- | --- |
| 思考过程 | `Think` / `ThoughtChain` | 展示推理步骤，可折叠 | 推荐规则 |
| 引用与来源 | `Sources` | 数据源、文档引用，可展开 | 硬规则（数据型结果） |
| 流式 Markdown | `@ant-design/x-markdown` | 流式渲染、代码高亮 | 推荐规则 |
| 代码块 | `CodeHighlighter` | 代码展示 | 可选模式 |
| 图表/流程图 | `Mermaid` | 结构化图示 | 可选模式 |
| 动作条 | `Actions` | 复制、重新生成、编辑、确认 | 硬规则（可修正） |

## Agent / 富交互

| 场景 | 推荐组件 | 说明 | 规则级别 |
| --- | --- | --- | --- |
| 动态卡片 UI | `XCard`（`@ant-design/x-card`） | Agent 渲染可交互卡片、A2UI | 可选模式 |
| 工具调用结果 | Bubble + Sources + Actions | 结果、依据、操作分离 | 硬规则 |
| 高风险确认 | Actions + 确认文案（可配 antd Modal） | 先影响范围再执行 | 硬规则 |

## SDK（逻辑层）

| 场景 | 推荐能力 | 包 / 技能 |
| --- | --- | --- |
| 对话状态与流式 | `useXChat` | `@ant-design/x-sdk` · 技能 `use-x-chat` |
| 请求封装 | `XRequest` | 技能 `x-request` |
| 自定义流式接口 | Chat Provider | 技能 `x-chat-provider` |

## 典型页面配方

### 1. AI 数据助理（对话 + 结构化结果）

```text
XProvider
├── Conversations（可选侧栏）
├── Welcome（空态）
├── Bubble 列表
│     ├── 文本 / x-markdown
│     ├── Sources（来源与时效）
│     ├── Think / ThoughtChain（可选）
│     └── Actions（编辑 / 重试 / 复制）
└── Sender + Prompts
```

须满足：AI 标识、来源时效、可修正、失败可恢复（见 `references/ai-trust-and-states.md`）。

### 2. 页面内 Copilot 侧栏

```text
抽屉/侧栏容器（选定栈：Semi SideSheet / antd Drawer / Nubes Drawer）
└── X 对话区（Bubble + Sender + Sources）
```

硬规则：不得遮挡主任务关键字段与唯一 primary 操作。

### 3. Agent 执行流

```text
ThoughtChain（计划）→ Bubble（影响预览）→ Actions/确认 → 执行结果 Bubble + Sources
```

## 与 DESIGN.md 对齐（硬）

- 对话面板：`surface` + `1px border`，禁止渐变玻璃拟态。
- 每屏仍只有 **1 个** 主操作实心按钮（发送可为主操作）。
- 状态必须有文字，不只靠颜色。
- 禁止紫粉霓虹「赛博 AI」默认皮肤；可用 Ant Design X 默认主题并收敛到信任蓝 primary。

## 反模式

- 把整站后台全部改成 Ant Design X（X 只管 AI 交互层）。
- 未取证臆造 Bubble/Sender props。
- 有数据结论却无 Sources / 时效。
- 高风险动作无确认直接执行。
