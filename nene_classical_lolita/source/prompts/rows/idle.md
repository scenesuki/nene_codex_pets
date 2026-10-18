Create one horizontal animation strip for Codex pet `nene_classical_lolita`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Kusanagi Nene, card 886 trained Queen of Heart. Long pale sage-green hair and lavender-purple eyes. Small upright gold crown with red heart jewels. Dark emerald-green fitted short lolita dress above the knees, gold piping, ivory layered lace underskirt and ruffled hem. Short rich-red cape with fluffy ivory collar, cream cravat bow, rose/pink heart medallion and red-black diamond accents. Opaque black tights; dark-green low boots with white frilled cuffs and small gold diamond detail. White lace wrist cuffs with emerald ribbons. Retain a single red rose in her anatomical right hand (screen-left in front view) and one small white red-heart playing card in left hand (screen-right). Both props remain attached to hands, close to body. Reserved gentle expression, quiet confident stage presence. Standing full body, compact short legs, preserve garment silhouette and asymmetry. Gentle 8px hop maximum at final cell size; never a high leap. No chair, animals, scenery, floating cards or extra props.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Polished Japanese anime chibi illustration, compact 2.5-head-tall proportions, large readable violet anime eyes, crisp fine dark outlines, soft cel shading. Not pixel art. Keep the exact same style in every state..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Quiet breathing and one tiny blink, hands and both props resting low. Six coherent frames; first and last almost match. Feet planted; no waving or expressive head turning.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
