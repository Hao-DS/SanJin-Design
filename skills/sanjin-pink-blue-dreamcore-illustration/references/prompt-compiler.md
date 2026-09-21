# 提示词编译器

先锁定媒介，再写看得见的日常事实，最后写空气、色彩与材质。第一段必须声明这是 **fully rendered soft-airbrushed pastel digital illustration**，并明确排除 photography、architectural visualization 与 photorealistic 3D。不要用 “dreamcore、ethereal、cute、detailed、magical” 等空泛形容词替代可见规则。

## 静态生成模板

~~~text
Create an original, fully rendered soft-airbrushed pastel digital illustration of [一句可见场景]. This must unmistakably read as illustration: smooth painted color fields, softened structural edges, selective fine drawn detail, pearlescent color separation and luminous pastel bloom. It must not look like a photograph, architectural visualization, lifestyle advertisement, real-estate render or photorealistic 3D. Emotional register: [晨间苏醒/日常被照亮/私密成长/温柔独处/熟悉之地的异化/短暂停驻].

Format and composition: [2:3/3:2/4:3/1:1/指定比例], chosen because [人物留白、建筑高度、街景动线或静物结构理由]. Use an [平视/略低/安静近景] illustrated viewpoint, stable verticals, one clear focal subject, broad simple shapes and [明确留白位置]. Avoid camera, lens, depth-of-field and exposure language.

Dreamcore mechanism: use [熟悉的阈限空间 / 光学错位 / 空间错位 / 尺度错位 / 时间错位 / 语义模糊] as the single primary dream mechanism. Keep it non-threatening and built entirely from ordinary real-world elements. Add no more than one weak supporting optical phenomenon. The image should still feel like a half-remembered dream if pastel color, bubbles and iridescence are mentally removed.

Scene and daily anchor: [地点]. The emotional focal point is [人物/动物/房屋/静物/门口/转角/通道/光线停留处] and is [平静可读的状态或空间状态]. Explain the place with only [1–3 个生活残留]. Preserve recognizable silhouette, scale, gravity and contact, while allowing secondary objects to remain semantically ambiguous, as if partly omitted by memory. Simplify bricks, asphalt, wood grain, foliage, skin pores and interior merchandise into softly painted shapes.

Character styling, scaled by visual importance: above 30% of the frame, the clearly adult character uses one complete original couture-inspired silhouette, one construction motif, 2–3 materials, one makeup direction, one hair structure and no more than two hero accessories. At 15–30%, use only one silhouette feature, one construction detail and one makeup/accessory identifier. Below 15%, simplify clothing and make it subordinate to the environment. Use runway and haute-couture principles only as general design vocabulary; no brand logos, monograms, signature prints, recognizable luxury-product shapes or copied runway looks.

Global color integration: choose [strong powder-blue 75–90% / memory powder-blue 55–75% / liminal powder-blue 40–65%]. Use [雾青/浅天蓝/水蓝] with [浅粉/蜜桃/淡紫/奶油黄/薄荷] across multiple surfaces and shadows, not merely in the sky or reflections. Repaint nominal whites with pink-cyan light, foliage with mint and turquoise, pavement and shadows with blue-lilac, and brown materials with peach-rose; the memory and liminal tiers may retain small areas of faded cream, old mint and pale gray-violet as reality anchors. Keep near-black below 3%. Soft does not mean washed out. Preserve a clean cyan field, readable pastel-pink light, pearly spectral highlights and luminous warm skin; avoid gray haze, dirty whites, naturalistic photographic color and a single flat color wash.

Edge and dream material: introduce subtle cyan-magenta-lilac color separation along selected contour edges, hair strands, window frames and reflective objects. Use [transparent bubbles / pearlescent glass / subtle refracted steam / soft water reflections / luminous leaves] as at most one supporting anomaly, with thin translucent pink, yellow, mint and lilac reflections. Add [0–20] sparse points of light only near [主体或光源], never as dense glitter.

Lighting and finish: high-key diffused daylight, pale cyan-lilac shadows and peach-pink highlights, low-to-medium contrast, soft atmospheric depth, smooth airbrushed digital painting with restrained powdery texture and fine drawn detail only in [毛发/玻璃边缘/叶脉/织物/电线]. Keep edges luminous and slightly dissolved. No photographic microtexture, lens bokeh, natural camera exposure or harsh sharpening.

Avoid: photography, architectural photography, lifestyle photography, real-estate rendering, commercial café imagery, realistic lens effects, photorealistic 3D, realistic brick/asphalt/wood microtexture, large black areas, a normal photo with rainbow reflections added; recreating any supplied reference image or its specific people, houses, fruit arrangements, animals, streets, props or compositions; threatening liminal dread, dark empty rooms, infinite mazes, creepy dolls, glitch text, surveillance mood or weirdcore fear; cyberpunk neon, laser light, futuristic city styling; heavy oil paint, hard vector lines, anime cartooning, toy-like 3D, game-render gloss, HDR; opaque rainbow chrome, dense holographic film, excessive bubbles or sparkles; gray fog, dirty whites, fluorescent or gray skin, blown-out facial detail, random readable text, logos, watermarks.
~~~

## 图像转译补充

~~~text
Use the supplied image as the edit target. Preserve [人物、宠物、产品或建筑的身份] and [关键动作、造型、比例或用户指定特征]. Rebuild its lighting, surroundings and materials using the visual system above. Remove incidental clutter, existing typography, logos and contemporary background noise unless explicitly requested. Keep the result recognisably derived from the target subject, but do not reproduce the composition of any style reference.
~~~

## 风格参考补充

~~~text
Use the 2–3 attached style references as strong evidence for medium, whole-frame color coverage, luminous edge handling, pastel shadow color, simplified surface detail and airbrushed digital-illustration finish. They are style references, not edit targets. Match their degree of illustration and chromatic flooding before matching incidental scene detail. Do not copy their people, animals, fruit, cups, houses, street layouts, trees, clothing, props, text or compositions.
~~~

## 建筑与街景纠偏

建筑、咖啡店、街道和住宅最容易滑向摄影。为这类请求额外加入：

~~~text
Treat the building and street as softly painted pastel shapes, not as a photographed location. Simplify brick, asphalt, foliage and interior furnishings; let cyan, pink, lilac, peach and mint light permeate every surface and shadow. The façade may remain structurally recognizable, but the entire frame must have the same airbrushed illustrated color logic as the style references. No architectural photography, no real-estate visualization, no lifestyle café advertising, no natural camera color.
~~~

## 海报/文字请求补充

用户明确要求排版时才添加：

~~~text
Reserve [位置] as a clean, quiet typography zone. Do not invent copy. Add only the exact short text “[TEXT]” if the image system can render it reliably; otherwise leave the zone empty for a verified layout pass.
~~~

## 提示词复核

确认提示词包含：2–3 张已附加风格参考、开头的媒介锁定、反摄影/反建筑渲染声明、一句可见场景、一个情感、一个主梦核机制、比例及理由、插画视点、一个情绪焦点与留白、1–3 个生活残留、三档综合色强度之一、跨表面色相迁移、记忆模糊、至多一个主错位和一个弱辅助现象、柔光和空气喷绘表面、来源残留禁区。人物造型必须按 30% / 15–30% / 15% 以下分级，不得让背景人物抢走环境焦点。必须出现 “Soft does not mean washed out” 和 naturalistic photographic color 禁令。若仍出现 50–85 mm、bokeh、photorealistic、architectural photography、realistic brick texture 等摄影诱导词，删除或转写。

## 梦核不足纠偏

- **只像粉彩治愈插画**：先加入一个阈限状态、生活残留或温和逻辑错位，再考虑泡泡与虹彩。
- **空间完全正常**：让门、路径、时钟、水迹、季节或次要物件产生一次可见但不威胁的偏差。
- **异常太奇幻**：删除怪物、门户、魔法符号和多重悬浮物，把异常换成日常物的位置、尺度、时间或用途错位。
- **空场景变恐怖**：提高日光与可居住性，加入未收椅子、半开窗帘、杯子或水迹等生活残留，删除黑暗、无限和监控感。
