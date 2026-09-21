# SanJin-设计专家

B 端数据中台 / BI / AI 数据助理设计技能（技术标识：`sanjin-design-expert`）。默认交付可运行、可交互的高保真原型；设计规范和评审报告仅在用户明确要求时产出。本目录是可独立分享的极简技能包，不依赖仓库内其它 Skill。

## 目录结构

```text
sanjin-design-expert/
├── SKILL.md                 # 技能入口（必读）
├── README.md                # 本说明
├── references/              # 设计规范、Token、模板、验收
│   ├── DESIGN.md            # 产品默认视觉硬规则
│   ├── visual-quality.md
│   ├── ui-judgment.md       # UI 判断规则入口（与技术栈无关）
│   ├── ui-judgment/         # 层级 / 布局与滚动 / 状态 / 动效
│   ├── context-routing.md    # 按需上下文路由
│   ├── design-evidence-gate.md # 设计问题证据门禁
│   ├── design-md-workflow.md # DESIGN.md 证据化沉淀
│   ├── brief-template.md    # 原型需求最小模板
│   ├── prototype-delivery.md# 原型闭环与验证
│   └── ...
├── scaffold/                # Semi 原型脚手架模板（复制起工程）
├── scripts/
│   └── validate_prototype.py # 单栈、证据与视觉风险检查
├── knowledge/design-md/     # Google DESIGN.md 格式规范
├── companions/
│   ├── mcp-setup/           # 协助安装 Semi / Ant Design / TDesign MCP
│   ├── ant-design-x/        # AI 产品按需：Ant Design X 组件与场景映射
│   └── vchart/              # 图表层：VChart（其它 UI 仍用选定栈）
└── examples/
    └── 数据中台-任务监控.html
```

## 安装（分享给同事）

1. 将整个 `sanjin-design-expert` 文件夹复制到目标项目的：
   - `.agents/skills/sanjin-design-expert/`，或
   - `.cursor/skills/sanjin-design-expert/`
2. **配置组件库 MCP（写代码强烈推荐）**：让 Agent 按 `companions/mcp-setup/` 写入项目 `.cursor/mcp.json`，或手动复制 `companions/mcp-setup/mcp.json.example`。最少装 **Semi MCP**；步骤见 `companions/mcp-setup/INSTALL.md`。
3. **默认实现栈为 Semi Design**：通过 Semi MCP 取得组件文档和示例证据，调用方式按 `references/mcp-evidence-protocol.md`（先清单后文档，定向取字段）。
4. **AI 产品（可选增强）**：伴生 `companions/ant-design-x/` 已内置。需要官方完整技能包时可安装 [`@ant-design/x-skill`](https://x.ant.design/x-skills/introduce-cn/)（`npm i -g @ant-design/x-skill && npx x-skill`）。
5. **图表**：`companions/vchart/` 已内置；实现时核对项目 VChart 版本和官方 API。
6. （可选）将 `references/DESIGN.md` 复制到项目根，便于任意 Agent 发现。

## 路径约定（技能内相对路径）

| 用途 | 路径 |
| --- | --- |
| 视觉硬规则 | `references/DESIGN.md` |
| 视觉验收 | `references/visual-quality.md` |
| UI 判断规则（层级 / 布局 / 状态 / 动效） | `references/ui-judgment.md` + `references/ui-judgment/` |
| DESIGN.md 官方格式 | `knowledge/design-md/google-spec/docs/spec.md` |
| 按需上下文路由 | `references/context-routing.md` |
| 设计问题证据门禁 | `references/design-evidence-gate.md` |
| DESIGN.md 沉淀流程 | `references/design-md-workflow.md` |
| 组件取证调用协议 | `references/mcp-evidence-protocol.md` |
| 原型脚手架模板 | `scaffold/` |
| MCP 安装助手 | `companions/mcp-setup/` |
| 原型需求 / 交付规范 | `references/brief-template.md`、`references/prototype-delivery.md` |
| 截图还原规范 | `references/screenshot-to-prototype.md` |
| 证据模板 / 原型校验 | `references/evidence-record.template.json`、`scripts/validate_prototype.py` |
| 权限 / 审计 / 性能模式 | `references/b2b-operational-patterns.md` |
| Ant Design X（AI 按需） | `companions/ant-design-x/` |
| VChart（图表） | `companions/vchart/` |
| 示例页面 | `examples/数据中台-任务监控.html` |

## 使用边界

- **产品默认视觉**：只用 `references/DESIGN.md`，不要直接套用合集里的 Linear/Stripe 等营销皮肤。
- **三层分工**：`DESIGN.md` 定取值，`visual-quality.md` 判合格，`ui-judgment/` 给方法。判断规则与技术栈无关，换栈不需重新判断；但它不产出取值，也不放宽前两者的硬规则。
- **默认产物**：页面、后台、BI、AI 助理与截图还原请求，默认直接实现可交互原型；只有明确提出“规范、方案、报告、评审”时才输出对应文本。
- **按需路由**：同一阶段使用 `sanjin-design-expert` + 至多 2 个必要伴生；AI、图表和基础实现分阶段加载。
- **改进证据**：现有界面改进必须同时证明设计契约、实际运行路径和唯一修正；没有充分证据时不凑问题。
- **规范沉淀**：DESIGN.md 只记录可追溯的治理性决策，不把重复值、局部样式或案例皮肤提升为规范。
- **实现库**：进入可运行页面 / 工程前先询问用户技术栈；用户不选择则默认 Semi Design。支持 Semi / Ant Design / TDesign；AI 区按需使用 Ant Design X。
- **图表**：有可视化图表时统一用 **VChart**（`companions/vchart/`），其它控件仍用选定栈。
- **AI 对话区**：设计 AI 产品时按需启用 `companions/ant-design-x/`（[Ant Design X Skills](https://x.ant.design/x-skills/introduce-cn/)）。
- **按需读取**：只加载当前任务需要的 references 或 companion；不要预读全部资料。
