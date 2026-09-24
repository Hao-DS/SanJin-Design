# 控制台观感（怎么把页面做像工作台）

S2 排版时必读。`visual-quality.md` 管「什么不合格」，本文件管「合格的控制台长什么样」。取值仍只查 `DESIGN.md`，组件 API 仍只查选定栈。

来源（MIT，已剥离冲突项）：[hrhrng/taste-saas-skill](https://github.com/hrhrng/taste-saas-skill) 的结构原型与对齐不变量；[educlopez/ui-craft](https://github.com/educlopez/ui-craft) 的 dense-dashboard 密度。不采用它们的 Tailwind / shadcn / Cmd+K / 8 档风格旋钮 / IBM Plex / 问用户选 Linear 还是 Stripe。

## 结构原型（每项目只选一个，默认写在 Design Read 里）

| 页面类型 | 用哪个 | 做法 |
| --- | --- | --- |
| 列表、监控、用量、资源、规则 | **表优先**（Stripe / Retool） | canvas 底 + **一块** surface 表；不要每行一张卡 |
| 概览、KPI、对比 | **齐平工作台**（Vercel / Sentry） | KPI 与主图/主表左缘对齐；禁止四张大卡漂在灰底上互不挨着 |
| AI 对话、文档、说明 | **整栏工作区** | 对话或正文铺满内容区；结果卡是 surface + 1px 边，不是玻璃/渐变 |

**禁止默认成「舞台上的悬浮卡片」**（Linear 那种圆角卡漂在浅底上）。这是控制台技能里最常见的丑法，也和 DESIGN.md 的 flat-first 冲突。

用户没点名 Linear / 卡片舞台时，不要问四选一，按上表默认。

## 对齐（看起来「散」几乎都是这个）

同一内容列里，下面这些的**左缘必须重合**（差 ≤ 2px）：

1. 页面标题
2. 筛选条
3. KPI 行（若有）
4. 主表 / 主图面板
5. 底部分页

侧栏每个导航图标的中心 x 必须同一条竖线。侧栏第一项顶边与主区标题顶边大致齐平（差 ≤ 8px）。

实现：用脚手架的 `.page` / `.page__head` / `.filter-bar` / `.kpi-row` / `.table-panel`，它们已经吃同一套 24px 页边距。不要给标题另加 8px、给表格再套一层 padding。

S3 用 `getBoundingClientRect().left` 核这几个节点，不要靠截图猜。

## 密度

- 控件高 32px，工具栏 `gap: 8px`。
- 表格行约 36–40px；单元格左右 12px、上下 8px。不要做成营销站那种 56px 疏行。
- 数字列：`font-variant-numeric: tabular-nums` + 右对齐。脚手架 class：`.tabular`。
- ID、工号、时间戳、哈希：等宽 `.mono`，不要用正文比例字体。
- 侧栏 240px、浅底，不要整列深色（那是默认 AI 后台脸）。
- 间距只走 4 / 8 / 12 / 16 / 24。出现 10、14、20 就是在漏。

## 少即是准

- 同一含义的标签只出现一次。面包屑写了「规则」就不要再写一遍页面大标题「规则管理」。
- 环比、状态用纯文字 + 语义色，不要每列一颗彩色胶囊。
- 选中行：约 6% 的 primary 浅底，必要时 3px 左边条；不要整行高饱和铺色。
- 空态：一句话原因 + 一个恢复动作，骨架行要跟列结构同宽，不要一个居中大插画占半屏。
- 图表：趋势用线/面积，构成用条；不用饼图、不用 3D。

## 动效

只要行 hover（浅底、≤100ms）和选中提示。表体里不要入场错落、不要滚动揭晓。

## 不做

- 不换 DESIGN.md 的色、字号、圆角去「更有品味」。
- 不引入第二套字体（IBM Plex / Public Sans / Geist）——内网与中文以系统 UI 为准。
- 不把 Cmd+K、命令面板做成默认交付。
- 不整包安装 taste-saas / Ayla Admin / frontend-design。那些会改栈或把控制台做成落地页。
