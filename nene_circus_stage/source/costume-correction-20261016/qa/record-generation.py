"""Record one selected generated strip and run the native row checks."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("job")
parser.add_argument("source", type=Path)
parser.add_argument("--note", required=True)
args = parser.parse_args()
run = Path(__file__).resolve().parents[1]
manifest_path = run / "imagegen-jobs.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
job = next(job for job in manifest["jobs"] if job["id"] == args.job)
assert args.source.is_file(), args.source
output = run / job["output_path"]
if output.exists():
    assert any(
        (run / attempt["preserved_output"]).is_file()
        and (run / attempt["preserved_output"]).read_bytes() == output.read_bytes()
        for attempt in job.get("previous_attempts", [])
    ), "Preserve earlier candidates before selecting another strip"
output.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(args.source, output)
assert output.read_bytes() == args.source.read_bytes()
job.update(source_path=str(args.source), source_sha256=hashlib.sha256(output.read_bytes()).hexdigest(), worker_qa=args.note, selected_at=datetime.now(timezone.utc).isoformat(), status="selected-awaiting-validation")
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if job["kind"] == "row-strip":
    scripts = Path.home() / ".codex/skills/hatch-pet/scripts"
    qa = run / "qa/rows" / args.job
    subprocess.run([sys.executable, str(scripts / "extract_strip_frames.py"), "--decoded-dir", str(run / "decoded"), "--output-dir", str(qa / "frames"), "--states", args.job, "--method", "auto"], check=True)
    subprocess.run([sys.executable, str(scripts / "inspect_frames.py"), "--frames-root", str(qa / "frames"), "--json-out", str(qa / "review.json"), "--states", args.job, "--require-components"], check=True)
    job.update(status="complete", completed_at=datetime.now(timezone.utc).isoformat())
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"job": args.job, "status": job["status"], "copied_to": str(output)}, ensure_ascii=False))
