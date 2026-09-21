# 组件取证调用协议

本文件回答「**怎么取**」：用什么顺序调 MCP，取到的东西怎么落地，才能既满足「未取证不得臆造 API」，又不把整本组件文档拖进上下文。

取证的**义务**在 `SKILL.md` 边界规则 3，本文件不放宽它：仍然是所用组件的 API 必须来自选定栈的 MCP / 物料。
本文件只约束**取的方式**。

## 总原则

1. **先清单后文档。** 不确定组件是否存在、导出名怎么写时，先要清单再要文档；清单便宜，猜错名字要多花一整轮。
2. **先写清单再调用。** 动手前把本页需要的组件一次列全，合并成一批调用，不要边写边想起来就补一次。
3. **带着问题取，不整篇读。** 调用前先写下要确认的 props / 事件；拿到文档只提取这几项。
4. **越贵的来源越靠后。** 清单 → 文档 → 单个示例 → 源码，前一层能回答就不进下一层。

## 调用顺序

| 步骤 | 目的 | Semi | TDesign |
| --- | --- | --- | --- |
| 1 清单 | 确认组件存在与准确名称 | `get_semi_document` **不传** `componentName` | `get-component-list`（需 `framework`） |
| 2 文档 | 取 props / 事件 / 类型 | `get_semi_document(componentName)` | `get-component-docs(framework, names[])`，**支持批量** |
| 3 示例 | 取某个具体用法 | `get_semi_code_block(componentName, codeBlockIndex)` | 文档内已含示例 |
| 4 源码 | 文档回答不了的内部行为 | `get_component_file_list` → `get_file_code` → `get_function_code` | `get-component-dom`（改样式时） |

Ant Design MCP 同样按「清单 → 文档 → 示例」推进，具体工具名以该 MCP 自己的 schema 为准，不要照搬上表。

步骤 1 尤其能避免空转：Semi 的侧边导航组件文档名是 `navigation` 而不是 `Nav`，直接按组件名查会落空。

## 大文档不要整篇读

文档超过阈值时会被转存成文件并只返回路径。**这时用 Grep 定向检索该文件，不要整篇 Read。**

典型量级：Semi `Table` 约 55 KB / 960 行，实际需要的通常是 `columns`、`scroll`、`rowSelection`、`pagination`、`fixed` 这几行表格行。
先 `rg '^\| (columns|scroll|rowSelection|fixed|ellipsis) '` 拿到属性表，再 `rg '^#+ '` 拿章节目录判断要不要看示例，比整篇读省一个数量级。

代码块同理：Semi 文档里的示例默认是占位符，按需只取用得上的那个序号，不要把所有代码块都拉出来。

## 每个组件的默认预算

| 组件复杂度 | 允许的调用 |
| --- | --- |
| Button、Input、Checkbox、Divider 等基础件 | 与同批组件合并，尽量只靠清单与既有文档确认；不单独开一轮 |
| Table、Form、DatePicker、Tree 等复杂件 | 1 次文档 + 最多 2 次定向调用（示例或源码） |
| 文档无法解释的行为 | 追加源码调用，并在 `evidence.json` 记录原因 |

超出预算说明问题没想清楚：回到「要确认哪几个 props」重新收敛，而不是继续翻文档。

## 读得多、产出少的活交给子代理

组件文档这类任务的特征是**读入几万字符、最终只用上十几行**。这部分内容留在主上下文里，会在后续每一轮被重复携带。

符合下面两条时，派一个子代理去做，只让它回传提取结果：

- 需要翻阅的原文远大于结论（单个文档超过约 20 KB，或要跨多个文档比对）
- 结论可以用结构化的短文本表达（属性名、类型、默认值、一小段示例）

给子代理的指令要写清**要哪几个字段**和**回传格式**，否则它会把整篇摘要带回来，白费一层：

```text
用 Semi MCP 查 Table 组件文档，只回传这些属性的名称、类型、默认值：
columns、dataSource、rowSelection、scroll、pagination、empty、loading，
以及 Column 的 fixed、width、ellipsis。
再取「固定列或表头」一节的代码块，只回传 scroll 与 fixed 的写法。
不要复述其它章节，不要附加说明。
```

不适合派子代理的情况：只查一两个属性（一次调用就完事，派发反而更贵）、
需要结合页面上下文反复追问的行为细节。

## 不该走 MCP 的两类信息

- **图标名**：直接列本地包目录核对，例如 `ls node_modules/@douyinfe/semi-icons/lib/es/icons`，逐个比对要用的名字。Semi MCP 的 icons 入口只返回 2 个聚合文件，问不出图标清单。
- **包的真实导出与路径**：以 `node_modules` 里的 `package.json`（尤其 `exports` 字段）为准。文档写的路径可能被 `exports` 挡住——Semi 文档给的 `@douyinfe/semi-ui/dist/css/semi.min.css` 就不在 `exports` 里，需要别名或相对路径绕过。

## 记进 evidence.json

`components[].evidence` 写**取到了什么**，不是「查过文档」。带上工具名与关键字段，便于复核和换版本时重查：

```json
{
  "pattern": "任务列表主表格：固定列、内部滚动、行选择",
  "component": "Table",
  "source": "semi-mcp",
  "evidence": "get_semi_document: Table（columns / scroll / rowSelection / empty / pagination）；get_semi_code_block: Table #8（fixed 列 + scroll.x/y）",
  "risk": "真实列集合与排序能力未知"
}
```

本地包核对同样要记，`source` 写 `local-package`，`evidence` 写核对路径。
