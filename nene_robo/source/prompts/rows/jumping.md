Create one horizontal animation strip for Codex pet `nene-robo`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Official original Robo-Nene/NeneRobo from Project SEKAI, a compact rigid humanoid stage robot modeled after Kusanagi Nene. Preserve original mascot proportions: huge broad head, short stout body, grey-sage long segmented hair with two thick low sidelocks and pink round ties, lavender circular eyes, subtle vertical cheek panel seams, green headband, angular pale lime butterfly hair ornament with pink double outline on screen-right, pink striped neck bow, teal sleeveless vest with pale yellow piping and three yellow buttons over pale cream short sleeves with pink cuffs, flared skirt alternating pale yellow and cream panels with lavender hem, short pale yellow legs/boot shafts with black bow detail, dark teal rounded shoes. Small lavender balls at skirt sides remain attached by short solid rods, never floating. Arms short and simple, hands mitten-like. No school uniform. Natural printed robot eyes and rigid head pitch/yaw, no whole-sprite rotation.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Close to the original Japanese mobile game robot illustration and official box art: clean thin dark outlines, crisp restrained cel shading, flat pastel colors, iconic 2-head-tall mascot geometry, slightly deadpan cute robot face; 2D game sprite, not photorealistic plastic, not generic human chibi, not pixel art..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Hover jump loop: anticipation, lift, airborne peak, descent, and settle through body height.

State requirements:
- Show the jump through pose and vertical body position only: anticipation, lift, airborne peak, descent, settle.
- Do not draw ground shadows, contact shadows, drop shadows, oval shadows, landing marks, dust, smears, bounce pads, or motion marks under the pet.
- Keep the background outside the pet perfectly flat chroma key with no darker key-colored patches.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
