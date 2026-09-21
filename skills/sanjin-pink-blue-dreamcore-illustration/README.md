# SanJin-粉蓝梦核插画

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>

将文字主题、照片、人物、产品或建筑转译为原创的粉蓝梦核数字插画：先以熟悉的阈限空间、醒后记忆般的局部模糊、一次温和的日常逻辑错位和有情绪的生活残留建立梦核骨架，再叠加柔雾空气喷绘、水青—粉紫综合色、珍珠边缘分色与被简化的日常细节。它不是把粉蓝滤镜、彩虹油膜或泡泡特效盖在普通场景上；整张画面必须同时一眼读作“梦核”和“插画”。

本技能不会复刻任何参考图，也不会复制其中的具体人物、动物、房屋、果物、器皿、街道、文字、道具组合或画面布局。它使用可复用的视觉语法完成新的主题与场景。

## 能做什么

- 根据主题、物件或情绪生成原创的粉蓝梦核插画。
- 将照片、人物、宠物、产品、静物或建筑转译到该视觉系统，同时保留约定特征。
- 分析参考图，输出固定规则、安全可变量与来源残留禁区。
- 只编写可复用提示词、负面约束和输出规格。
- 用肖像漂浮、社区街景、晨光房屋、折光静物、窗边生命体、杯中蒸汽、校园阈限空间或熟悉之地错位等配方组织画面。
- 通过梦核身份、插画媒介和参考使用三项硬门禁，检查阈限感、记忆模糊、逻辑错位、综合色彩、人物层级与文字污染。
- 自动从九张内置视觉参考中选取并实际附加 2–3 张，稳定媒介、综合色域与边缘处理；阈限空间和逻辑错位由原创场景规则控制。
- 前景人物使用原创高定妆造；中景与背景人物按占比分级简化，避免服装压过空间情绪。

## 核心视觉原则

- 媒介首先是柔雾空气喷绘式数字插画：平滑综合色域、软化结构边缘、局部细线和珍珠分色并存；照片感、建筑可视化与商业空间渲染直接判失败。
- 先保证去掉粉蓝、泡泡与虹彩后，画面仍通过阈限空间、记忆模糊、温和错位或生活残留呈现梦感；否则它只是粉彩治愈插画。
- 色彩按三档控制：人物与虹彩静物使用强粉蓝 75–90%，怀旧日常使用记忆粉蓝 55–75%，走廊、楼梯和候车区使用阈限粉蓝 40–65%。综合色必须进入多个表面与阴影，而不是只出现在水坑或玻璃反光中。
- 默认是 2:3 竖幅：它能同时保留主体与大面积清澈留白。画幅必须服务主体，用户指定优先。
- 画面保持高调、低到中等反差；冷蓝阴影与蜜桃暖光同时可读，白色物体和面部保留细节。
- 玻璃、肥皂泡、水、蒸汽、露水、瓷釉与叶片可出现薄而透的粉、黄、青、紫折射，不能变成厚重油膜、铬金属或塑料。
- 先用 1–3 个生活残留建立现实感，再从光学、空间、尺度、时间或语义错位中选择一个主梦核机制；必要时只增加一个弱辅助现象。
- 构图自然、安静、可呼吸：一个情绪焦点、大面积留白、平视或略低的稳定视点。焦点既可以是人物与物件，也可以是一扇门、一个转角或一段没有抵达点的通道。
- 人物超过画面 30% 时使用完整原创高定系统；占比 15–30% 时只保留一个廓形特征、一个结构细节和一个妆发/配饰识别点；低于 15% 时服装服从环境。
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
├── narrative-system.md               # 梦境情感、阈限状态与五类错位机制
├── scene-recipes.md                  # 八种场景配方
├── prompt-compiler.md                # 生成、转译与文字请求的提示词结构
├── quality-gate.md                   # 交付验收和常见失败修订
├── character-fashion-system.md       # 按人物占比分级的原创高定妆造
└── reference-index.md                # 九张用户参考图的证据索引
assets/style-references/              # 用户提供的九张视觉参考
scripts/export_still.py               # RGB JPG/PNG 导出与比例、尺寸检查
~~~

## 结构来源

目录和渐进式信息披露方式参考 SanJin-维斯.安德森美学；本技能的视觉系统、情感逻辑、提示词、质量标准、视觉索引与脚本均依据当前用户提供的粉蓝梦核参考图重新编写。

---

<a id="english"></a>

## English

Create original powder-blue dreamcore digital illustrations from a brief, photo, person, product, object, or building. The system first establishes a dreamcore backbone through familiar liminal space, partial memory ambiguity, one gentle everyday logic displacement, and emotional traces of ordinary life. It then applies a soft-airbrushed pastel medium, tiered cyan-pink-lilac color integration, pearlescent edge separation, simplified detail, and high-key diffused light. The result must read as both dreamcore and illustration—not merely a pastel healing image, photography, architectural visualization, a lifestyle advertisement, or photorealistic 3D.

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
