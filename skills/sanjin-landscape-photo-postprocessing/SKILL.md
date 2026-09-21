---
name: sanjin-landscape-photo-postprocessing
description: |
  当用户提供风光照片并要求分析、制定或直接执行后期修图时调用，包括风格诊断、构图优化、通透排障、影调、调色、局部光影、空间立体与质感、降噪锐化、合成决策，以及把方案转成生图/图像编辑模型指令。方法论来自《风光摄影后期基础》。不适用于无原图的纯文生图、人物精修，或把生成式重构冒充纪实摄影。Triggers: 风光修图/调色/通透/影调/局部光影/landscape retouch/color grading/photo edit.
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.landscape-photo-postprocessing
  cangjie.capability-count: 10
  cangjie.entrypoint-count: 1
---
# 《风光摄影后期基础》 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 无原图、只要求从零生成风景画或摄影作品
- 人像皮肤、商业产品、建筑室内等非风光精修
- 伪造新闻、纪实或比赛允许范围之外的内容
- 将2018年Adobe界面路径或案例参数当作当前软件的固定处方

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 技术服务形式，形式服务内容；先定主题、主体和情绪，再选工具。
2. 后期以局部处理为核心：先统一整体，再制造有目的的局部变化。
3. 通透需分别诊断发闷与发灰，不能等同于全图清晰、去雾或增艳。
4. 配色模型必须服从自然性，主体通过相对明度和饱和度突出。
5. 空间、立体与质感必须遵守既有遮挡、光源、投影和真实纹理。
6. 生成式编辑必须声明尺度和不可改项，并逐步验收结构保真。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 诊断风光照片；制定后期方向；选择修图风格 | references/capabilities/intent-diagnosis.md | references/capabilities/authenticity-boundary.md、references/capabilities/composition-guidance.md |
| 判断修图尺度；规划生成式修改；评估合成真实性 | references/capabilities/authenticity-boundary.md | references/capabilities/intent-diagnosis.md、references/capabilities/compositing-decision.md |
| 突出主体；优化构图；清理画面干扰 | references/capabilities/composition-guidance.md | references/capabilities/intent-diagnosis.md、references/capabilities/local-unity-variation.md、references/capabilities/depth-volume-texture.md |
| 局部调光调色；蒙版编辑；修复过渡生硬 | references/capabilities/local-unity-variation.md | references/capabilities/intent-diagnosis.md、references/capabilities/composition-guidance.md、references/capabilities/clarity-diagnosis.md、references/capabilities/natural-color-design.md |
| 让照片通透；修复发灰发闷；局部去雾 | references/capabilities/clarity-diagnosis.md | references/capabilities/histogram-tonality.md、references/capabilities/natural-color-design.md、references/capabilities/local-unity-variation.md |
| 调整影调；保住高光阴影；制作暗调亮调 | references/capabilities/histogram-tonality.md | references/capabilities/clarity-diagnosis.md、references/capabilities/local-unity-variation.md |
| 风光调色；统一色彩；设计冷暖或互补色 | references/capabilities/natural-color-design.md | references/capabilities/intent-diagnosis.md、references/capabilities/clarity-diagnosis.md、references/capabilities/local-unity-variation.md |
| 增强空间层次；塑造立体感；增强材质质感 | references/capabilities/depth-volume-texture.md | references/capabilities/composition-guidance.md、references/capabilities/local-unity-variation.md、references/capabilities/technical-finish.md |
| 风光精修收尾；降噪锐化；修复色彩断层 | references/capabilities/technical-finish.md | references/capabilities/depth-volume-texture.md、references/capabilities/local-unity-variation.md |
| 选择风光合成方法；融合多张素材；判断HDR接片流程 | references/capabilities/compositing-decision.md | references/capabilities/authenticity-boundary.md、references/capabilities/technical-finish.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 没有可读取的原图，无法进行图像诊断或编辑时，先请求图片
- 用户没有说明纪实/创意边界且请求新增、替换或大幅改变场景时，先确认尺度
- 严格摄影保真模式下，一次模型编辑即出现地貌、建筑、云层或物体结构漂移时，停止生成并交付可控蒙版/传统编辑方案
