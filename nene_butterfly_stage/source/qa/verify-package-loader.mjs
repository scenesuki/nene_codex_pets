// Replay the installed application's image/version and path validators, without driving its UI.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../../', import.meta.url));
const installed = root;
const archive = 'C:/Program Files/WindowsApps/OpenAI.Codex_26.1007.9446.0_x64__2p2nqsd0c76g0/app/resources/app.asar';
const fd = fs.openSync(archive, 'r');
const header = Buffer.alloc(16);
fs.readSync(fd, header, 0, 16, 0);
const jsonBytes = Buffer.alloc(header.readUInt32LE(12));
fs.readSync(fd, jsonBytes, 0, jsonBytes.length, 16);
const tree = JSON.parse(jsonBytes.toString());
const entry = tree.files['.vite'].files.build.files['src-DCNiwad_.js'];
const moduleBytes = Buffer.alloc(entry.size);
fs.readSync(fd, moduleBytes, 0, entry.size, 8 + header.readUInt32LE(4) + Number(entry.offset));
fs.closeSync(fd);
const source = moduleBytes.toString();
function excerpt(start, end) {
  const left = source.indexOf(start);
  const right = source.indexOf(end, left);
  assert(left >= 0 && right > left, `Missing installed validator boundary: ${start}`);
  return source.slice(left, right);
}
const context = vm.createContext({ Buffer, GK: 1536, KK: 1872, qK: 2288 });
vm.runInContext([
  excerpt('function QK(', 'async function $K('),
  excerpt('function iq(', 'function cq('),
  excerpt('function nq(', 'function rq('),
].join('\n'), context);

const manifest = JSON.parse(fs.readFileSync(path.join(installed, 'pet.json'), 'utf8'));
assert.equal(manifest.id, 'nene_costume_2');
assert.equal(manifest.spriteVersionNumber, 2);
assert.equal(manifest.spritesheetPath, 'spritesheet.webp');
assert.equal(typeof manifest.displayName, 'string');
assert(manifest.displayName.trim().length > 0);
const spritePath = context.nq(path, installed, manifest.spritesheetPath);
assert(spritePath !== null, 'Application path validator rejected spritesheetPath');
const bytes = fs.readFileSync(spritePath);
const decoded = context.iq(bytes);
const accepted = context.QK(bytes, manifest.spriteVersionNumber);
assert(accepted !== null, 'Application image/version validator rejected the installed sprite');
assert.equal(context.QK(bytes, 1), null, 'v1 should reject the v2 atlas height');
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const report = {
  ok: true,
  package_directory: installed,
  package_files: ['pet.json', 'spritesheet.webp'],
  id: `custom:${manifest.id}`,
  display_name: manifest.displayName,
  sprite_version: accepted.spriteVersionNumber,
  decoded_dimensions: { width: decoded.width, height: decoded.height },
  format: accepted.extension,
  spritesheet_sha256: hash(bytes),
  app_validator_source: `${archive}::.vite/build/src-DCNiwad_.js`,
  app_validator_module_sha256: hash(moduleBytes),
  method: 'standalone workspace package: read-only replay of installed-app image/version and path validators, no pet installation or app UI action',
  application_ui_detection_verified: false,
  floating_display_verified: false,
  current_pet_changed: false,
};
fs.writeFileSync(path.join(root, 'preview/app-loader-validation.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
