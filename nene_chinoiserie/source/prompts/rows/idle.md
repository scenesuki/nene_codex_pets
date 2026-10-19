Create one horizontal animation strip for Codex pet `nene_chinoiserie`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Kusanagi Nene from trained card 夢をのせたメロディー. Compact 2.5-head chibi with short legs, long loose muted sage-green hair, purple eyes. Card is authoritative for upper body and hairstyle; original-color full-body model supplies lower body. Deep navy/blue-violet asymmetric Chinese-inspired wrap jacket with grey diagonal lapel, pearl trim, multicolor botanical bird-like embroidery, side waist bow, flared three-quarter sleeves. Long black ankle-length skirt with asymmetric slit and grey patterned inset; grey ankle socks with visible sock tops; black strapped low leather shoes. Blue gemstone drop earrings, black ring choker. Centered front-facing standing, both eyes open, quiet reserved smile, arms close to body. No bird/scenery/new props; keep asymmetry, do not mirror. Gentle hop only, maximum about 8 final-cell pixels.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Japanese chibi anime illustration, clean fine outlines, soft cel shading, compact short-leg proportions, readable at 192x208..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Calm low-distraction resting loop: subtle breathing, tiny blink, slight head/body bob, and only quiet persona-preserving motion.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Specific motion: Six calm frontal frames: open eyes/rest, tiny inhale, partial blink, full blink, reopen, return to initial rest. Feet planted, micro breathing only.
Keep every figure identical scale/head proportions with generous outer margins.
