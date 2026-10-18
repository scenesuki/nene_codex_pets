"""Render previews by cropping the cleaned atlas without altering sprite geometry."""
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[2]
atlas = Image.open(root / "source/final/spritesheet-extended.webp").convert("RGBA")
output = root / "preview"
output.mkdir(exist_ok=True)
states = {
    "idle": [280, 110, 110, 140, 140, 320],
    "running-right": [120] * 7 + [220],
    "running-left": [120] * 7 + [220],
    "waving": [140] * 3 + [280],
    "jumping": [140] * 4 + [280],
    "failed": [140] * 7 + [240],
    "waiting": [150] * 5 + [260],
    "running": [120] * 5 + [220],
    "review": [150] * 5 + [280],
}
frames_by_state = {}
for row, (state, durations) in enumerate(states.items()):
    frames = [atlas.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))
              for column in range(len(durations))]
    frames_by_state[state] = frames
    frames[0].save(output / f"{state}.gif", save_all=True, append_images=frames[1:],
                   duration=durations, loop=0, disposal=2, optimize=False)

look_frames = [atlas.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))
               for row in (9, 10) for column in range(8)]
look_frames[0].save(output / "look-directions.gif", save_all=True,
                    append_images=look_frames[1:], duration=200, loop=0, disposal=2, optimize=False)

labels = ["Idle", "Move right", "Move left", "Wave", "Jump", "Failed", "Needs input", "Working", "Review"]
overview = []
for step in range(28):
    canvas = Image.new("RGB", (576, 678), "#f6f5f8")
    draw = ImageDraw.Draw(canvas)
    for index, (state, durations) in enumerate(states.items()):
        elapsed = step / 28 * sum(durations)
        frame_index = 0
        while frame_index < len(durations) - 1 and elapsed >= durations[frame_index]:
            elapsed -= durations[frame_index]
            frame_index += 1
        x, y = (index % 3) * 192, (index // 3) * 226
        draw.text((x + 8, y + 3), labels[index], fill="#35313d")
        frame = frames_by_state[state][frame_index]
        canvas.paste(frame, (x, y + 18), frame)
    overview.append(canvas)
overview[0].save(output / "animation-overview.gif", save_all=True,
                  append_images=overview[1:], duration=60, loop=0, optimize=False)
print(f"Rendered 9 state GIFs, 16-direction GIF and overview into {output}")
