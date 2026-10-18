Create one horizontal look-direction strip for Codex pet `nene-initial-uniform`, atlas row 10.

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

IMPORTANT LAYOUT: The attached1536x512 guide has a central208px-high short row: draw small fullbody characters only inside those short rectangles, about40percent of image height, with wide empty magenta above/below. Leave full-height magenta gaps between hair of all adjacent poses. Keep feet/legs/skirt/torso fixed and both hands low, exactly2arms2hands. Use eyes+eyelids+natural headneck pitch/yaw to express gaze; no body rotation, distorted skull, or pupil-only cheats. Match approved cardinals exactly at their directions; diagonals progress gradually.
CROSS-ROW SCALE PRIORITY: Match the attached completed row9 canvas and actual character scale exactly; row9 has safe spacing and characters about53percent canvas height. This approved source scale overrides the approximate40percent suggestion above. Keep feet at same source-height baseline and all head/body proportions. Pose180 should naturally continue after157.5, and337.5 naturally precede000; keep these near-vertical poses mostly frontal with only small left yaw. Direction arc: down, slightlydownleft, downleft, mostlyleftdown, LEFT, mostlyleftup, upleft, slightlyupleft. Nearvertical202.5 and337.5 must have less yaw than225/315, so head returns gradually to frontal instead of a sudden snap.
CRITICAL LEFT-HALF REPAIR: The completed row9 is ONLY a body-size/baseline/style reference; NEVER copy its right-facing head directions. Use the LAST pose in approvedcardinals (270 screenLEFT) for EVERY leftward head. This is NOT a 3D turntable spin. All poses2 through8 look to viewerSCREENLEFT, with nose and pupils LEFT of head center. The head never turns right anywhere in this row. Pose1 frontal down;2 slightLEFTdown;3 LEFTdown;4 LEFT with chin slightly down;5 unmistakableLEFT matching270;6 STILLLEFT but chin slightly up;7 STILLLEFT plus higher gaze;8 almost frontal but pupils/nose subtly LEFT and clearly UP. Pose6,7,8 MUST NOT copy row9 upward-right poses. As gaze pitches upward after270, preserve LEFT yaw sign and progressively reduce its magnitude toward0. Equal8slots with visible full-height magenta gaps between hair, never touching. Match row9 source2172x724/53percent bodyheight, do not enlarge.
