"""Reproduce the two-pixel validator/cleanup selection mismatch."""
import importlib.util
import math
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("despill_under_test", Path(sys.argv[1]))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
# Opaque source pixel from running-right cell1, and its translucent neighbor.
pixels = [(150, 170, 160, 255)] * 9
pixels[4] = (233, 27, 167, 255)
pixels[7] = (204, 40, 172, 127)
pixels[8] = (0, 0, 0, 0)
key = tuple(mod.srgb_to_linear(v / 255) for v in (255, 0, 255))
result, _ = mod.suppress_boundary_spill(
    pixels, size=(3, 3), boundary=[True] * 9, key_linear=key,
    strength=1, edge_radius=5, spill_tolerance=.15, minimum_saturation=.1)
assert math.dist(result[4][:3], (255, 0, 255)) > 96, "Opaque validator-positive pixel was not selected"
assert math.dist(result[7][:3], (255, 0, 255)) > 96, "Contaminated opaque neighbor propagated key color"
assert [p[3] for p in result] == [p[3] for p in pixels], "Alpha changed"
assert result[0] == pixels[0], "Uncontaminated opaque color changed"
print("PASS: validator-positive opaque edge selected; neighbor clean; alpha and clean interior preserved")
