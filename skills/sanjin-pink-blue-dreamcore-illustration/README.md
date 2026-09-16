# SanJin-粉蓝梦核插画

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>

将文字主题、照片、人物、产品或建筑转译为原创的粉蓝梦核数字插画：用柔雾空气喷绘、水青—粉紫综合色、珍珠边缘分色、稀疏细闪与被简化的日常细节，让一个寻常片刻像刚从梦里醒来。它不是把粉蓝滤镜、彩虹油膜或泡泡特效盖在照片上；整张画面都必须被插画化重绘，一眼不能像建筑摄影、生活方式广告或写实 3D。

本技能不会复刻任何参考图，也不会复制其中的具体人物、动物、房屋、果物、器皿、街道、文字、道具组合或画面布局。它使用可复用的视觉语法完成新的主题与场景。

## 能做什么

- 根据主题、物件或情绪生成原创的粉蓝梦核插画。
- 将照片、人物、宠物、产品、静物或建筑转译到该视觉系统，同时保留约定特征。
- 分析参考图，输出固定规则、安全可变量与来源残留禁区。
- 只编写可复用提示词、负面约束和输出规格。
- 用肖像漂浮、清空的社区街景、晨光房屋、折光静物、窗边生命体或杯中蒸汽等配方组织画面。
- 通过质量门禁检查空气、色温、透明材质、留白、日常锚点、异常克制与文字污染。
- 自动从八张内置视觉参考中选取并实际附加 2–3 张，稳定媒介、综合色域与边缘处理。

## 核心视觉原则

- 媒介首先是柔雾空气喷绘式数字插画：平滑综合色域、软化结构边缘、局部细线和珍珠分色并存；照片感、建筑可视化与商业空间渲染直接判失败。
- 水青、粉蓝、淡紫、蜜桃、奶油黄和薄荷色覆盖约 75–90% 画面，并进入墙面、路面、植物、肤色、白色物体和阴影，而不是只出现在水坑或玻璃反光中。
- 默认是 2:3 竖幅：它能同时保留主体与大面积清澈留白。画幅必须服务主体，用户指定优先。
- 画面保持高调、低到中等反差；冷蓝阴影与蜜桃暖光同时可读，白色物体和面部保留细节。
- 玻璃、肥皂泡、水、蒸汽、露水、瓷釉与叶片可出现薄而透的粉、黄、青、紫折射，不能变成厚重油膜、铬金属或塑料。
- 一个可信日常锚点（窗、屋檐、衬衣、杯子、植物、果物或电线）先建立现实感；0–2 个梦境现象只负责轻微偏移感受。
- 构图自然、安静、可呼吸：一个明确焦点，大面积留白，平视或略低的稳定视点，避免极端广角与摆拍。
- 插画表面是细腻的空气喷绘写实，柔化但不失去剪影；砖缝、柏油、木纹、叶片、皮肤毛孔和室内陈设应被适度简化。可有稀疏星点，禁止真实镜头纹理、密集闪粉、HDR、游戏 3D、硬边矢量和商业棚拍质感。
- “Soft does not mean washed out”：必须保留清澈青空、可辨粉光、珍珠高光和暖净肤色，避免灰雾、脏白、平淡蒙版与荧光肤色。

## 安装

将整个文件夹复制到 Codex skills 目录，保持技术目录名不变：

~~~text
<CODEX_HOME>/skills/sanjin-pink-blue-dreamcore-illustration/
~~~

重启或刷新 Codex 后即可发现该技能。界面名称显示为“SanJin-粉蓝梦核插画”。

## 使用示例

~~~text
使用 $sanjin-pink-blue-dreamcore-illustration 生成一张 2:3 原创插画：清晨，一个男孩坐在河边的石阶上给透明水壶加水，河面映出淡粉和奶油黄的光，远处是安静的水青色住宅街。
~~~

~~~text
使用 $sanjin-pink-blue-dreamcore-illustration 将这张猫咪照片转成粉蓝梦核插画。保留猫的花色、坐姿和红色项圈；把背景变为有大窗与几盆植物的安静房间，窗光在玻璃水杯上形成少量珍珠反射。
~~~

~~~text
使用 $sanjin-pink-blue-dreamcore-illustration 分析这组参考图，只输出视觉规则、安全可变量、来源残留禁区和一份结构化生成提示词。
~~~

## 文件结构

~~~text
SKILL.md                              # 主流程、路由、默认规格与关键禁区
README.md                             # 技能说明、安装方法与示例
agents/openai.yaml                    # Codex 界面元数据
references/
├── visual-system.md                  # 固定视觉规则、色板、材质与构图
├── narrative-system.md               # 梦境情感、日常锚点与异常控制
├── scene-recipes.md                  # 六种场景配方
├── prompt-compiler.md                # 生成、转译与文字请求的提示词结构
├── quality-gate.md                   # 交付验收和常见失败修订
└── reference-index.md                # 八张用户参考图的证据索引
assets/style-references/              # 用户提供的八张视觉参考
scripts/export_still.py               # RGB JPG/PNG 导出与比例、尺寸检查
~~~

## 结构来源

目录和渐进式信息披露方式参考 SanJin-维斯.安德森美学；本技能的视觉系统、情感逻辑、提示词、质量标准、视觉索引与脚本均依据当前用户提供的粉蓝梦核参考图重新编写。

---

<a id="english"></a>

## English

Create original powder-blue dreamcore digital illustrations from a brief, photo, person, product, object, or building. The system uses a soft-airbrushed pastel medium, whole-frame cyan-pink-lilac color flooding, pearlescent edge separation, simplified everyday detail, high-key diffused light, and sparse sparkles. The result must read as illustration—not photography, architectural visualization, a lifestyle advertisement, or photorealistic 3D.

It does not recreate the supplied references or copy their people, animals, houses, fruit, glassware, streets, text, props, or compositions.

### Installation

Copy the complete folder to:

~~~text
<CODEX_HOME>/skills/sanjin-pink-blue-dreamcore-illustration/
~~~

Restart or refresh Codex, then invoke it with $sanjin-pink-blue-dreamcore-illustration.

### Example

~~~text
Use $sanjin-pink-blue-dreamcore-illustration to create an original 2:3 illustration of an ordinary neighborhood greenhouse after rain, with one watering can, a cyan morning atmosphere, and faint pearly reflections in the wet window glass.
~~~
