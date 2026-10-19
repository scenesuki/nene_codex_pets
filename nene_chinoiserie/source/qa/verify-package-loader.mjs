// Validate all renamed workspace packages against the installed app's actual functions.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';

const audit=fileURLToPath(new URL('./',import.meta.url));
const root=path.resolve(audit,'../../..');
const pets=[{new_id:'nene_chinoiserie',display_name:'宁宁 · 新中式礼装'}];
const archive='C:/Program Files/WindowsApps/OpenAI.Codex_26.1013.4894.0_x64__2p2nqsd0c76g0/app/resources/app.asar';
const fd=fs.openSync(archive,'r'),header=Buffer.alloc(16);
fs.readSync(fd,header,0,16,0);
const json=Buffer.alloc(header.readUInt32LE(12));fs.readSync(fd,json,0,json.length,16);
const tree=JSON.parse(json.toString());
const moduleName='src-DsLVGakC.js';
const entry=tree.files['.vite'].files.build.files[moduleName];
const moduleBytes=Buffer.alloc(entry.size);
fs.readSync(fd,moduleBytes,0,moduleBytes.length,8+header.readUInt32LE(4)+Number(entry.offset));
fs.closeSync(fd);
const source=moduleBytes.toString();
function excerpt(start,end){const left=source.indexOf(start),right=source.indexOf(end,left);assert(left>=0&&right>left,start);return source.slice(left,right);}
assert(source.includes('eq=1536,tq=1872,nq=2288'),'Installed constants changed');
const context=vm.createContext({Buffer,eq:1536,tq:1872,nq:2288});
vm.runInContext([excerpt('function sq(','async function cq('),excerpt('function pq(','function _q('),excerpt('function dq(','function fq(')].join('\n'),context);
const hash=data=>crypto.createHash('sha256').update(data).digest('hex');
for(const pet of pets){
  const directory=path.join(root,pet.new_id);
  const manifestBytes=fs.readFileSync(path.join(directory,'pet.json'));
  const manifest=JSON.parse(manifestBytes.toString());
  assert.equal(manifest.id,pet.new_id);assert.equal(manifest.displayName,pet.display_name);
  assert.equal(manifest.spriteVersionNumber,2);assert.equal(manifest.spritesheetPath,'spritesheet.webp');
  const spritePath=context.dq(path,directory,manifest.spritesheetPath);assert(spritePath!==null);
  const bytes=fs.readFileSync(spritePath),decoded=context.pq(bytes),accepted=context.sq(bytes,2);
  assert(accepted!==null);assert.equal(context.sq(bytes,1),null);
  const output=path.join(directory,'preview/app-loader-validation.json');
  const report={ok:true,checked_at:new Date().toISOString(),package_directory:directory,package_files:['pet.json','spritesheet.webp'],id:'custom:'+manifest.id,display_name:manifest.displayName,sprite_version:accepted.spriteVersionNumber,decoded_dimensions:{width:decoded.width,height:decoded.height},format:accepted.extension,manifest_sha256:hash(manifestBytes),spritesheet_sha256:hash(bytes),app_version:'26.1013.4894.0',app_validator_source:archive+'::.vite/build/'+moduleName,app_validator_module_sha256:hash(moduleBytes),method:'Read-only replay of installed-app image/version and path validators on this new workspace package; no installation or UI action',application_ui_detection_verified:false,floating_display_verified:false,current_pet_changed:false};
  fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
}
console.log(JSON.stringify({ok:true,pets:pets.length,app_version:'26.1013.4894.0',validator_module_sha256:hash(moduleBytes),installed:false}));
