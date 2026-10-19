Use completed row9 as the WHOLE-STRIP EDIT TARGET for a new coherent second-half gaze family. Keep its exact canvas dimensions, eight body positions, source pixel body/head scale, skirt, hands, feet baselines, and rendered identity. Redraw the head/eyes coherently for the row10 directions below; do not enlarge or shrink the figures. This is a complete row synthesis, not individual-cell patching.

Create one horizontal look-direction strip for Codex pet `nene_chinoiserie`, atlas row 10.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip and completed coherent row 9 are authoritative. Use the cardinals for direction meaning and row 9 for cross-row identity, scale, registration, and continuity.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `180`: vertical DOWN; no horizontal requirement.
2. `202.5`: horizontal SCREEN-LEFT and vertical DOWN.
3. `225`: horizontal SCREEN-LEFT and vertical DOWN.
4. `247.5`: horizontal SCREEN-LEFT and vertical DOWN.
5. `270`: horizontal SCREEN-LEFT; no vertical requirement.
6. `292.5`: horizontal SCREEN-LEFT and vertical UP.
7. `315`: horizontal SCREEN-LEFT and vertical UP.
8. `337.5`: horizontal SCREEN-LEFT and vertical UP.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-left means the viewer's left image edge, never the character's own left. The row should travel naturally through the left half of the loop. Near-vertical 202.5 and 337.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

All16poses keep BOTH EYES OPEN (especiallydown180); visibly rotate eyes/eyelids/brows with restrainedheadyaw/pitch, no pupil-only sticker motion. Keep feet/hem/waist/hands registered and chibi scale identical to neutral. Do not add props or change outfit side placement.

Measured approved row9 SOURCE canvas (2172, 724), pose heights [467, 467, 467, 468, 467, 465, 464, 464]. Keep this same source pixel scale (do not independentlynormalize or resize the figures); the final assembly uses row9 fixed scale 0.4230769230769231.



# Look mechanics: 宁宁 · 新中式礼装

- Human/anime eyes are physical eyes: eye globes, irises, eyelids and brows participate together; do not slide dot pupils over fixed apertures or add replacement eyes.
- Eyes lead attention; restrained neck yaw/pitch and slight upper-body follow-through reinforce direction while face proportions remain unchanged. Long sage hair follows the head plausibly, not a distorted skull.
- Feet, black skirt hem, waist, bow and resting hands keep the canonical registration and shared body scale. No stepping, floating, tilting the whole sprite or broad raster warping.
- Drop earrings remain attached and may be partly occluded as the head turns; lapel and waist bow stay on their original physical sides. No handheld props.
- Four cardinals:000=eyes/head clearlyUP,090=nose and gazeSCREEN-RIGHT,180=chin slightlydown with BOTH EYES OPEN and irises visiblyDOWN,270=nose/gazeSCREEN-LEFT. Left/right use viewer coordinates.
- Keep all16eyes open and small reserved neutral expression; looking down is not blinking/sleeping. Cardinal nose and pupils must visibly aim toward requested edge.
- Eight coherent poses per row, same scale and baseline. Row9=000,022.5,045,067.5,090,112.5,135,157.5; row10=180,202.5,225,247.5,270,292.5,315,337.5. Interpolate head+eyes smoothly, no reversals.
- Inspect normal192x208poses againstidle0, require exact cardinal meaning; report intermediate subtlety as warning only after checking quadrant and continuity.



INPUT ROLES: Image 1 is spacing reference only, image 2 canonical identity reference, image 3 standard contact reference, image 4 cardinal semantics reference, image 5 is the sole WHOLE-STRIP EDIT TARGET. Edit image 5. Preserve its exact 2172x724 canvas and existing eight body positions, each SOURCE figure 464–468 pixels tall. Preserve identical compact 2.5-head proportions. Preserve waist, skirt, hands and foot baseline exactly; no independent figure resizing or head enlargement. New eight-pose gaze family ONLY, in order DOWN, down-slight-left, down-left, LEFT-slight-down, LEFT, LEFT-slight-up, up-left, up-slight-left. At pose 1 (180) BOTH eyes visibly open, chin and pupils aim DOWN. At pose 5 (270) the nose and both iris directions visibly aim SCREEN-LEFT. All physical eyes, eyelids and eyebrows rotate coherently with restrained head pitch/yaw. No blinking, extra eyes or pupil-only sliding. Same costume and earrings; flat pure #FF00FF. Output the whole edited eight-figure strip only, no guides or labels.
