# nene_movie gaze mechanics

Humanoid head leads gaze. Torso, pinafore skirt hem, shoes and anatomical LEFT hand with popcorn bucket stay anchored. The free right hand rests; no prop swap. Neck bends naturally, face surface and nose shift with yaw, violet irises/pupils and eyelids track the target. Hair follows slightly without flipping yellow bows. Bucket and popcorn remain upright, hand-attached, stationary against torso.

- UP000: frontal head, chin slightly raised, pupils high under upper lids, clearly different from neutral.
- RIGHT090: face turns toward image right, nose tip and pupils right of head center, far eye narrows; body fixed.
- DOWN180: frontal head, chin tucked and open eyes look down, not a blink.
- LEFT270: face turns toward image left, nose tip and pupils left of head center, opposite right. Never mirror body or switch bucket hand.
- Diagonals use both horizontal and vertical cues; near-vertical directions use small yaw rather than maintaining profile. Each22.5 step changes head/eye pose by similarly small visual amounts.
- Row9 goes UP→RIGHT→DOWN. Row10 goes DOWN→LEFT→UP and deliberately faces opposite to row9. 157.5→180 and337.5→000 must be small coherent transitions without anchor/scale changes.
- No whole-sprite rotation, skew, head pasted from another style, detached eyes, new facial markings, body rocking, loose popcorn, effects or text. Final family is generated one whole8pose row per source, no one-off cell patches.
