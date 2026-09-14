# 提示词编译器

先写事实，再写风格；先锁定空间，再补道具。不要用一串空泛形容词代替可见指令。

## 静态生成模板

```text
Create an original cinematic still about [一句可见故事], using a meticulously art-directed mid-century visual grammar without reproducing any existing film frame. Emotional engine: [失去与保存/秩序与混乱/破碎家庭与临时共同体/身份与自我表演/记忆与重述/时代终结]. Let formal order contain the emotion rather than showing it through melodrama.

Narrative frame: [无/章节页/档案条目/回忆转述/舞台中的舞台/并行小传]. Keep it legible at a glance and use at most one weak secondary frame.

Format and camera: [1.37:1/1.85:1/2.35:1/4:3/3:4/指定比例], chosen because [年代、队列、空间距离或叙事层级理由]. Fixed frontal eye-level camera, [perfect central axis / strict modular grid / balanced bilateral split], restrained perspective, clean full-frame geometry. Include one deliberate asymmetry only when it reveals imbalance or change.

Scene architecture: [地点与年代范围]. Build the space from [门/拱/楼梯/隔间/柜台/窗/地砖] arranged as [所选场景配方]. Keep [前景处理] uncluttered and preserve clear negative space.

Color zoning: high-luminance, high-saturation macaron blocks of [主色 1], [主色 2], [主色 3], separated by [亮奶油/暖象牙]. Chromatic surfaces cover roughly 60–85% of the frame; at least two contrasting color fields each occupy roughly 15–35% and collide clearly across walls, floors, furniture or costumes. Use [局部强调色] on [叙事锚点]. Colors distinguish [年代/空间/阵营/心理状态] and create strong visual impact. Muted does not mean gray or muddy. Preserve clearly separated pink, teal, mustard, blue and burgundy color blocks; avoid global desaturation, gray-brown wash and dirty skin tones.

Characters and blocking: [1–5 位角色的身份、位置、动作与视线]. Each person performs a believable function; calm deadpan expressions, emotion conveyed by distance, pauses, eye-lines and small hand actions. Character identity is encoded through [固定服装/制服/头衔/徽章/工具], not fashion posing.

Prop archive: [每个关键人物 1–2 件信件、钥匙、书、地图、行李、文具、照片、徽章或机械物]. Arrange, label, wear, omit or preserve them to reveal what the characters value or have lost; do not add generic decorative clutter.

Quiet absurdity or ritual: [无/一个轻微荒诞锚点/过时礼仪/执拗仪式], treated as ordinary. Do not add a second spectacle.

Lighting and finish: soft even warm-neutral light or bright diffused daylight, medium tonal contrast and high chromatic contrast, clean warm skin tones, matte painted wood and plaster, velvet/tiles/brass/paper/cloth as relevant, subtle vintage wear, visible handcrafted or miniature-set character, fine restrained film grain that does not desaturate the image, cinematic realism with a slightly theatrical set quality.

Avoid: copied film characters or compositions, copied reference props or wording, readable filler text, logos, watermarks, modern devices, trendy contemporary decor, symmetry-and-pastels with no narrative function, global desaturation, gray-brown wash, muddy neutrals, dirty gray skin tones, colors blending into one haze, color limited to tiny accents, dutch angle, extreme wide-angle distortion, dramatic chiaroscuro, neon colors, teal-orange blockbuster grading, glossy commercial styling, HDR, seamless plastic 3D render, dense clutter, exaggerated facial acting, random costumes, direct sentimental crying or advertising-style warmth.
```

## 图像转译补充

```text
Use the supplied image as the edit target. Preserve [人物/产品/建筑身份、关键动作、服装或其他约定特征] and [原始或指定比例]. Rebuild the environment and art direction in the visual system above. Remove incidental clutter, existing typography, logos and contemporary background cues unless explicitly requested. Keep the result recognisably derived from the target subject but not from any style-reference composition.
```

## 风格参考补充

```text
Use the attached style references only for abstract evidence: frontal geometry, controlled color zoning, soft flat light, period material mood and restrained character blocking. Do not copy their people, animals, props, text, room layouts, signs, wardrobe combinations or exact palettes.
```

## 海报/文字请求补充

只有用户明确要求排版时添加：

```text
Reserve [位置] as a clean typography zone. Do not invent copy. Add only the exact short text “[TEXT]” if the image system can render it reliably; otherwise leave the zone empty for a verified layout pass.
```

## 提示词复核

确认提示词包含：一句故事、情感发动机、可选叙事框架、比例及理由、机位、主结构、3–6 个高饱和马卡龙色及叙事功能、两块以上大面积撞色区域、60–85% 彩色覆盖、干净暖肤色、人物动作、服装身份、档案道具、0–1 个荒诞/仪式锚点、光线与手工材质、年代边界、来源残留禁区。必须出现“Muted does not mean gray or muddy”及全局降饱和禁令。删除“cinematic、whimsical、vintage、detailed”等无法单独指导构图的重复形容词。
