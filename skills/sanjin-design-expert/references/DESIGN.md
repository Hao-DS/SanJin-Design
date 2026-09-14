---
version: alpha
name: B2B-Data-Console
description: "Enterprise data-console visual system for data platforms, BI workbenches, and AI data assistants. Light-first, dense but calm, trust-blue primary, flat surfaces with hairline borders. Tokens describe look and feel; implementation stack is selectable (default Semi Design) and must not copy third-party brand skins."

colors:
  primary: "#1677FF"
  on-primary: "#FFFFFF"
  primary-hover: "#4096FF"
  primary-active: "#0958D9"
  primary-soft: "#E6F4FF"
  success: "#52C41A"
  warning: "#FAAD14"
  error: "#FF4D4F"
  info: "#1677FF"
  ink: "#1F1F1F"
  ink-secondary: "#595959"
  ink-tertiary: "#8C8C8C"
  ink-disabled: "#BFBFBF"
  canvas: "#F5F5F5"
  surface: "#FFFFFF"
  surface-subtle: "#FAFAFA"
  border: "#F0F0F0"
  border-strong: "#D9D9D9"
  focus-ring: "#1677FF"

typography:
  page-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
  section-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22px
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 20px
  kpi-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 36px
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  full: 9999px

spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  page-margin: 24px
  section-gap: 24px
  card-padding: 16px
  control-height: 32px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    height: 32px
    padding: 0 15px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    height: 32px
    padding: 0 15px
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    height: 32px
    padding: 4px 11px
  kpi-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 16px 20px
  filter-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 12px 16px
  data-table-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0px
  page-shell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: 24px
---

# B2B Data Console DESIGN.md

本文件遵循 [Google DESIGN.md 规范](https://github.com/google-labs-code/design.md)（YAML token + 正文说明），并吸收 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) / [HU-UH/awesome-design-md](https://github.com/HU-UH/awesome-design-md) 的扩展章节（氛围、组件状态、Do/Don't、响应式、Agent Prompt）。  
**适用范围**：数据中台、BI 报表、数据工作台、AI 数据助理。  
**实现约束**：视觉气质由本文件定义；可运行页面使用用户选定的实现栈（未选择则默认 Semi Design），不得混用其它库组件 API，也不得照搬其它品牌皮肤。

## Overview

视觉主题是 **Enterprise Data Console**：克制、专业、信息密集但可读。像成熟的数据工作台，而不是营销落地页或消费级 SaaS 官网。

- **气质**：冷静、可信、可扫描；用层级与对齐表达专业度，不用装饰表达“高级感”。
- **密度**：桌面默认高效密度（14px 正文、32px 控件），但保留 8/16/24 的呼吸节奏。
- **主色策略**：单一信任蓝作为唯一交互强调色；语义色只服务状态，不服务装饰。
- **页面主角**：筛选后的指标与表格/图表，而不是插画、大英雄区或渐变背景。
- **受众**：产品经理、数据分析师、数据治理/运营人员；阅读路径是“决策摘要 → 解释 → 明细”。

## Colors

调色板以中性灰阶承载内容，以单一 primary 驱动操作。

- **Primary (#1677FF)**：主按钮、链接、选中、焦点环；每屏只保留一个主操作。
- **On-primary (#FFFFFF)**：主按钮文字。
- **Success / Warning / Error / Info**：业务状态与反馈；必须配合文字或图标，不可单靠颜色。
- **Ink (#1F1F1F) / Secondary (#595959) / Tertiary (#8C8C8C)**：正文、次要说明、辅助元数据。
- **Canvas (#F5F5F5)**：页面底色。
- **Surface (#FFFFFF)**：卡片、表格、筛选条等内容容器。
- **Border (#F0F0F0 / #D9D9D9)**：分区与控件描边；用边界而非重阴影建立结构。

禁止引入第二套营销强调色（紫、青、粉渐变）作为页面主视觉。

## Typography

使用系统 UI 字体栈，保证中英文与内网环境可用。只使用 **400** 与 **600** 两档字重。

- **page-title 20/28/600**：页面标题。
- **section-title 16/24/600**：区块标题、表格面板标题。
- **body-md 14/22/400**：正文、表单、表格单元格。
- **body-sm 12/20/400**：辅助说明、筛选摘要、环比文案。
- **kpi-value 28/36/600**：指标卡主数字，是首屏最强数字信号。
- **label 14/22/400**：控件标签与按钮文字。

不要在同一屏混用三套展示字体，不要用斜体或超细字重做界面字。

## Layout

布局遵循 **Fixed-max-width workbench**：内容区建议最大 1440px，页边距 24px（超宽可 32px）。

- 严格 **4px 基线**；常用间距 8 / 16 / 24 / 32。
- 区块间距默认 24px；卡片内边距 16px（紧凑工具条可为 12px 垂直）。
- 首屏模块预算（硬规则）：**标题行 → 筛选条 → KPI（≤4）→ 主表格/主图表**。
- 禁止在首屏堆叠长说明段落、meta chip 瀑布、多个互不相关的卡片墙。
- 筛选影响范围、数据更新时间放在标题行右侧或筛选摘要一行，不单独占一个说明区块。

## Elevation & Depth

默认 **flat-first**。层级靠三层表面完成：

1. `canvas`：页面背景。
2. `surface`：筛选条、KPI、表格面板。
3. `elevated`：仅 Dialog / Drawer / Dropdown / Popover 使用轻阴影。

普通卡片与表格分区优先用 1px 边框和间距，不使用多层投影、玻璃拟态或光晕。

## Shapes

圆角保持克制：

- 控件：6px（`rounded.md`）
- 表面卡片/面板：8px（`rounded.lg`）
- Tag：4px（`rounded.sm`）
- 状态点 / 头像：full

禁止把普通按钮做成大胶囊；禁止在同一视图混用 0px 直角与 16px+ 大圆角。

## Components

### Buttons

- **button-primary**：唯一主操作。实心 primary，高 32px，圆角 6px。
- **button-default**：次要操作。白底描边。
- **button-link**：表格行内操作。不使用实心彩色按钮堆叠。

### Filter Bar

- **filter-bar**：单行优先；标签 + 控件水平排列；查询/重置贴右。
- 生效条件用一行弱文案或少量 Tag 摘要，不使用 chip 瀑布。

### KPI Card

- **kpi-card**：等高；标题弱、数字强；环比用 12px 次要色。
- 异常相关 KPI 可用 3px 左侧语义色条提示，但必须保留文字状态。
- 一屏最多 4 个 KPI。

### Data Table Panel

- **data-table-panel**：工具栏与表头对齐；固定识别列；操作列仅 link。
- 状态列：文案 + Tag（可加色点），禁止只用色块。
- 空态、加载、无权限必须在面板内表达。

### Inputs

- 高度 32px，圆角 6px，focus 使用 primary 描边/环。
- 标签不依赖 placeholder 代替。

### Feedback

- Alert 用于需持续关注的异常；Toast 用于轻反馈。
- 高风险操作使用 Dialog，展示影响范围后再确认。

## Do's and Don'ts

### Do

- 先决定阅读顺序，再摆组件。
- 每屏只保留一个 primary 按钮。
- 用边框、间距、字号建立层级。
- KPI 数字使用 `kpi-value`，环比使用 `body-sm`。
- 状态同时提供文字（和图标）。
- HTML / 工程原型优先复用选定栈默认主题，少写自定义颜色。
- 生成页面前读取本 DESIGN.md，并在交付前做视觉验收。

### Don't

- 不要做营销 Hero、大渐变、玻璃拟态、霓虹光效。
- 不要堆叠 meta chip、说明卡片、统计条造成首屏噪音。
- 不要把未选定库的视觉皮肤硬编码进当前实现页面。
- 不要出现双主按钮或彩色实心操作列。
- 不要用紫色 AI 渐变作为企业数据台默认主题。
- 不要为“好看”增加无任务意义的装饰插画。
- 不要跳过 empty / loading / error / no-permission 状态。

## Responsive Behavior

| 断点 | 行为 |
| --- | --- |
| ≥1280 | 4 KPI 横排；筛选可单行 |
| 768–1279 | KPI 2×2；筛选可两行 |
| <768 | KPI 单列；表格横向滚动；抽屉改全宽 |

触控场景控件高度提升到 40px；桌面数据台默认保持 32px。

## Agent Prompt Guide

生成或改版页面时，优先使用以下约束句：

```text
遵循 references/DESIGN.md（B2B-Data-Console）。
视觉：克制专业、flat-first、单一信任蓝、首屏仅标题/筛选/≤4 KPI/主表。
禁止：营销 Hero、渐变、玻璃拟态、chip 瀑布、双主按钮、紫粉 AI 装饰风。
实现：先询问技术栈；用户不选则默认 Semi Design；先取组件证据再写代码；禁止混库。Nubes HTML 须显式闭合 nb-* 标签。
```

快速 Token 对照：

| 用途 | Token |
| --- | --- |
| 页面底 | `{colors.canvas}` |
| 内容面 | `{colors.surface}` |
| 主操作 | `{colors.primary}` |
| 正文 | `{colors.ink}` + `{typography.body-md}` |
| 指标数字 | `{typography.kpi-value}` |
| 圆角控件 | `{rounded.md}` |
| 圆角卡片 | `{rounded.lg}` |
| 页边距 | `{spacing.page-margin}` |

## Sources

- Format: [google-labs-code/design.md](https://github.com/google-labs-code/design.md)（技能包内必要规范：`knowledge/design-md/google-spec/`）
- Collection pattern: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)、[HU-UH/awesome-design-md](https://github.com/HU-UH/awesome-design-md)（5 个精选样例：`knowledge/design-md/examples/`）
- Enterprise console principles for B-end data products with selectable implementation stack（default Semi Design; not a copy of any single brand skin）
