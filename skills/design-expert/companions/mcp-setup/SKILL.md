---
name: mcp-setup
description: 帮助用户在 Cursor 中安装并配置「设计专家」所需的组件库 MCP（Semi、Ant Design、TDesign）。当用户提到安装 MCP、配置 mcp.json、MCP 不可用、或首次使用设计专家写组件代码时使用。
---

# 组件库 MCP 安装助手

本伴生帮助用户把「设计专家」依赖的组件库 MCP 配进 Cursor，从而能按官方文档取证写代码。

官方 / 包来源均为各组件库官方或常用官方通道（见下方链接）。内网环境请确认可访问 npm 官方源或公司已同步的镜像。

## Agent 行为（硬规则）

当出现以下任一情况时，**先读本文件并协助安装/配置**，再写组件代码：

1. 用户明确要求「安装 MCP / 配置组件库 MCP」
2. 选定实现栈后，对应 MCP 不可用或调用失败
3. 用户首次用本技能做可运行原型，且未配置任何 MCP

协助步骤：

1. 确认用户使用 **Cursor**（本指南默认 Cursor；其它 IDE 见 INSTALL.md 附录）
2. 询问要装哪些：推荐默认 **Semi**；按需加 Ant Design / TDesign
3. 检查项目是否已有 `.cursor/mcp.json`；有则合并，无则创建（使用本目录 `mcp.json.example`）
4. 提醒用户：**保存后重启 Cursor 或 Reload Window**，在 Settings → Tools & MCP 确认绿灯
5. 用一句探测请求验证（如「用 Semi MCP 查一下 Button 文档」）

**禁止**：在未获用户同意时覆盖其已有 MCP 配置中的无关服务器；合并时保留原有项。

## 快速安装（推荐给用户）

### 方式 A：一键复制配置（Cursor 项目级）

1. 将本目录 [`mcp.json.example`](mcp.json.example) 内容合并进项目根目录 `.cursor/mcp.json`
2. 最少只需保留 `semi-mcp`（默认栈）；其它按需保留
3. 重启 Cursor → Settings → Tools & MCP 查看状态

### 方式 B：命令行辅助（需 Node.js 18+）

```bash
# 可选：预拉包，加快首次启动
npm install -g @douyinfe/semi-mcp
npm install -g @ant-design/cli
# TDesign 一般用 npx，无需全局安装
```

Ant Design 也可用官方一键写入 Cursor 配置（【官方】）：

```bash
npx -y @ant-design/cli setup --client cursor --mode mcp
```

文档：https://ant.design/docs/react/mcp

### 方式 C：Ant Design X 技能（非 MCP，AI 对话用）

```bash
npm i -g @ant-design/x-skill
npx x-skill
```

介绍：https://x.ant.design/x-skills/introduce-cn/

## 各 MCP 对照

| 用途 | Cursor 配置名（建议） | 启动方式 | 优先级 |
| --- | --- | --- | --- |
| Semi Design（默认栈） | `semi-mcp` | `npx -y @douyinfe/semi-mcp` | **强烈推荐** |
| Ant Design | `antd` | `npx -y @ant-design/cli mcp` | 选用 Ant 时 |
| TDesign | `tdesign-mcp-server` | `npx -y tdesign-mcp-server@latest` | 选用 TDesign 时 |
| Ant Design X | — | `@ant-design/x-skill` 或官网 | AI 对话时 |

详细步骤、排障与完整 JSON 见 [INSTALL.md](INSTALL.md)。
