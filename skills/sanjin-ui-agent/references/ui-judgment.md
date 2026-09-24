# UI 判断规则（与技术栈无关）

本文件回答「**怎么判断**」：信息谁主谁次、空间怎么分、哪一层滚、要不要做这个状态、该不该加这个动效。
规则不绑定任何组件库，Semi / Ant Design / TDesign / 纯 HTML 都适用。

## 与相邻文件的边界

三者分工不重叠，冲突时按下表优先级裁决：

| 你要的 | 读这里 | 它管什么 |
| --- | --- | --- |
| 颜色、字号、圆角、间距的**准确取值** | `references/DESIGN.md` | 定貌。取值的唯一真源 |
| 交付前判断**合不合格** | `references/visual-quality.md` | 硬清单与反模式。未过不得交付 |
| 动手前判断**该怎么做** | 本文件与 `ui-judgment/` | 方法。不产出取值，也不放宽硬规则 |

本文件**不覆盖**：`references/DESIGN.md` 的任何 token 与硬规则；组件内部尺寸、props、ARIA 与键盘行为（以选定栈 MCP 证据为准）；
现有界面的问题举证（读 `references/design-evidence-gate.md`）；B 端权限、审计、大数据量模式（读 `references/b2b-operational-patterns.md`）。

## 按问题读取

单点问题只读对应文件，不要通读。

| 问题 | 读取 |
| --- | --- |
| 信息主次、分组、呈现形式与阅读顺序 | `references/ui-judgment/hierarchy.md` |
| 位置、尺寸、对齐、滚动归属、响应式重排、长内容 | `references/ui-judgment/layout.md` |
| 要做哪些状态、loading / empty / error / 权限、反馈组件选型 | `references/ui-judgment/states.md` |
| 要不要动效、动效表达什么、reduced motion | `references/ui-judgment/motion.md` |

完整页面通常按 `references/ui-judgment/hierarchy.md` → `references/ui-judgment/layout.md` 的顺序；状态和动效在需求已定义对应行为时再读。

## 三条总原则

1. **任务决定主次，视觉只负责表达已确认的主次。** 没有产品依据时，不用字号、面积或颜色制造优先级。
2. **只做需求明确要求、且有可见差异的东西。** 不为凑齐清单补状态、补动效、补空态。
3. **不能确认的标为待确认。** 不从颜色、组件名、按钮文案反推业务含义；缺 token 或缺组件能力时记录缺口，不就近找一个蒙过去。

## 出处

方法部分本地化自 [`@cloudai-design/oneskill`](https://www.npmjs.com/package/@cloudai-design/oneskill)（MIT）的 `design-system/`，
已剥离其 Tailwind v3 + shadcn 的类名、token 名与品牌色体系，取值一律改绑本技能 `references/DESIGN.md`。
原包中与技术栈耦合的组件层、主题层和页面模板未纳入。
