Create one horizontal animation strip for Codex pet `nene-initial-uniform`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Kusanagi Nene from Project SEKAI, initial Kamiyama high school uniform, one-star Foul-Mouthed and Unsociable card. Long muted sage-grey green hair past waist, thick asymmetrical sweeping bangs and two low-tied sidelocks held by small dark rose bands; violet eyes. Navy blazer with thin white piping around lapels and pockets, two brass buttons; white shirt; red diagonal white striped bow ribbon; blue grey plaid pleated skirt; dark grey short calf socks and brown school loafers. No props. Quiet mildly deadpan shy girl, restrained expressions, tiny hesitant wave, focused chin-hand thinking, modest happy small jump. Preserve outfit and face across all frames.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Japanese chibi anime illustration, 2.5-head full body, clean dark outlines, soft cel shading, readable compact features; no pixel art, no 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Hover jump loop: anticipation, lift, airborne peak, descent, and settle through body height.

State requirements:
- Show the jump through pose and vertical body position only: anticipation, lift, airborne peak, descent, settle.
- Do not draw ground shadows, contact shadows, drop shadows, oval shadows, landing marks, dust, smears, bounce pads, or motion marks under the pet.
- Keep the background outside the pet perfectly flat chroma key with no darker key-colored patches.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Nene-specific sequence: modest anticipation crouch, lifting off, a small cheerful airborne hop, descending, settle back toward starting stance. Hair and skirt follow gently; keep socks and shoes unchanged.
