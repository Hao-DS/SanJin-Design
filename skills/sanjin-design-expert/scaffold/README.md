# 原型脚手架模板

Semi Design（默认栈）的 Vite + React 原型骨架。新建原型时复制本目录，避免每次重造同样四个配置文件、重踩同样的环境坑。

模板文件以 `_` 前缀命名，防止被包管理器和构建工具当成真实配置。复制时去掉前缀：

| 模板 | 落地为 |
| --- | --- |
| `_package.json` | `package.json`（改 `name`） |
| `_gitignore` | `.gitignore` |
| `_vite.config.js` | `vite.config.js` |
| `_index.html` | `index.html`（改 `<title>`） |
| `src/main.jsx` | `src/main.jsx` |

之后写 `src/App.jsx`、`evidence.json`、`README.md`。

## 依赖安装

优先把依赖装在**原型目录的上一级**（如 `prototypes/node_modules`）由所有原型共享：
Node 的模块解析会向上逐级查找，Vite 也遵循该规则。单个原型约 260 MB，多个原型各装一份纯属浪费。

```bash
cd prototypes && npm install   # 在上级目录安装，各原型共用
```

上级目录记得 `.gitignore` 掉 `node_modules`。

内网 npm 镜像可能对 `@douyinfe/*` 返回 403。此时不要改用公网 registry 硬拉，先确认合规，
或从同级已装好的原型复用依赖目录。

## 模板已处理的三个坑

**Semi 的 CSS 路径进不了 `exports`。** `@douyinfe/semi-ui` 的 `exports` 字段只暴露 `.`、`./lib/es/*`、`./lib/cjs/*`，
文档给的 `@douyinfe/semi-ui/dist/css/semi.min.css` 无论用 JS import 还是 CSS `@import` 都解析失败。
模板从包入口反推包根目录再拼路径，依赖提到上级目录后依然有效。

**部分环境收不到文件系统事件**，dev server 不热更新且会持续提供旧代码，容易误判成代码没生效。
模板默认开 `server.watch.usePolling`。若仍怀疑是缓存，直接 `curl http://127.0.0.1:<port>/src/App.jsx` 看服务端返回的是不是最新代码，
别靠反复截图猜。

**端口被旧进程占用时 Vite 会静默换端口。** 启动后以日志里打印的实际地址为准，不要假设就是配置里那个。
