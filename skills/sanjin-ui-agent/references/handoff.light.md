# HANDOFF 轻量模板（S4）

仅在用户明确要求标准模式或正式交付说明时使用。默认快速模式不生成 `design/HANDOFF.md`。

**复制下方内容到 `design/HANDOFF.md` 后填写。** 不要先读填写说明。口径与状态细节以 `design/design-spec.md` 为准，这里不重复。

适用：S1 走了轻量档，或 S1 折叠后仍需交付说明。完整档用 `handoff.template.md`。

方括号写完删掉；残留 `[...]` 视为 G4 未通过。

---

~~~~markdown
# [产品/模块名] 原型交付说明

版本：v1 · [日期] · 档位：轻量 · 对应 `design/design-spec.md`

## 1. 运行

    cd prototypes/[name]
    npm install
    npm run dev
    npm run build

入口：`[路由 / URL]`

## 2. 技术栈

| 项 | 值 |
| --- | --- |
| 框架 | Vite + React 18 |
| UI 库 | [@douyinfe/semi-ui x.x] |
| 图表 | [VChart / 占位待换 VChart / 无] |
| 路由 | [hash / 无] |

组件证据：`prototypes/[name]/evidence.json`

## 3. 页面与职责

| 路由 | 文件 | 职责 | 主操作 |
| --- | --- | --- | --- |
| `/` | `src/pages/….jsx` | [一句话] | [主操作] |

壳层：`src/App.jsx`（Sider / Nav 同宽 240）

## 4. 主任务闭环

T1 [任务名]：`[触发] → [进行中] → [成功落点] / [失败恢复]`

接真实系统时：[改哪一层 mock 即可]

## 5. 数据与 mock

位置：`src/mock/`　字段口径见 design-spec 第 6 节，此处不抄。

## 8. 边界

**已实现**：[页面、闭环、状态]

**未实现**：[真实接口、鉴权、…]

**待产品确认**：

| 项 | 原型当前做法 | 需要谁定 |
| --- | --- | --- |
| […] | […] | [产品] |

## 9. 验收用例

来自 design-spec 第 11 节，已在原型上走过。

| # | 页面 | 操作或条件 | 可观察结果 | 原型 |
| --- | --- | --- | --- | --- |
| 1 | [页] | [操作] | [结果] | 通过 |
~~~~
