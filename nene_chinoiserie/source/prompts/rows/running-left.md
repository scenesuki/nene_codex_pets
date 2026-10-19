Create one horizontal animation strip for Codex pet `nene_chinoiserie`, state `running-left`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Kusanagi Nene from trained card 夢をのせたメロディー. Compact 2.5-head chibi with short legs, long loose muted sage-green hair, purple eyes. Card is authoritative for upper body and hairstyle; original-color full-body model supplies lower body. Deep navy/blue-violet asymmetric Chinese-inspired wrap jacket with grey diagonal lapel, pearl trim, multicolor botanical bird-like embroidery, side waist bow, flared three-quarter sleeves. Long black ankle-length skirt with asymmetric slit and grey patterned inset; grey ankle socks with visible sock tops; black strapped low leather shoes. Blue gemstone drop earrings, black ring choker. Centered front-facing standing, both eyes open, quiet reserved smile, arms close to body. No bird/scenery/new props; keep asymmetry, do not mirror. Gentle hop only, maximum about 8 final-cell pixels.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Japanese chibi anime illustration, clean fine outlines, soft cel shading, compact short-leg proportions, readable at 192x208..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-left loop: show directional movement to the left through body and limb poses only.

State requirements:
- Show directional drag movement to the left through body, limb, and prop movement only.
- The row must unmistakably face and travel left.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Specific motion: EIGHT distinct gait poses travelling SCREEN-LEFT, matching rightward row cadence but actually redraw opposite view. Preserve asymmetric bow/lapel on their physical sides; do NOT horizontally mirror the costume.
Keep every figure identical scale/head proportions with generous outer margins.
