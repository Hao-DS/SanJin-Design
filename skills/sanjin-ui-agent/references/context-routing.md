# 按阶段加载上下文

先按 pipeline.md 选择快速或标准模式。两种模式均先完成 Figma 静态设计与人工确认，再加载实现资料。

| 阶段 | 必读 | 按需 |
| --- | --- | --- |
| 设计理解 | pipeline.md；快速模式读 fast-mode.md，标准模式读对应 design-spec 模板 | 现有界面读 design-evidence-gate.md；截图读 screenshot-to-prototype.md |
| Figma 静态设计 | figma:figma-use、figma:figma-generate-design、DESIGN.md、visual-quality.md、console-craft.md | 新文件读 figma:figma-create-new-file；布局和状态读 ui-judgment/；数据、AI、权限、图表读对应领域参考 |
| 人工评审 | pipeline.md 的确认和回退规则 | 用户反馈涉及的局部设计参考 |
| 交互实现 | prototype-delivery.md、mcp-evidence-protocol.md、mock-data-realism.md、full-output.md | Semi 读 scaffold/；AI 对话读 companions/ant-design-x/；图表读 companions/vchart/ |
| 正式交付 | 对应 handoff 模板 | 规范沉淀读 design-md-workflow.md |

Figma 阶段不读取组件代码 API，不建 React 工程，不运行浏览器交互验证。实现阶段先读已确认 Frame 和状态记录，只补充当前问题需要的参考。
