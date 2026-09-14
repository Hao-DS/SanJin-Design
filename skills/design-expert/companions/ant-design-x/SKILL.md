---
name: ant-design-x
description: Ant Design X（@ant-design/x）AI 产品组件与技能指南。设计或实现 AI 对话、Agent、数据助理、流式回答、提示词面板时按需使用。覆盖 Bubble、Sender、Conversations、Prompts、ThoughtChain、Welcome、Attachments、Sources、Suggestion、Think、XCard、useXChat、XRequest、x-markdown 等。
---

# Ant Design X 伴生技能

专为 **AI 对话 / Agent / 数据助理** 界面提供组件选型与实现指引。  
官方介绍：[Ant Design X Skills](https://x.ant.design/x-skills/introduce-cn/) · 技能列表：[skills-cn](https://x.ant.design/x-skills/skills-cn/)

> **调用关系**：由「SanJin-设计专家」在 AI 产品场景下按需读取。
> 视觉气质仍以「SanJin-设计专家」`references/DESIGN.md` 为准；本伴生只负责 **AI 交互层组件与 SDK**，不得用紫粉霓虹 AI 装饰风覆盖企业数据台规范。

## 何时启用（硬规则）

满足任一条件时，**必须先读本文件**，再按任务选读下方组件表：

| 触发场景 | 示例 |
| --- | --- |
| AI 对话界面 | 智能问答、Copilot、多轮聊天 |
| AI 数据助理 | 指标解释、自然语言查数、生成报告 |
| Agent / 工具调用 | 计划→确认→执行、思维链、动作条 |
| 流式生成与富内容 | Markdown 流式、引用 Sources、附件、代码块 |
| 用户明确要求 Ant Design X / `@ant-design/x` | 实现或高保真原型 |

**不启用**：纯 BI 报表、普通后台 CRUD、无对话的配置台——继续用 Semi / Nubes / Ant / TDesign 常规组件。

## 与实现栈的关系

| 情况 | 处理 |
| --- | --- |
| 用户选定 **Ant Design X** 或 **Ant Design + X** | AI 对话区用 `@ant-design/x`；页面壳可用 antd Layout |
| 用户选定 Semi / Nubes / TDesign，但需求含 AI 对话 | **推荐规则**：对话/助理区域优先映射到 Ant Design X 组件模式；若工程禁止混库，则用选定栈复刻同等信息架构，并在交付说明中标注「模式来源：Ant Design X」 |
| 仅做设计规范、不写代码 | 用本文件组件表做选型与状态矩阵，不输出具体 import |

一旦输出 `@ant-design/x` 代码，**禁止**与 Semi / Nubes / TDesign 组件 API 混在同一交互树上。

## 取证顺序

1. 本伴生 `components.md`（场景 → 组件映射）
2. 若项目已安装 `@ant-design/x-skill` 技能包：按任务读取对应子技能（见下表）
3. 官方文档：[x.ant.design](https://x.ant.design/)（组件 props 以官网为准，未取证不得臆造）
4. Ant Design MCP：仅用于配套 antd 壳层（Button、Layout、Form 等），**不是** X 组件 API 来源

## 官方技能包（可选安装）

来源：[介绍](https://x.ant.design/x-skills/introduce-cn/)

```bash
# 全局安装技能库（官方推荐）
npm i -g @ant-design/x-skill
# 交互式注册到当前 IDE
npx x-skill
```

| 技能包 | 子技能 | 用途 |
| --- | --- | --- |
| x-components | `x-components` | Bubble、Sender、Conversations、Prompts、ThoughtChain、Actions、Welcome、Attachments、Sources、Suggestion、Think、FileCard、CodeHighlighter、Mermaid、Folder、XProvider、Notification |
| x-sdk-skills | `use-x-chat` | useXChat、消息管理、错误处理、多会话 |
| x-sdk-skills | `x-chat-provider` | 自定义 Chat Provider / 流式适配 |
| x-sdk-skills | `x-request` | XRequest 配置 |
| x-sdk-skills | `x-card` | XCard / A2UI 动态富交互卡片 |
| x-markdown | `x-markdown` | 流式 Markdown、插件、主题、聊天富文本 |

项目内未安装时：以本伴生 + 官网文档为准，不要假装已读取上游 skill 全文。

## 快速工作流

1. 确认是 AI 产品界面（见「何时启用」）。
2. 读「SanJin-设计专家」`references/ai-trust-and-states.md`（信任 / 确认 / 失败态硬规则）。
3. 读本文件 + `components.md`，选定组件组合。
4. 若写代码：先查官网或已安装的 `x-components` / `use-x-chat` 再实现。
5. 对照「SanJin-设计专家」`visual-quality.md` 做视觉验收（flat、单一 primary、无紫粉 AI 装饰）。

## 交付声明

实现 AI 对话区时，在交付说明中写明：

```text
AI 组件来源：Ant Design X（@ant-design/x）
伴生：companions/ant-design-x
证据：官方文档 / x-skill 子技能（如已安装）
```
