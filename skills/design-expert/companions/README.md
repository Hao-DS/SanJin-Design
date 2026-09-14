# 伴生技能

| 目录 | 说明 |
| --- | --- |
| `mcp-setup/` | 协助安装 Semi / Ant Design / TDesign MCP（`mcp.json.example` + `INSTALL.md`）。**写组件代码前缺 MCP 时必读。** |
| `ant-design-x/` | Ant Design X（`@ant-design/x`）AI 对话 / Agent 组件。**设计 AI 产品时按需必读。** |
| `vchart/` | VisActor VChart 图表层。**页面有可视化图表时必读**；其它 UI 仍用选定栈。 |

默认实现栈为 Semi Design（询问用户；不选则默认）。Semi、Ant Design 和 TDesign 组件 API 直接通过对应 MCP 取证，不依赖其它本地 Skill。

AI 对话 / Agent UI 取证顺序：

1. 本包 `companions/ant-design-x/SKILL.md` + `components.md`
2. 若已安装官方 [`@ant-design/x-skill`](https://x.ant.design/x-skills/introduce-cn/)，按任务读对应子技能
3. 官网 [x.ant.design](https://x.ant.design/) 组件文档

图表取证顺序：

1. 本包 `companions/vchart/SKILL.md`
2. 项目安装的 VChart 版本与已有封装
3. 官网 [visactor.io/vchart](https://www.visactor.io/vchart/)

分享时复制完整 `design-expert/` 目录即可；写组件代码前按 `mcp-setup/` 配置所需 MCP。
