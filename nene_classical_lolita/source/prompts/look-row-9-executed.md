Create one horizontal look-direction strip for Codex pet `nene_classical_lolita`, atlas row 9.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip is authoritative for the up, screen-right, down, and screen-left pose families. Interpolate the intermediate directions as even 22.5-degree steps between those anchors.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-right means the viewer's right image edge, never the character's own right. The row should travel naturally through the right half of the loop. Near-vertical 022.5 and 157.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

# 注视机制

人物为草薙宁宁，使用原基准图的动漫眼型；眼睛与眼睑先参与，头颈以克制的偏航和俯仰跟随，王冠随头保持固定连接。不能只移动瞳孔，不能扭曲整张图、倾斜全身或替换眼睛。

## 稳定基准

- 双脚、髋部、短裙下缘和双手基本锚定；黑色连裤袜腿部与鞋底保持同一尺度、基线及位置。
- 玫瑰始终在人物右手，红心牌在左手；道具随手臂轻微跟随，与身体的遮挡逐步变化，不换手、不突然侧翻。
- 头与王冠偏航不超过约25度；俯仰不超过约15度。每22.5度相邻步长的视觉变化尽量均匀。头部轮廓、紫色眼睛、上下眼睑、眉毛与鼻尖共同表达方向。

## 四个主方向（均按观看者屏幕坐标）

- 000向上：抬下巴、眼睛看上方，上眼睑与眉毛跟随，不能像直视前方的待机。
- 090向屏幕右：脸和鼻尖转向画面右侧，瞳孔看右；面部左侧更完整可见、远侧面部有自然遮挡。身体和道具只轻微跟随。
- 180向下：下巴微收、眼睛明显看下方，眼睑和眉毛配合；不能只闭眼，也不能仍看正前方。
- 270向屏幕左：脸和鼻尖转向画面左侧，瞳孔看左；与090清楚相反，不能保留向右脸或镜像整个人物道具。

九行顺序000、022.5、045、067.5、090、112.5、135、157.5；十行180、202.5、225、247.5、270、292.5、315、337.5。每个斜向保留其水平和垂直分量，157.5→180和337.5→000均只跨一个小步。最终以主方向明确、整体顺序连贯、没有错象限或反转为硬验收条件；中间角度的细微差异单独记录。

EXECUTION SPECIFICATION:
Use case: identity-preserve. Asset: one unified full-body eight-pose gaze sprite source strip.
Input images in order: 1 spacing-only eight-slot guide (never draw guide lines); 2 canonical identity, costume and compact chibi proportions reference; 3 approved standard poses for style and anchored feet; 4 approved cardinal families, ordered UP, SCREEN-RIGHT, DOWN, SCREEN-LEFT. Preserve those native anime violet eyes and 2.5-head compact silhouette.
Make a landscape canvas. CRITICAL: figures must be SMALLER in a central horizontal band; each full crown-to-boot character occupies roughly 40–50 percent of canvas height. Eight equal invisible columns, each containing exactly one complete character. Leave substantial pure magenta horizontal gutters between all neighboring hair, roses, cards and capes. Generous blank magenta top, bottom and outer side margins. NO touching foreground between characters, no cropped crown or boot.
Fixed pose sequence LEFT TO RIGHT: 1 UP, 2 mostly UP and slightly screen-RIGHT, 3 UP-RIGHT diagonal, 4 mostly screen-RIGHT slightly UP, 5 unequivocally SCREEN-RIGHT, 6 mostly screen-RIGHT slightly DOWN, 7 DOWN-RIGHT diagonal, 8 mostly DOWN slightly screen-RIGHT. FIRST is chin lifted and violet eyes looking UP; FIFTH has face, nose and gaze unmistakably toward the viewer's RIGHT image edge. Final poses progressively approach the approved open-eyed DOWN cardinal family. Whole body stays planted and upright throughout.
Same tiny dark-green heart-themed boots, black tights, short white-frilled green dress, red cape, long sage hair, heart crown attached to head. Rose in anatomical right hand (normally viewer-left), heart card in anatomical left hand (normally viewer-right), both kept close to torso. Body scale, leg placement and skirt baseline unchanged. Eyes, eyelids, eyebrows, nose, face and head/neck naturally turn together. No whole-body tilts or detached pupil replacements. Near-vertical oblique aiming cues can be subtle; never exaggerate anatomical warps.
Opaque flat pure #FF00FF backdrop throughout. No transparent output. No grids, text, labels, arrows, captions, effects, shadows or extra objects.

TARGETED SPACING CORRECTION FOR THIS EXECUTION — OVERRIDES EARLIER APPROXIMATE LAYOUT:
Draw all eight characters UNIFORMLY SMALLER. Aim crown-to-sole height at exactly 40% of the total canvas height, never more than 43%; the entire figure lies inside the middle band from 30% to 70% of canvas height. This leaves large empty magenta areas above and below. Each character silhouette including its widest hair must be no wider than 72% of its own equal eighth-width slot. Centers lie at 6.25%, 18.75%, 31.25%, 43.75%, 56.25%, 68.75%, 81.25%, and 93.75% of canvas width. The blank magenta gutters occupy at least one quarter of every slot width. Especially keep fourth and fifth figures completely separated. Outer figures also have generous blank left/right margin. This is a small sprite strip with expansive empty magenta space, NOT eight large portraits filling the canvas. Preserve exactly the requested coherent direction arc, compact costume proportions and native violet anime eyes. Do not enlarge any character to fill its column.
