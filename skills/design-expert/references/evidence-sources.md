# 规范来源与证据治理

本知识库按**当前选定实现栈**取证：组件 API 只允许来自该栈的 MCP / 物料。其它库仅作模式与原则参考，不得混用 API。默认实现栈为 **Semi Design**（用户未选择时）。

路径均相对于本技能根目录 `设计专家/`。

## 优先级

| 优先级 | 来源 | 可决定的内容 |
| --- | --- | --- |
| P0 | 项目品牌规范、业务安全规则、**当前选定实现栈**的已验证物料 / MCP | 最终视觉、真实组件 API、权限与合规限制 |
| P0.5 | 本技能 `references/DESIGN.md` + `visual-quality.md` | B 端数据台默认视觉气质、首屏预算、反模式（无项目品牌时生效） |
| P1 | 无障碍与可信 AI 硬规则 | 对比度、键盘焦点、AI 透明度、人工确认与可恢复性 |
| P2 | 非选定栈的 Ant / Semi / TDesign MCP 官方组件规范 | 企业级交互模式、Token 思路、组件使用场景（仅参考） |
| P3 | 本技能 B 端、AI、图表与 DESIGN.md 参考 | 专项规则和格式；不得覆盖项目契约 |

冲突时按优先级处理；同级冲突时，以目标用户任务、可访问性、数据正确性和**选定栈**能力为裁决依据。

## MCP 证据索引

| 来源 | 已验证内容 | 使用方式 | 限制 |
| --- | --- | --- | --- |
| Semi MCP | 组件 API、无障碍、中文文案、Table/Form 等场景 | 默认栈：先查文档和示例，复杂场景再查组件文件或函数实现 | 未取证不得臆造 API |
| Ant Design MCP | 企业级 Token、Table/Form 组件与交互能力 | 用户选定 Ant 时作实现证据；否则仅作模式参考 | 不得把 Ant API 写进 Semi/TDesign 代码 |
| Ant Design X + `companions/ant-design-x/` | AI 对话组件（Bubble/Sender/Conversations/Prompts/Sources/ThoughtChain 等）、useXChat、XRequest、x-markdown | **AI 产品按需**取证；可选安装官方 `@ant-design/x-skill` | 仅用于 AI 交互层；视觉仍服从 DESIGN.md；未取证不得臆造 API |
| TDesign MCP | Vue Next 的 Table、Form、Dialog、Drawer、Pagination、Select、DateRangePicker 等 | 用户选定 TDesign 时作实现证据；否则作 Vue 场景参考 | 不得跨库复制 API |

## 技能包内知识库

| 路径 | 复用范围 | 使用限制 |
| --- | --- | --- |
| `knowledge/design-md/google-spec/docs/spec.md` | Google DESIGN.md 格式规范 | 仅在编写/校验设计文档时读取 |
| `references/context-routing.md` | 本地 UI 技能与参考的最小加载规则 | 每个 UI 任务先路由；同一阶段最多 3 个技能 |
| `references/design-evidence-gate.md` | 现有界面改进与评审的证据要求 | 发现须同时具备契约、运行路径和唯一修正 |
| `references/design-md-workflow.md` | DESIGN.md 的证据账本、纳入门禁与更新规则 | 仅沉淀可追溯的治理性决策 |
| `companions/mcp-setup/` | Semi / Ant Design / TDesign 的 Cursor MCP 安装与排障 | 缺 MCP 或用户要求安装时必读；合并写入 `.cursor/mcp.json` |
| `references/evidence-record.template.json` | 原型组件取证记录格式 | 每个可运行原型工程复制为 `evidence.json`，记录栈、组件、来源、风险与验证命令 |
| `scripts/validate_prototype.py` | 静态单栈、证据、状态与视觉风险检查 | 原型交付前执行；脚本告警须人工复核，错误必须修复 |
| `companions/ant-design-x/` | Ant Design X AI 对话/Agent 组件与场景映射 | 设计 AI 产品时按需必读；可选配合官方 x-skill |
| `companions/vchart/` | VChart 图表选型、接入、证据与验收 | 有图表时必读 |
| `examples/数据中台-任务监控.html` | B 端页面结构示例 | 只参考结构，按业务改写 |

## 外部官方来源

以下来源用于规则追溯。引用时优先提炼原则，不复制品牌皮肤或特定组件代码。

| 来源 | 适用规范 | 技能包内路径 / 链接 |
| --- | --- | --- |
| Google DESIGN.md 规范 | YAML token + 固定章节顺序 | `knowledge/design-md/google-spec/docs/spec.md` · https://github.com/google-labs-code/design.md |
| Google DESIGN.md Spec | Overview → Colors → … → Do's and Don'ts | `knowledge/design-md/google-spec/docs/spec.md` |
| UI Skills（MIT） | 最小 Skill 路由、设计发现证据门禁、DESIGN.md 证据管线 | 已本地化为 `context-routing.md`、`design-evidence-gate.md`、`design-md-workflow.md` · https://github.com/ibelick/ui-skills |
| Microsoft Power BI Dashboard Tips | 受众导向、单屏叙事、KPI 层级 | https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips |
| Microsoft Human-Centered Design for Agents | AI 能力边界、修正与恢复 | https://learn.microsoft.com/en-us/agents/design-guidelines/human-centered-design |
| Ant Design X Skills | AI 对话组件与 Agent 技能包 | `companions/ant-design-x/` · https://x.ant.design/x-skills/introduce-cn/ |
| SAP Fiori Generative AI Principles | 人类主导、可验证与可调节 | https://www.sap.com/design-system/fiori-design-web/v1-120/foundations/ai-and-joule-design/guidelines/design-principles-for-generative-ai |
| WCAG 2.2 | 对比度、键盘、焦点等 | https://www.w3.org/TR/WCAG22/ |

### DESIGN.md 落点

| 路径 | 用途 |
| --- | --- |
| `references/DESIGN.md` | B 端数据台权威视觉规范（本技能默认） |
| `references/visual-quality.md` | 视觉硬规则与验收 |
| `knowledge/design-md/google-spec/docs/spec.md` | Google DESIGN.md 格式规范 |
| 项目根 `DESIGN.md`（可选） | 分享后可从 `references/DESIGN.md` 复制到根目录便于发现 |

使用说明见技能根 `README.md`。

## 证据记录模板

| 字段 | 内容 |
| --- | --- |
| Rule ID | 例如 `DATA-TABLE-001` |
| 规则 | 可执行、可验收的短句 |
| 级别 | 硬规则 / 推荐规则 / 可选模式 |
| 适用范围 | 产品类型、页面、组件、端 |
| 来源 | P0–P4、URL/MCP 文档/本地路径 |
| 版本/日期 | 组件库版本、文档日期或检索日期 |
| 冲突处理 | 与项目 Token 或选定栈能力冲突时的决定 |
| 示例 | 最小正确案例或反例 |

## 使用注意

- 对于组件 **API、props、events 或代码示例**，必须以**当前选定实现栈**的 MCP / 物料为准（未选择时默认 Semi Design）。
- 对于未验证的市场文章、搜索摘要或历史案例，只能写成“参考实践”，不能写为硬规则。
- 触及数据安全、权限、导出、自动执行时，优先采用项目内部要求；没有要求时，将风险显式列为待确认项。
