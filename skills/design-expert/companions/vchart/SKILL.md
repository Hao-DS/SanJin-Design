---
name: design-expert-vchart
description: 设计专家内置的 VChart 图表工作流。页面出现 KPI 趋势、对比、构成、BI 主图或 AI 结果图表时启用；负责图表选型、证据、接入、交互与验收，其它 UI 保持用户选定的 Semi / Ant Design / TDesign。
---

# VChart 伴生技能（设计专家）

> 由「设计专家」在需要渲染真实数据图表时读取。视觉气质仍以 `references/DESIGN.md` 为准；本文件只负责图表渲染层，不依赖其它本地 Skill。

## 何时启用（硬规则）

满足任一条件时必须读取本文件：

| 触发场景 | 示例 |
| --- | --- |
| BI / 数据台主图表 | 趋势、对比、构成、漏斗 |
| AI 助理结果区的图表 | 执行详情 `content_type=chart`、分析报告插图 |
| 用户明确要求 VChart / VisActor | 生成、调试、还原图表 |
| 原型中需要可交互图表（非纯装饰） | 点击、联动、导出、主题 |

**不启用**：纯文案页、无数据可视化的 CRUD、仅用图标/色块表达状态的场景。

## 与实现栈的关系（硬规则）

| 层 | 技术 |
| --- | --- |
| 页面壳 / 表单 / 表格 / 导航 / 反馈 | **用户指定组件库**（Semi / Ant Design / TDesign） |
| AI 对话交互层（可选） | Ant Design X（见 `companions/ant-design-x/`） |
| **图表** | **仅 VChart**（`@visactor/vchart` 或 `@visactor/react-vchart`） |

约束：

1. **图表区域禁止**用组件库自带 Chart / 手写 SVG 柱示意冒充最终图表实现（低保真线框除外，且须标注「待换 VChart」）。
2. **禁止**因引入 VChart 而改用另一套 UI 组件库。
3. VChart 容器样式（边框、padding、标题）跟 DESIGN.md surface；系列色跟设计 Token / 主色，避免紫粉霓虹皮肤。
4. 交付说明中写明图表来源：`图表：VChart（@visactor/vchart）`。

## 取证顺序

1. 本文件（栈边界与启用条件）
2. 项目安装的 `@visactor/vchart` / `@visactor/react-vchart` 版本
3. VChart 官方文档：https://www.visactor.io/vchart/
4. 项目已有图表封装与主题 Token

只读取公开文档；不得向外部站点上传项目源码、数据或设计文件。未核对当前版本 API 时，不编造事件名、配置项或导出能力。

## 栈 → VChart 接入约定

| 用户选定栈 | 图表接入 |
| --- | --- |
| Semi Design（React） | `@visactor/react-vchart` 或 `new VChart(spec, { dom })` |
| Ant Design（React） | 同上 |
| TDesign（Vue） | 同上 Vue 方式 |
| 单文件 HTML 原型 | 使用项目已批准的本地或官方 VChart 资源 |

## 快速工作流

1. 确认页面含图表 → 读本文件。
2. 明确业务问题、维度、度量、时间范围、单位、精度和数据规模。
3. 选择最简单可回答问题的图表：趋势用 line/area，对比用 bar，构成用 pie（类别少）或 stacked bar，流程转化用 funnel。
4. 核对当前 VChart 版本的 `type`、字段映射、数据结构、事件和生命周期 API。
5. 用选定栈实现非图表 UI；图表 DOM 仅作 VChart 挂载点，并在卸载时释放实例。
6. 仅实现用户要求的 loading、empty、error、权限不足或数据更新状态；未要求时不增加图表状态切换器。
7. `evidence.json` 记录库版本、官方文档 URL、已验证 API 和构建/交互验证命令。
8. 对照 `visual-quality.md` 验收（单一分析问题、单位/图例可读、颜色非唯一编码）。

## 与 content_type=chart 的映射

执行详情 / AI 流式结果中的 `chart` 节点：

| payload | VChart |
| --- | --- |
| `spec_type` | `type`（bar / line / pie / …） |
| `spec.x` / `spec.y` / `spec.series` | `xField` / `yField` / `seriesField` |
| `dataset.rows` + `columns` | `data[].values` |
| `summary` / `source` | 图外标题与脚注（非 VChart 内部 title 也可） |

## 交付声明模板

```text
实现栈：{Semi|Ant|TDesign}
图表：VChart（@visactor/vchart）
AI 区（若有）：Ant Design X / 选定栈复刻
证据：evidence.json（含版本、官方文档与验证命令）
```
