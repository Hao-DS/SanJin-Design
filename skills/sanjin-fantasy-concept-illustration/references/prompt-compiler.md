# 提示词编译器

先写可见事实，再写风格系统；先锁定主轮廓和光源，再补笔触与细节。避免连续堆叠同义形容词。

## 静态生成模板

```text
Create an original still illustration of [主体、环境与动作]. The single visual verb is [生长/升腾/穿行/凝视/聚拢/迸发/静置/逼近]. Keep one unmistakable focal subject and a clear silhouette; do not reproduce any supplied reference composition or subject arrangement.

Format and composition: [2:3/3:2/16:9/1:1/指定比例], chosen because [理由]. Use the [单一图腾/低地平线大天空/纵深通道/前景压暗框景/近景静物舞台/低机位英雄视角] structure. Organize the full frame into roughly 4–9 large readable color masses. Keep [前景] / [中景] / [远景] identifiable through overlap and color separation, but flatten natural depth and reduce realistic atmospheric perspective. Main directional flow: [斜向上冲/弧形包裹/水平延展/纵向升腾/向心聚拢].

Color hierarchy: target roughly 50% deep blue / cobalt / ultramarine / indigo, 20% cyan / electric blue, 15% violet / magenta / rose, and 15% orange-yellow / coral orange. Use deep indigo and blue-black instead of neutral black, gray or brown in shadows. Magenta must form clearly visible masses across at least two of these zones: sky/background, subject shadows, ground/foreground; do not confine pink to the sunset or a tiny accent. Preserve broad dark masses so electric cyan and warm highlights can jump abruptly.

Lighting: [高位天光/逆光地平线/街道湿光/物体内发光/侧逆光肖像] from [方向]. Keep the main light readable, but use stepped color planes and broken highlight shapes instead of natural gradients. Add 1–3 deliberately nonphysical cyan, magenta or orange light accents on selected edges or shadow planes. Reserve near-white for a few peak highlights; never outline the whole subject evenly.

Painterly construction: semi-abstract, high-saturation expressionist digital painting—not polished or realistic concept art. Build the image from simplified color masses, broad swept strokes, dragged broken edges and visible impasto-like digital brush marks. Use huge elongated strokes and 3–7 abstract blocks for skies/backgrounds; use medium-to-large strokes for the subject and ground; use smaller controlled strokes only at [脸/眼睛/手/产品结构/叙事物]. Reduce normal concept-art microdetail by roughly 40–50%. Tree crowns, cloud groups, fur masses, hair groups and drapery groups should each resolve into about 3–5 primary color blocks rather than individual leaves, hairs, fibers or droplets. Mix sharp broken light cuts with lost shadow edges. Keep deliberate artificial brush traces and decorative flatness.

Subject integrity: preserve recognizable [人物身份与肤色/动物解剖与物种特征/建筑透视主线/产品轮廓与接口]. Let the style simplify material, texture, depth and lighting aggressively without destroying identity.

Avoid: copied reference subjects, poses, landmarks, prop combinations, cloud shapes or framing; imitation of a named artist; polished epic game concept art; cinematic realism; realistic cloud rendering; detailed bark, individual leaves, single hair strands, dense pebbles, grass blades, cracks or material microtexture; natural smooth gradients; realistic atmospheric perspective; physically complete lighting; cyberpunk technology by default; readable signs, random text, logos, watermarks or signatures; flat anime cel shading, clean comic line art, generic vaporwave gradients, uniform neon glow, neutral gray or brown shadows, muddy blacks, teal-orange blockbuster grading, photorealism, plastic 3D, game-render surfaces, HDR, over-sharpening, equal detail everywhere, chaotic small brush marks, anatomy errors, malformed hands, melted architecture, and accidental extra objects.
```

## 图像转译补充

```text
Use the supplied image as the edit target. Preserve [身份、轮廓、姿势、关键服装、产品特征、建筑结构] and [原始或指定比例]. Repaint the scene through the color, light and brushwork system above. As a first pass, remove roughly 40–50% of microtexture, merge natural gradients into broad color planes, and replace realistic background forms with large directional brush marks. Remove incidental clutter, existing typography, logos and unrelated background cues unless explicitly requested. Do not borrow any style-reference composition.
```

## 风格参考补充

```text
Use the attached style references only as abstract evidence for cobalt/ultramarine dominance, magenta distributed across multiple zones, deep-indigo shadows, electric-cyan broken highlights, warm-orange counter-masses, flattened decorative space, simplified color blocks, coarse directional strokes and reduced microdetail. Do not copy their trees, buildings, streets, people, animals, still-life arrangements, cups, cloud silhouettes, poses or framing.
```

## 文字请求补充

只有用户明确要求时加入：

```text
Reserve [位置] as a calm typography zone. Do not invent copy. Render only the exact short text “[TEXT]” if reliable; otherwise leave the zone empty for a verified layout pass.
```

## 复核清单

提示词必须包含：内容事实、单一视觉动词、比例与构图理由、主轮廓、4–9 个全画幅大色块、平面化空间、主导宽笔势、50/20/15/15 色彩校准、跨区域洋红分布、深靛暗部、断裂电光跳亮、允许的非物理光、40–50% 微细节削减、3–5 色块式自然形体、题材保真项、原创性边界和“非精致 Concept Art”排除项。删除没有独立决策作用的重复词。
