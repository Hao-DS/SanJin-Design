# 组件库 MCP 安装指南（Cursor）

面向分享「SanJin-设计专家」技能后的同事：不装 MCP 仍可做设计方案；**写可运行组件代码时建议至少安装 Semi MCP**。

前置：已安装 [Node.js](https://nodejs.org/) 18+，终端可执行 `node -v` / `npx -v`。

## 1. 配置文件放哪

| 范围 | 路径 |
| --- | --- |
| 仅当前项目（推荐分享场景） | 项目根目录 `.cursor/mcp.json` |
| 本机所有项目 | `~/.cursor/mcp.json` |

## 2. 推荐配置（可整段复制）

把 [`mcp.json.example`](mcp.json.example) 合并进上述文件。最小可用（仅默认栈）：

```json
{
  "mcpServers": {
    "semi-mcp": {
      "command": "npx",
      "args": ["-y", "@douyinfe/semi-mcp"]
    }
  }
}
```

完整三件套（Semi + Ant Design + TDesign）：

```json
{
  "mcpServers": {
    "semi-mcp": {
      "command": "npx",
      "args": ["-y", "@douyinfe/semi-mcp"]
    },
    "antd": {
      "command": "npx",
      "args": ["-y", "@ant-design/cli", "mcp"]
    },
    "tdesign-mcp-server": {
      "command": "npx",
      "args": ["-y", "tdesign-mcp-server@latest"]
    }
  }
}
```

保存后：**重启 Cursor**，或 Command Palette → `Developer: Reload Window`。  
打开 **Settings → Tools & MCP**，对应服务器应为已连接（绿灯）。

## 3. 官方来源说明

| MCP | 包名 | 说明 | 文档 |
| --- | --- | --- | --- |
| Semi | `@douyinfe/semi-mcp` | 【官方】Semi Design MCP | https://semi.design （AI / MCP 相关文档） |
| Ant Design | `@ant-design/cli` → `mcp` | 【官方】antd MCP | https://ant.design/docs/react/mcp |
| TDesign | `tdesign-mcp-server` | TDesign 组件文档 MCP | 以 npm 包 `tdesign-mcp-server` 为准 |

内网若禁止公网 npm：请改用公司镜像，或联系管理员同步上述包；**不要**使用来源不明的第三方 MCP 包冒充官方。

## 4. 一键命令（可选）

```bash
# Ant Design：官方 CLI 写入 Cursor MCP 配置
npx -y @ant-design/cli setup --client cursor --mode mcp

# 预装 CLI（可选，加快启动）
npm install -g @douyinfe/semi-mcp @ant-design/cli
```

## 5. Ant Design X（技能包，不是 MCP）

AI 对话 / Agent UI 额外推荐：

```bash
npm i -g @ant-design/x-skill
npx x-skill
```

文档：https://x.ant.design/x-skills/introduce-cn/

「SanJin-设计专家」内已有伴生：`companions/ant-design-x/`。

## 6. 验证是否成功

在 Cursor Agent 中试一句：

- Semi：`用 Semi MCP 查一下 Table 组件的基本用法`
- Ant Design：`用 antd MCP 列出 Form 相关 API`
- TDesign：`用 TDesign MCP 查一下 Dialog 文档`

若 Agent 能返回组件文档/示例，即配置成功。

## 7. 常见问题

| 现象 | 处理 |
| --- | --- |
| MCP 一直转圈 / 失败 | 确认 Node/npx 在 PATH；macOS 从 Dock 启动 Cursor 时偶尔找不到 npx，可把 `command` 改成 `npx` 的绝对路径 |
| `npx` 卡住 | args 必须带 `-y`，避免交互确认 |
| 403 / 装包失败 | 内网源拦截；改用官方 registry 或公司已同步镜像 |
| 配置了但不生效 | 检查 JSON 根键必须是 `mcpServers`；保存后 Reload Window |
| 与已有 mcp.json 冲突 | 合并对象，勿删除同事已有的其它 server |

## 9. 请 Agent 代劳时可以说

> 用「SanJin-设计专家」帮我安装 Semi / Ant Design / TDesign 的 MCP，写入项目 `.cursor/mcp.json`，不要删掉我已有的其它 MCP。
