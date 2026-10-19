Create one horizontal animation strip for Codex pet `nene_chinoiserie`, state `waiting`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Kusanagi Nene from trained card 夢をのせたメロディー. Compact 2.5-head chibi with short legs, long loose muted sage-green hair, purple eyes. Card is authoritative for upper body and hairstyle; original-color full-body model supplies lower body. Deep navy/blue-violet asymmetric Chinese-inspired wrap jacket with grey diagonal lapel, pearl trim, multicolor botanical bird-like embroidery, side waist bow, flared three-quarter sleeves. Long black ankle-length skirt with asymmetric slit and grey patterned inset; grey ankle socks with visible sock tops; black strapped low leather shoes. Blue gemstone drop earrings, black ring choker. Centered front-facing standing, both eyes open, quiet reserved smile, arms close to body. No bird/scenery/new props; keep asymmetry, do not mirror. Gentle hop only, maximum about 8 final-cell pixels.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Japanese chibi anime illustration, clean fine outlines, soft cel shading, compact short-leg proportions, readable at 192x208..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Needs-input loop: expectant asking pose for approval, help, or user input.

State requirements:
- Show that Codex needs approval, help, or user input through an expectant asking pose.
- Keep the motion patient and readable, without turning it into ordinary idle or review.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Specific motion: SIX expectant user-input poses: hands near chest, gentle questioning head tilt, raised brows, small look toward viewer, hold, return; both eyes generally open, no new props.
Keep every figure identical scale/head proportions with generous outer margins.
