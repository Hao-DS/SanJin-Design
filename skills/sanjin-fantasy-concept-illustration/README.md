# SanJin-幻想概念插画

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>

将文字主题、照片、人物、动物、建筑、静物或产品转译为原创的半抽象表现主义幻想数字绘画：以钴蓝、群青和深靛建立整体世界，用电光青制造断裂跳光，让紫红、玫红和品红贯穿多个空间区域，再以珊瑚橙和金黄形成直接反冲。最终画面强调大色块、粗宽刷痕、破碎边缘、平面化空间和明显人工绘制痕迹，而不是完成度精致的写实 Concept Art、照片写实、平涂动漫或通用赛博朋克。

本技能不会复制参考图中的树、房屋、街道、人物、动物组合、静物排列、咖啡杯、云形或构图，也不会模仿某位特定艺术家的署名风格。它提取的是可跨题材复用的色彩、光线、笔触、构图和质量标准。

## 能做什么

- 根据主题生成原创幻想数字厚涂静态图。
- 将照片、人物、动物、建筑或产品重绘到该视觉系统，同时保留约定特征。
- 分析一组参考图，区分可见证据、固定规则、安全可变量与来源残留禁区。
- 只编写结构化生成提示词、负面约束与输出规格。
- 针对自然主体、幻想景观、建筑、湿街、人物、动物、静物和单件产品选择不同配方。
- 用质量门禁优先拦截“过度完成、过度自然、过度写实”，再检查色彩比例、洋红分布、粗笔触、空间压平、题材保真与原创性。

## 核心视觉原则

- 默认色彩校准接近：深蓝/群青 50%、青蓝/电光蓝 20%、紫色/洋红 15%、橙黄/珊瑚橙 15%。
- 洋红必须形成明确色块，并跨越天空/背景、主体暗部、地面/前景中的至少两个区域，不能只围绕夕阳。
- 深靛暗部托住高纯度亮部，避免灰褐罩染、浑浊黑位和全画面均匀泛光。
- 一个主光逻辑、一个强主轮廓、1–3 条主导宽笔势；允许少量非物理青色、洋红或橙色跳光。
- 全画幅先读出约 4–9 个大色块；单个树冠、云团、毛发或衣褶组优先控制在 3–5 个主色块。
- 相较常规精致 Concept Art，微观细节默认减少约 40–50%；以宽刷痕、拖拽破边和色面突变代替自然渐变与真实材质。
- 弱化自然空气透视和连续景深，使空间更平面、更装饰性；不依赖清晰线稿。
- 人物、动物、建筑和产品的身份结构必须可信，风格不能吞没解剖、透视和关键特征。
- 默认无文字、logo、水印或签名；默认 2:3 竖幅、长边至少 1536 px。

## 安装

将整个文件夹复制到 Codex skills 目录，并保持技术目录名不变：

```text
<CODEX_HOME>/skills/sanjin-fantasy-concept-illustration/
```

重启或刷新 Codex 后即可发现技能；界面名称显示为“SanJin-幻想概念插画”。

## 使用示例

```text
使用 $sanjin-fantasy-concept-illustration 生成一张 2:3 竖幅：荒原上一棵被风塑形的古树，天空占画面三分之二，蓝色统摄，青色边光，暖橙地表。
```

```text
使用 $sanjin-fantasy-concept-illustration 把这张人物照片重绘成炫彩幻想厚涂，保留面部身份、肤色、发型和耳饰，使用青蓝背光与暖色侧光。
```

```text
使用 $sanjin-fantasy-concept-illustration 分析这组参考图，只输出可见证据、固定规则、安全可变量、来源残留禁区和一份结构化提示词。
```

## 文件结构

```text
SKILL.md                              # 路由、默认规格、制作流程与关键禁区
agents/openai.yaml                    # Codex 界面元数据
references/
├── color-light-system.md             # 色彩面积、色板、光源与暗部逻辑
├── composition-brushwork.md          # 构图骨架、笔势、边缘与形体简化
├── scene-recipes.md                  # 八种跨题材画面配方
├── prompt-compiler.md                # 生成、转译、参考图与文字请求模板
├── quality-gate.md                   # 全画幅验收与失败修订
└── reference-index.md                # 八张用户参考图的证据索引
assets/style-references/              # 用户提供的八张视觉参考
scripts/export_still.py               # RGB JPG/PNG 导出与比例、尺寸检查
```

## 结构说明

目录组织、路由方式、渐进式参考文档和质量门禁参考了 `sanjin-wes-anderson-aesthetic` 的成熟结构；视觉系统、提示词、配方、禁区和验收标准均根据本项目的八张参考图重新提炼。

---

<a id="english"></a>

## English

Create original semi-abstract, high-saturation expressionist fantasy paintings from a brief, photo, person, animal, building, still life, or product. The system targets a roughly 50/20/15/15 balance of deep blue, electric cyan, magenta-violet and warm coral-orange; it uses flattened decorative space, large simplified masses, coarse directional strokes, broken nonphysical highlights and substantially reduced microdetail. The goal is visibly painted chromatic expression—not polished realistic game concept art.

It does not copy subjects, poses, props, cloud silhouettes, layouts, or framing from the supplied references, and it does not imitate a named artist's signature style.

### Installation

Copy the complete folder to:

```text
<CODEX_HOME>/skills/sanjin-fantasy-concept-illustration/
```

Restart or refresh Codex, then invoke `$sanjin-fantasy-concept-illustration`.

### Example

```text
Use $sanjin-fantasy-concept-illustration to create an original 2:3 fantasy landscape dominated by cobalt and ultramarine, with deep-indigo shadows, electric-cyan rim light, and a restrained warm-orange horizon.
```
