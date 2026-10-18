"""Assemble incrementally validated generated rows without changing artwork."""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--stable-jump', action='store_true', help='Use only after reviewing source jump trajectory lost by component fitting.')
args = parser.parse_args()
run = Path(__file__).resolve().parents[1]
scripts = Path.home() / '.codex/skills/hatch-pet/scripts'
states = ['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
rows = []
for state in states:
    origin = run / 'qa/rows' / state / 'frames'
    record = json.loads((origin / 'frames-manifest.json').read_text(encoding='utf-8'))
    row = record['rows'][0]
    target = run / 'frames' / state
    target.mkdir(parents=True, exist_ok=True)
    for frame in (origin / state).glob('*.png'):
        shutil.copy2(frame, target / frame.name)
    row['frames'] = [str((target / Path(frame).name).resolve()) for frame in row['frames']]
    rows.append(row)

def native(script, *values):
    subprocess.run([sys.executable, str(scripts / script), *map(str, values)], check=True)

if args.stable_jump:
    native('extract_strip_frames.py', '--decoded-dir', run / 'decoded', '--output-dir', run / 'qa/jumping-stable/frames', '--states', 'jumping', '--method', 'stable-slots')
    native('inspect_frames.py', '--frames-root', run / 'qa/jumping-stable/frames', '--json-out', run / 'qa/jumping-stable/review.json', '--states', 'jumping', '--require-components', '--allow-stable-slots')
    for frame in (run / 'qa/jumping-stable/frames/jumping').glob('*.png'):
        shutil.copy2(frame, run / 'frames/jumping' / frame.name)
    next(row for row in rows if row['state'] == 'jumping')['method'] = 'stable-slots'
(run / 'frames/frames-manifest.json').write_text(json.dumps({'ok':True,'chroma_key':record['chroma_key'],'rows':rows},indent=2)+'\n',encoding='utf-8')
native('inspect_frames.py', '--frames-root', run / 'frames', '--json-out', run / 'qa/review.json', '--require-components', '--allow-stable-slots')
native('compose_atlas.py', '--frames-root', run / 'frames', '--output', run / 'final/spritesheet.png', '--webp-output', run / 'final/spritesheet.webp')
native('make_contact_sheet.py', run / 'final/spritesheet.webp', '--output', run / 'qa/contact-sheet.png')
native('render_animation_previews.py', '--frames-root', run / 'frames', '--output-dir', run / 'qa/previews')
