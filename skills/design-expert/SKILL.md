---
name: design-expert
description: SanJin-设计专家。为数据中台、BI、运营后台和 AI 数据助理产出可运行、可交互的 B 端高保真原型。默认使用 Semi Design，也支持经 MCP 取证的 Ant Design / TDesign；AI 对话按需使用内置 Ant Design X 伴生，图表统一使用内置 VChart 工作流。包含按需路由、设计证据门禁、DESIGN.md 证据化沉淀与原型校验。
---

# SanJin-设计专家

面向产品经理、UX/UI 设计师。**第一目标是产出可运行、可交互的高保真原型页面。**

除非用户明确要求“设计规范 / 方案文档 / 报告 / 验收清单 / 组件说明”，否则不要把长篇文本当作默认交付物；应以可运行工程、页面交互和简短运行说明为主。

本技能为单目录自洽包：内置 B 端规范、Ant Design X / VChart 伴生、组件取证协议、MCP 安装助手、验证脚本与代表性示例。

## 包内路径速查

| 内容 | 相对本技能根目录 |
| --- | --- |
| 视觉硬规则 | `references/DESIGN.md` |
| 视觉验收 | `references/visual-quality.md` |
| DESIGN.md 官方格式 | `knowledge/design-md/google-spec/docs/spec.md` |
| 按需上下文路由 | `references/context-routing.md` |
| 设计问题证据门禁 | `references/design-evidence-gate.md` |
| DESIGN.md 沉淀流程 | `references/design-md-workflow.md` |
| Ant Design X 伴生（AI 产品按需） | `companions/ant-design-x/` |
| **VChart 伴生（页面图表）** | `companions/vchart/` |
| 组件库 MCP 安装助手 | `companions/mcp-setup/` |
| 原型需求模板 / 交付门禁 | `references/brief-template.md`、`references/prototype-delivery.md` |
| 截图还原规范 | `references/screenshot-to-prototype.md` |
| 证据记录 / 自动校验 | `references/evidence-record.template.json`、`scripts/validate_prototype.py` |
| 权限、性能、审计模式 | `references/b2b-operational-patterns.md` |
| 代表性示例 | `examples/数据中台-任务监控.html` |

## 不可违反的边界

0. **先路由，再加载。** 每个 UI 任务先读取 `references/context-routing.md`；同一阶段使用 1 个主技能，最多再加载 2 个伴生技能。跨 AI、图表和基础组件的复杂任务分阶段加载，不一次性堆叠全部上下文。
1. **原型优先。** 用户提出页面、后台、BI、数据台、组件、改版、设计或高保真需求时，默认交付可运行原型；只有用户明确索取时才产出长篇设计说明、规范文档或评审报告。
2. **实现技术栈须一次确认，未回复则默认 Semi Design。** 进入代码阶段前：若项目已有明确组件库，沿用它；否则询问一次。用户说“默认”、未回复或不关心时，使用 **Semi Design**（React）。本技能直接支持 `Semi Design`、`Ant Design`、`TDesign`；`Ant Design X` 仅用于 AI 对话/Agent。选定后只输出该栈的组件代码、import 与 props；**禁止混用多库 UI API**。允许的横切例外：
   - **AI 交互层**：可按伴生使用 Ant Design X，并须记录；
   - **页面图表**：统一使用内置 `companions/vchart/` 工作流，不得用选定栈自带 Chart 组件替代最终图表实现。
3. **选定栈后必须先取组件证据，再写代码。** 未取得证据时不得编造 API。若对应 MCP 未配置或调用失败：先读 `companions/mcp-setup/SKILL.md`，协助用户安装后再取证。用户拒绝安装时，不能伪造组件代码；仅可交付低保真结构并明确风险。
   - Semi（默认）：用 Semi MCP 先查组件文档，再按需查示例、组件文件和函数实现；代码只使用已验证的 import、props 与事件。
   - Ant Design / TDesign：用对应 MCP 查询组件文档、DOM/示例和版本信息后再实现。
   - **Ant Design X（AI 产品按需）**：设计 AI 对话、Agent、数据助理、流式回答时，读取 `companions/ant-design-x/SKILL.md` 与 `components.md`；若项目已安装 `@ant-design/x-skill` 则按任务调用其子技能。组件 API 以 [x.ant.design](https://x.ant.design/) 为准。
   - **VChart（图表必选）**：页面含可视化图表时读取 `companions/vchart/SKILL.md`，按任务核对官方 API；不得把内部数据或文件上传到外部服务。
4. **视觉气质以 `references/DESIGN.md` 为硬规则。** 生成或改版任何 UI / HTML 前必须读取；交付前必须对照 `references/visual-quality.md` 验收。未通过视觉验收不得交付。视觉由 DESIGN.md 定貌；组件 API 跟所选实现库。Ant Design X 仅用于 AI 交互层，不得引入紫粉霓虹「赛博 AI」皮肤覆盖控制台规范。
5. **原型必须可验证。** 每个主任务至少可走通一条交互闭环；只实现用户明确要求的 loading、empty、error、no-permission 等状态，不主动增加状态切换器或演示入口。组件证据记录写入 `evidence.json`；交付前运行 `scripts/validate_prototype.py`。
6. 数据、指标、AI 输出和权限相关内容不得只用颜色表达；必须包含文本、图标或结构化状态。高风险批量操作、权限变更、导出和自动执行必须展示影响范围并确认。
7. **现有界面改进必须过证据门禁。** 读取 `references/design-evidence-gate.md`；只有同时证明设计契约、实际运行路径和唯一修正的候选，才能作为设计问题。用户只要求评审时保持只读；明确要求修改时才实施已证实的修正。
8. **DESIGN.md 只沉淀治理性决策。** 用户明确要求规范/设计系统，或项目约定需要同步设计契约时，读取 `references/design-md-workflow.md`。不得把重复字面量、页面局部样式或案例偏好提升为产品规范。

## 先判断交付物

| 用户目标 | 默认交付物 |
| --- | --- |
| 页面设计 / 信息架构 / 后台 / BI / AI 助理 | **可交互原型** + 简短运行说明 |
| 原型 / 高保真 / 可运行页面 | **可运行工程** + 核心任务闭环 |
| 截图 / Figma 还原 | **可交互还原原型** + 已确认 / 待确认差异 |
| 设计规范 / 设计系统 | 仅用户明确要求时：按 `design-md-workflow.md` 生成可追溯的 DESIGN.md / 规格 |
| 方案、评审、走查、报告 | 仅用户明确要求时：按 `design-evidence-gate.md` 输出有证据的发现 |

## 需求澄清

先读取 `references/brief-template.md`。仅在阻止实现的关键信息缺失时提问；能从现有代码、截图或合理默认值推断的，不重复追问。

1. 当前项目是否已有组件库；否则询问一次技术栈。
2. 原型必须完成的一个主任务与目标用户。
3. 数据口径、权限或高风险动作（未知则以 mock 数据、低风险演示实现并标注）。
4. 现有截图、Figma、品牌 Token 或既有页面。

技术栈询问可用：

> 实现用哪个技术栈？
> 1) Semi Design（默认，React）
> 2) Ant Design（React）
> 3) TDesign（Vue）
> 4) Ant Design X（AI 对话 / Agent UI）
> 不选则按 1) Semi Design 继续。含 AI 对话时可追加：AI 区是否用 Ant Design X 组件？

## 原型工作流（默认）

### 0. 输入分类与最小方案

- 首先读取 `references/context-routing.md`，选择当前阶段最小技能集；不要预读无关知识库或伴生技能。
- 文字需求：提取主任务、数据对象、风险动作和首屏主内容。
- 已有工程：先识别现有框架和组件库，追踪实际页面路径；涉及改进或评审时读取 `references/design-evidence-gate.md`。
- 截图 / Figma：读取 `references/screenshot-to-prototype.md`；先区分可见事实与待确认交互，禁止臆造。
- 设计规范 / 设计系统：读取 `references/design-md-workflow.md`，先建证据账本，再编写或更新文档。
- 不要先输出冗长方案。用不超过 10 行的实现摘要确认默认假设后，直接创建或改造原型。

### 1. MCP 与组件证据

- 用户要求安装 MCP、首次写工程、或 MCP 不可用时：读取并执行 `companions/mcp-setup/SKILL.md`。
- Semi 默认至少取证所需组件的文档 / 示例；Ant、TDesign 通过对应 MCP；AI 对话读取 Ant Design X 伴生。
- 用 `references/evidence-record.template.json` 在原型工程根目录生成 `evidence.json`，记录所用组件、来源、版本和风险。

### 2. 设计与实现

- **任何涉及界面外观、布局或 HTML/UI 输出**：先读 `references/DESIGN.md` 与 `references/visual-quality.md`。
- 数据中台、BI、运营数据页：读取 `references/product-patterns.md` 与 `references/component-selection.md`。
- 需要权限、审计、批量操作或大数据量表格：读取 `references/b2b-operational-patterns.md`。
- AI 数据助理、智能问答、AI 生成报告：额外读取 `references/ai-trust-and-states.md`；**并按需读取** `companions/ant-design-x/SKILL.md` 与 `components.md`（对话/Agent UI 组件选型）。
- **页面含图表**：读取 `companions/vchart/SKILL.md`；图表用 VChart，其余控件用选定栈。
- 默认实现 Vite + React + `@douyinfe/semi-ui`；其它栈只使用已取证 API。
- 将每个主任务写成可操作闭环：入口 → 输入 / 筛选 → 主操作 → 进行中 → 成功或失败 → 结果落点。
- 状态严格按用户要求实现；未要求时只交付主流程正常态，不增加本地状态开关或 mock 状态菜单。
- 不要因实现页面跳过业务规则、权限、高风险确认、数据来源与 AI 不确定性。

### 3. 验证与交付

1. 运行构建或启动命令；修复构建错误。
2. 运行：

```bash
python3 <SKILL_ROOT>/scripts/validate_prototype.py \
  --project <原型工程目录> \
  --stack semi \
  --evidence <原型工程目录>/evidence.json
```

3. 对照 `visual-quality.md` 检查首屏、主按钮、状态和反模式。
4. 默认只交付：运行路径、实现栈、已实现交互、已验证命令、已知限制。
5. 用户明确要求时，才从 `references/output-templates.md` 输出规格、设计系统、评审报告或验收文本。

## B端数据页面规则

- 页面顶部首先呈现任务标题、数据范围、更新时间和全局筛选；筛选影响的范围必须可见。
- 首屏模块预算（硬规则）：标题行 → 筛选条 → KPI（≤4）→ 主表格/主图表。
- 用“概览指标 → 趋势/对比 → 明细与钻取”组织信息，避免把完整报表堆在首屏。
- 图表只回答一个主要问题。说明维度、度量、时间范围、单位、精度与数据更新时点。
- 大表格必须定义列优先级、排序/筛选和横向滚动策略；状态与分页/虚拟化仅按用户要求或已给定业务规则实现。
- 只有一个主操作。批量操作、破坏性操作和高风险操作必须具有明确的选中范围与确认机制。

详细模式见 `references/product-patterns.md` 和 `references/component-selection.md`。视觉气质见 `references/DESIGN.md`。

## AI 数据助理规则

- 明确标识 AI 生成内容、所用数据源、数据时间范围、假设和不确定性。
- 输出必须可编辑、可重新生成、可调整条件或可拒绝；不把 AI 结论表述为确定事实。
- 会改变数据、权限、口径、自动化任务或对外发布的行为，必须先展示影响范围并请求用户确认。
- 对话不是唯一呈现方式：查询结果应根据任务使用指标卡、图表、表格、引用、筛选条件或可执行操作。
- AI 面板使用与工作台一致的 surface + 边框；禁止紫粉渐变、霓虹光效作为默认主题。
- 在首次使用、处理中、出错和结果不可信时提供可理解的恢复路径。
- **AI 对话 UI 组件（按需）**：优先查阅 `companions/ant-design-x/`（Bubble / Sender / Conversations / Prompts / Sources / ThoughtChain / Actions / Welcome / useXChat 等），再落到选定实现栈的代码。

详细状态要求见 `references/ai-trust-and-states.md`。组件映射见 `companions/ant-design-x/components.md`。

## 实现分支（按技术栈）

默认进入本节；用户明确只要文本方案时才不进入。

### A. Semi Design 实现分支（默认）

1. 读取 `references/DESIGN.md`、`references/visual-quality.md`。
2. 通过 Semi MCP 查询所需组件文档与示例；复杂组件再查文件列表、源码或函数实现。
3. 默认交付 **Vite + React + `@douyinfe/semi-ui` 工程**（可双击打开的单文件 HTML 仅在用户明确要求时再做 UMD/CDN 方案）。
4. 只使用已证实的 Semi 组件 API；优先直接 import 组件与图标，不复制组件内部实现。**若含图表**：读 `companions/vchart/`，用 `@visactor/react-vchart` 或 DOM 挂载。
5. 在工程根目录生成 `evidence.json`；完成用户要求的交互闭环。
6. 运行 build、`validate_prototype.py` 与视觉验收。

### B. Ant Design / TDesign 实现分支（用户明确选择时）

1. 读取 `references/DESIGN.md`、`references/visual-quality.md`。
2. 用对应 MCP 取证后再写代码；只输出该库 API。**若含图表**：读 `companions/vchart/`，用 VChart，不用 antd/TDesign 图表组件做最终实现。
3. 交付可运行工程、`evidence.json` 与交互闭环；完成构建和视觉验收。

### C. Ant Design X 实现分支（AI 产品按需 / 用户选择时）

1. 读取 `references/DESIGN.md`、`references/visual-quality.md`、`references/ai-trust-and-states.md`。
2. 读取 `companions/ant-design-x/SKILL.md` 与 `components.md`；按场景选型 Bubble、Sender、Conversations、Prompts、Sources、ThoughtChain、Actions、Welcome 等。
3. 若项目已安装 `@ant-design/x-skill`，按任务读取 `x-components` / `use-x-chat` / `x-request` / `x-markdown` / `x-card` 等子技能后再写代码。
4. 默认交付 **React + `@ant-design/x`**（可与 antd 壳层组合）；页面主栈若为 Semi/TDesign，仅 AI 区使用 X 或复用其模式并声明证据来源。
5. 组件 API 以 [x.ant.design](https://x.ant.design/) 为准；未取证不得臆造。**结果区图表**仍走 VChart 伴生。
6. 交付可运行工程与 `evidence.json`；来源/时效、可修正、高风险确认及失败恢复仅按用户要求和业务规则实现。

### D. VChart 图表层（横切，有图必走）

1. 读取 `companions/vchart/SKILL.md`。
2. 依据业务问题选择图表类型，并通过 VChart 官方文档核对当前 API。
3. 仅替换图表实现；页面其余部分保持当前实现分支的组件库。
4. `evidence.json` 增加 `@visactor/vchart`、版本、文档来源与验证命令。

## 默认交付格式

```markdown
实现栈：{栈}
图表：VChart（若有）
原型位置：{目录或页面}
运行：{命令 / URL}
已实现：{主任务闭环、状态、关键交互}
验证：{build / validate_prototype 结果}
限制：{mock 数据、待接接口、待确认交互}
```

用户明确要求方案、规范、报告、评审时，才读取并使用 `references/output-templates.md` 对应模板。

## 交付前检查

- [ ] 已按 `context-routing.md` 选择当前阶段最小技能集，未同时加载超过 3 个技能。
- [ ] 已读取并遵循 `references/DESIGN.md` 与 `references/visual-quality.md`。
- [ ] 实现栈已确认，或已声明采用默认 **Semi Design**。
- [ ] 若输出组件代码：对应 MCP / 物料已取证，且工程根目录有 `evidence.json`。
- [ ] 主任务可完成一条交互闭环；未主动增加用户未要求的状态演示。
- [ ] 已运行构建 / 启动验证和 `scripts/validate_prototype.py`。
- [ ] 首屏仅：标题 / 筛选 / ≤4 KPI / 主表或主图；仅 1 个 primary 实心按钮。
- [ ] 无营销 Hero、渐变、玻璃拟态、chip 瀑布、紫粉 AI 装饰风。
- [ ] 每条核心规范都有规则级别和适用场景。
- [ ] 页面状态与用户要求一致，无额外状态切换器或 mock 菜单。
- [ ] 小号文本对比度达到 4.5:1；交互状态与相邻颜色达到 3:1。
- [ ] 键盘焦点顺序、弹层初始焦点、Esc 关闭与焦点回收已说明。
- [ ] AI 结果具备来源、时效、可修正和高风险确认机制；若含对话 UI，已按需使用 / 映射 Ant Design X 组件并给出证据来源。
- [ ] 若输出代码：仅包含**选定栈** UI 实现（AI 区按伴生声明；图表用 VChart），已给出组件证据来源。
- [ ] 若改进现有界面：每条发现都已证明契约、运行路径和唯一修正，并完成反证复核。
- [ ] 若创建/更新 DESIGN.md：每条 Token 与规则均可回溯到证据账本，未把局部实现误升为全局规范。
