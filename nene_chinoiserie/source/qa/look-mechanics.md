# Look mechanics: 宁宁 · 新中式礼装

- Human/anime eyes are physical eyes: eye globes, irises, eyelids and brows participate together; do not slide dot pupils over fixed apertures or add replacement eyes.
- Eyes lead attention; restrained neck yaw/pitch and slight upper-body follow-through reinforce direction while face proportions remain unchanged. Long sage hair follows the head plausibly, not a distorted skull.
- Feet, black skirt hem, waist, bow and resting hands keep the canonical registration and shared body scale. No stepping, floating, tilting the whole sprite or broad raster warping.
- Drop earrings remain attached and may be partly occluded as the head turns; lapel and waist bow stay on their original physical sides. No handheld props.
- Four cardinals:000=eyes/head clearlyUP,090=nose and gazeSCREEN-RIGHT,180=chin slightlydown with BOTH EYES OPEN and irises visiblyDOWN,270=nose/gazeSCREEN-LEFT. Left/right use viewer coordinates.
- Keep all16eyes open and small reserved neutral expression; looking down is not blinking/sleeping. Cardinal nose and pupils must visibly aim toward requested edge.
- Eight coherent poses per row, same scale and baseline. Row9=000,022.5,045,067.5,090,112.5,135,157.5; row10=180,202.5,225,247.5,270,292.5,315,337.5. Interpolate head+eyes smoothly, no reversals.
- Inspect normal192x208poses againstidle0, require exact cardinal meaning; report intermediate subtlety as warning only after checking quadrant and continuity.
