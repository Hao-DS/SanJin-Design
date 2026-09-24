# 设计流水线编排

本文件是阶段与门禁的唯一真源。默认快速模式；明确要求正式需求、规范或交付文档时走标准模式。两种模式都以 Figma 静态稿 → 人工评审和优化 → 明确确认 → 交互实现为主线。用户明确要求跳过设计稿直接开发时遵从当次要求。

## 快速模式

F1 Design Read → F2 Figma 静态稿 → F3 设计自检 → 人工确认 → F4 交互实现及验证。细节见 fast-mode.md。

F3 后停下等待用户对当前审阅版本的明确确认；反馈修改则退回 F2。将 Figma 链接、Frame、审阅版本、确认人、确认时间、确认版本记入 design/pipeline.json。状态可用 pending、in_progress、awaiting_review、done、stale。只记录实际收到的确认，不代用户填写。设计稿修改后递增版本，清空旧确认，F4 标为 stale。

F4 完成条件：工程构建通过、validate_prototype.py 无 error，浏览器走通主任务、关键状态与恢复路径。设计稿阶段不运行前端构建或代码校验。

## 标准模式

S1 需求转化 ─G1→ S2 Figma 静态设计 ─G2→ S3 交互实现 ─G3→ S4 交付 ─G4→ 下游开发。

| 阶段 | 输入 | 产物 | 主要依据 |
| --- | --- | --- | --- |
| S1 需求转化 | PRD、截图、现有页面 | design/design-spec.md；折叠档用 brief-template.md 回显 | prd-to-design-spec.md |
| S2 静态设计 | 已确认需求 | 可编辑 Figma Frame、关键状态、审阅版本 | DESIGN.md、visual-quality.md、console-craft.md |
| S3 交互实现 | 人工确认的 Figma 版本 | prototypes/<name>/ 工程、evidence.json | prototype-delivery.md、mcp-evidence-protocol.md |
| S4 交付 | 已验证工程 | design/HANDOFF.md | 对应 handoff 模板 |

### 门禁

- G1 需求确认：主任务、页面与路由、数据口径、权限与高风险行为、关键状态、假设和验收路径已写清，且获得用户确认。轻量和完整档按对应 design-spec 模板；折叠档按 brief 回显。未确认不开始 S2。
- G2 设计确认：Figma Frame 覆盖页面和关键状态；设计满足 DESIGN.md 与 visual-quality.md；用户明确确认当前版本。修改意见先落实到 Figma 并重新提交；没有确认不写交互代码。
- G3 实现验收：实现与确认 Frame 一致；页面和状态可达；高风险操作有影响范围及二次确认；mock 符合 mock-data-realism.md；evidence.json 覆盖组件；构建和 validate_prototype.py 通过；主任务在浏览器走通；视觉与基本无障碍检查通过。
- G4 交付完整：HANDOFF 按档位写全；页面、状态、字段口径和验收用例与工程一致；写明已确认 Figma 版本及已实现、未实现、待确认事项；流水线没有 stale 残留。

G1、G2 是标准模式的人工确认点；G3、G4 是执行者自检。门禁未过就留在当前阶段。

### 产物档位

| 档位 | 条件 | S1 | S4 |
| --- | --- | --- | --- |
| 折叠 | 单页、无新路由或实体、无权限及高风险操作，且未要求正式需求 | brief-template.md 回显 | handoff.light.md |
| 轻量 | 不超过两页、无高风险操作 | design-spec.light.md | handoff.light.md |
| 完整 | 其余或用户要求完整需求 | design-spec.template.md | handoff.template.md |

页面数量与复杂度不影响模式选择。所有档位均须产出 Figma 静态稿并过 G2。高风险批量改数据、权限、导出、发布或自动执行选完整档。

### 状态与回退

design/pipeline.json 记录模式、当前阶段、Figma 链接和 Frame、审阅版本、确认人、确认时间和确认版本、原型路径、阶段状态和变更记录。门禁值为 pending、passed、failed。

| 变化 | 退回 | 失效范围 |
| --- | --- | --- |
| 主任务、页面、路由、数据对象或权限变化 | S1 | S2–S4，G1 与 G2 重新确认 |
| 设计结构、状态、视觉决定或关键文案变化 | S2 | S3–S4，G2 重新确认 |
| 仅实现细节且不影响确认稿 | S3 | S4，G3 重验 |
| 仅交付说明变化 | S4 | G4 重验 |

用户要求按已有设计稿直接实现时，先确认该稿是实现基线并记录链接与版本；无法确定版本时提交待确认项，不猜测。阶段与人工门禁始终串行。
