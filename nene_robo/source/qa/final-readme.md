# 宁宁机器人 · 原始造型

- 宠物 ID：`nene-robo`。
- 造型：官方原始ネネロボ／Robo-Nene，黄裙与青绿马甲的演出服。
- 画风：用户确认的“贴近游戏原画”；清晰轮廓、赛璐璐阴影、原始大头短身机器人比例。
- 交付：完整可导入 Codex 桌面宠物、9 种动画及 16 个注视方向、动画预览。此轮只制作和打包。

## 制作进度

- [x] 确定造型、画风、交付目标并复核本机规格。
- [x] 制作并检查角色基准图：`source/references/canonical-base.png`。
- [x] 制作与检查9种动画及16个注视方向。
- [x] 验收并打包：本套本地交付版本1.0.0。

## 参考与设计

1. [日文官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)与[英文官方资料](https://www.colorfulstage.com/characters/wonderlands-showtime/nene/index.html?year=past)：宁宁操作机器人代为登台。安静、认真和略带吐槽感来自宁宁的设定。
2. [游戏剧情截图整理](https://game-question.com/qa/project_sekai/1347c27f-3404-473b-a2b9-3167a065d192)：`source/references/game-story-robo.jpg` 核对原始机器人头脸、紫色圆眼、灰绿机械发束、粉色领结与蝶形头饰。
3. [官方商品包装照片（第三方卖家）](https://www.ebay.com/itm/405696609821)：`source/references/official-figure-box-art.jpg` 中的包装插画核对全身原始服装、比例、裙摆及鞋子。商品摄影背景、文字、材质和底座不进入生成素材。
4. [游戏一格漫画整理](https://gameo.jp/pjsekai/494)：`game-comic-40.png` 核对惊讶表情与机器人设定。`game-comic-38.png` 是不相关检索对照，排除生成输入。

排除的其他参考：当前官网 `card_2.png.webp` 实为其他时期卡图，与本套无关；`game-robo-object.png` 是另一时期游戏摆件服装；`official-figure-packaging.jpg` 有明显包装反光，仅作辅助对照。已下载文件均保留。

关键外观：宽大灰绿头部、斜刘海、低扎粗发束与粉色发圈、绿色发箍、角色左侧（画面右侧）浅绿粉边蝶形头饰、紫色圆眼和脸部面板接缝；青绿马甲与黄色纽扣、粉色条纹领结、浅黄和奶白分片裙摆、短腿和深青绿圆鞋。裙侧紫色球饰通过实心短杆连接，不绘制悬浮装饰。

动作是创作演绎：安静眨眼、小步机械行走、拘谨招手、短促弹跳、故障时低头停顿、等待时举手询问、工作时认真运算、检查时转头审视。不将这些动画宣称为游戏原动画。

## 目标规格与来源

2026-10-13 再次只读核对本机 `OpenAI.Codex_26.1007.2314.0_x64__2p2nqsd0c76g0` 的 `app/resources/app.asar`：渲染与本地图片加载代码仍接受 v2，图集 1536 × 2288、8 列 × 11 行、单格 192 × 208。代码摘录与 SHA-256 保存在 `source/references/app-contract-verification.json`。

| 行 | 用途 | 使用帧数 |
| --- | --- | --- |
| 0–8 | idle、running-right、running-left、waving、jumping、failed、waiting、running、review | 6、8、8、4、5、8、6、6、6 |
| 9–10 | 顺时针注视方向，以向上为 0°，每次 22.5° | 各 8 |

输出无损 RGBA WebP；`pet.json` 指定 `spriteVersionNumber: 2` 和 `spritesheetPath: spritesheet.webp`。备用中性格沿用 hatch-pet 组装合同，其余未使用格完全透明。实际支持通过应用代码核对；不采用 ChatGPT Work Pets 的上传规格。

安装方式：将本套 `pet.json` 与 `spritesheet.webp` 同时复制到 `CODEX_HOME/pets/nene-robo/`（默认 `~/.codex/pets/nene-robo/`），在设置 > Pets 中刷新并选择。此轮尚未执行安装、应用界面识别或浮动显示验证。

## 文件与验收

制作资料位于 `source/`，参考图在 `source/references/`，预览位于 `preview/`，最终导入文件位于本目录顶层。最终路径与实际验收结果如下。

## 最终交付与实际验收

- 安装文件：本目录的 `pet.json`、`spritesheet.webp`。
- 本地ZIP：`../release-assets/nene-robo-v1.0.0/nene-robo-v1.0.0.zip`，内含 `nene-robo/`，附完整GIF预览和说明。SHA-256见同目录 `SHA256SUMS.txt`。本套尚未发布GitHub Release。
- 预览：`preview/animation-overview.gif`、9个状态GIF、`preview/look-directions.gif`、两张静态检查表。
- 提示词与来源：`source/imagegen-jobs.json` 指向 `source/prompts/` 的正式及修复提示词。全部图像经内置imagegen生成或整行编辑，原图与候选均保留于 `source/decoded/`。

验收：无损RGBA WebP为1536×2288、8×11格；必需帧完整、边界合格、透明隐藏RGB残留为0，图集校验无错误或警告。只执行一次全图边缘清理，alpha逐像素保持不变。九种动画与完整16方向经独立视觉复核通过；三项隔离盲测的四正方向均通过严格多数判定。最终GIF全部帧解码、尺寸/帧数/时长、ZIP内容与校验和已核对。

接受的细微警告：157.5°/202.5°的水平轴、067.5°/112.5°的垂直轴在孤立盲测中较模糊；45°/315°与相邻方向差别较细。337.5°回到0°时头部回正幅度稍大，完整循环复核确认身体、脚、服装锚点与尺度稳定，无显著跳变。裙侧球饰和短杆的负空间为原有造型空隙，未见裙装裂缝。详见 `source/qa/direction-semantics.json`、`blind-review-resolution.json` 与 `final-visual-qa.json`。

还对交付文件重放了本机安装包的实际图片/版本及路径验证函数，v2接受、v1拒绝，见 `preview/app-loader-validation.json`。从仓库根目录运行 `node nene-robo/source/qa/verify-package-loader.mjs` 可复核（需要相同Windows应用版本及路径）。这是工作区文件的加载算法检查。本套尚未安装到用户宠物目录，应用界面识别、选用和浮动显示未验证。
