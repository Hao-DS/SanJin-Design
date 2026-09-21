# 提示词编译器

先写可见事实，再写构图、光色、媒介和细节层级。不要用 “healing、anime、cinematic、masterpiece、8K” 等标签代替视觉规则；也不要机械堆叠长串传统负面词。

## 静态生成模板

~~~text
Create an original hand-painted summer animation illustration of [一句可见场景]. The image must read as painterly digital illustration rather than photography, cel animation, glossy commercial art or 3D rendering. Emotional register: [quiet happiness / nostalgic youth / gentle solitude / fresh morning / warm everyday pause].

Format and composition: [2:3 / 3:2 / 16:9 / 4:5 / 1:1 / 指定比例], chosen because [人物纵向、街道动线、建筑框景、景观开阔或静物结构理由]. Use [low-angle / slightly low / eye-level] perspective. Place one clear focal subject [三分线或偏中心位置], with [前景], [中景] and [远景]. Keep [位置] as breathable negative space. For outdoor scenes, let clear sky or luminous air occupy about [35–65%] when appropriate; do not fill it with decorative clutter.

Subject and daily action: [主体、身份与可见特征] is [自然、可读的动作]. Preserve believable anatomy, scale, gravity, contact and functional structure. Use only [1–4 个] supporting details to establish place and daily life. If people appear, use natural human proportions, restrained semi-realistic animation features, understated eyes, painterly skin and simplified clothing folds; no chibi or fashion-ad posing.

Color system: a high-key, moderately saturated palette led by clear cyan/azure/turquoise air, fresh yellow-green and emerald foliage or accents, and warm cream/lemon-gold sunlight. Use peach, coral or pale lavender only as small reflected accents. Replace neutral gray or black shadows with cool cyan-green, blue-violet or deep teal. Keep near-black minimal. High-key must retain clean color separation; no gray haze, muddy greens or global white wash.

Lighting: one clear morning or afternoon summer-light direction, with warm golden direct light and cool cyan ambient shadows visible at the same time. Add [rim light / dappled leaf light / sunlit edges] where physically plausible, plus restrained luminous highlights, subtle bloom and light atmospheric haze. Preserve facial, cloud, wall and object structure inside bright areas.

Paint and detail: hand-painted animation-background aesthetic, gouache-like opaque digital brushwork, layered color blocks, visible directional brush texture and slightly imperfect handmade edges. Build foliage, clouds, terrain, hair and cloth from large shapes to medium clusters to a few bright broken strokes. Keep the focal silhouette clear and selectively detailed; simplify middle distance and soften far edges with atmospheric perspective. No photographic microtexture or perfectly smooth digital gradients.

Mood and originality: peaceful summer day, gentle breeze, fresh air, quiet everyday warmth and light nostalgia. Use the attached references only for abstract evidence of medium, light-color relationships, brush scale, edge hierarchy, airy depth and mood. They are style references, not edit targets. Do not copy their people, faces, outfits, animals, trees, houses, streets, props, clouds, text or compositions.

Avoid outcomes that look photorealistic, architectural visualization, lifestyle advertising, CGI, game concept art, glossy commercial illustration, hard cel shading, cute big-eyed anime, dark cinematic grading, cyberpunk neon, gray-brown atmosphere, deep black shadows, heavy HDR, over-sharpening, excessive bloom, dense film grain, hyper-detailed foliage/brick/skin/fur, equally sharp backgrounds, random readable text, logos, watermarks or signatures.
~~~

## 图像转译补充

~~~text
Use Image 1 as the edit target. Preserve [人物/动物/产品/建筑的身份] and [关键动作、轮廓、比例、服装或结构]. Repaint the entire frame using the visual system above. Keep unedited identity features stable, while removing incidental clutter, existing typography and unrelated brands unless explicitly requested. Images 2–4 are style references only; do not copy their content or composition into Image 1.
~~~

## 风格参考补充

~~~text
Use the 2–3 attached style references as strong evidence for high-key cyan–yellow-green–warm-cream color relationships, warm direct light with cool cyan ambient shadow, gouache-like opaque brushwork, selective detail, softened distance and quiet summer atmosphere. Match these abstract visual relationships before incidental scene detail. Do not reproduce any reference subject, identity, location, prop arrangement, animal grouping, tree silhouette, cloud shape or camera composition.
~~~

## 常见题材纠偏

- **建筑/街景像照片**：要求整帧成为 hand-painted animation-background illustration；合并砖、柏油、玻璃和树叶微纹理，用色块与叶影取代摄影细节。
- **人物像萌系二次元**：重申 natural human proportions、restrained eyes、painterly skin、adult identity 和 relaxed daily action；删除 kawaii、cute、glossy anime skin。
- **景观像精致游戏原画**：降低史诗尺度和材质完成度，扩大安静天空/空气，把微细节集中在焦点，删除 epic、concept art、ultra detailed、cinematic masterpiece。
- **画面只有蓝绿滤镜**：让暖黄直射光、青色环境影和桃粉/淡紫反光分别落在可见表面，不用单一蒙版覆盖整帧。

## 提示词复核

确认提示词包含：2–3 张实际附加的参考、可见场景与自然动作、比例及理由、焦点/前中后景/留白、青蓝—黄绿—暖黄颜色关系、暖直射光与青色环境影、水粉不透明笔触、由实到虚的细节、安静日常情绪、来源残留禁区和必要排除项。若出现与目标冲突的 photorealistic、ultra detailed、hard cel shading、epic concept art、dark cinematic lighting 或 perfectly smooth digital painting，删除或重写。
