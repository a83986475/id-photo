#!/usr/bin/env python3
"""ID Photo Studio - 纯前端证件照制作工具 (v5 - 重构版)"""
import os, base64

STATIC = r'C:\Users\Yang\wx-channel\sph\static'
def b64(p):
    with open(os.path.join(STATIC, p), 'rb') as f:
        return base64.b64encode(f.read()).decode()

QR_B64 = b64('qrcode_opt.jpg')
DONATE_B64 = b64('donate_opt.jpg')
ICON_B64 = b64('icon_opt.png')
path = r'C:\Users\Yang\Desktop\photo.html'

CSS = r'''
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#f2f0eb;--surface:#ffffff;--s2:#f8f7f4;--text:#1c1a15;--muted:#7a756c;--border:#e3e0d9;--border-light:#efede8;--p:#0b5840;--ph:#073d2b;--phl:#dff0e9;--pulse:#10b981;--gold:#c9a84c;--gold-light:#f5edd6;--shadow:0 1px 3px rgba(0,0,0,.04),0 4px 16px rgba(0,0,0,.06);--shadow-lg:0 8px 40px rgba(0,0,0,.1);--shadow-glow:0 0 30px rgba(11,88,64,.12);--radius:16px;--radius-sm:10px;--radius-xl:24px;--font:"Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;--transition:.25s cubic-bezier(.4,0,.2,1);--bounce:.5s cubic-bezier(.34,1.56,.64,1)}
[data-theme=dark]{--bg:#11100e;--surface:#181715;--s2:#201e1b;--text:#e6e2d8;--muted:#a39c91;--border:#2f2c27;--border-light:#252320;--p:#3b9b78;--ph:#5bbd99;--phl:#1a2f27;--gold:#b8922f;--gold-light:#2a2415;--shadow:0 1px 3px rgba(0,0,0,.35),0 4px 16px rgba(0,0,0,.45);--shadow-lg:0 8px 40px rgba(0,0,0,.55);--shadow-glow:0 0 30px rgba(59,155,120,.15)}
html{scroll-behavior:smooth}body{margin:0;font-family:var(--font);background:var(--bg);color:var(--text);-webkit-font-smoothing:antialiased;min-height:100vh}
button,input,select,textarea{font:inherit}canvas{display:block;max-width:100%}
.shell{max-width:1280px;margin:0 auto;padding:0 1.5rem}.hidden{display:none!important}
.topbar{display:flex;justify-content:space-between;align-items:center;padding:1rem 0 .8rem;border-bottom:1px solid var(--border);margin-bottom:1.2rem}
.brand{display:flex;align-items:center;gap:.6rem;font-weight:800;font-size:1.2rem;letter-spacing:-.02em}
.brand-logo{width:36px;height:36px;border-radius:10px;overflow:hidden;flex-shrink:0}
.brand-logo img{width:100%;height:100%;object-fit:cover;display:block}
.brand-info{display:flex;flex-direction:column}.brand-name{font-size:1.1rem}
.brand-sub{font-size:.65rem;font-weight:600;color:var(--muted);letter-spacing:.04em;text-transform:uppercase}
.top-actions{display:flex;gap:.5rem;align-items:center}
.tbtn{width:36px;height:36px;display:grid;place-items:center;background:var(--surface);border:1px solid var(--border);border-radius:999px;cursor:pointer;transition:all var(--transition);font-size:1rem;color:var(--text)}
.tbtn:hover{background:var(--s2);border-color:var(--p);transform:scale(1.05);box-shadow:0 0 0 3px var(--phl)}

/* Desktop: Grid areas */
.workspace{display:grid;grid-template-columns:360px 1fr;gap:1.5rem;margin-bottom:1.2rem;align-items:start}
@media(max-width:960px){.workspace{grid-template-columns:1fr}}
@media(max-width:768px){.workspace{display:block}}

.panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-xl);padding:1.5rem;box-shadow:var(--shadow)}
.ptitle{font-size:1.05rem;font-weight:700;margin:0 0 1rem;display:flex;align-items:center;gap:.5rem}
.ptitle small{font-size:.72rem;font-weight:400;color:var(--muted)}

/* Upload: label-based (no CSS overlay, no JS click handler) */
.upload-zone{display:block;border:2px dashed var(--border);border-radius:var(--radius-sm);padding:1.6rem 1rem;text-align:center;cursor:pointer;transition:all var(--transition);background:var(--bg);margin-bottom:.75rem}
.upload-zone:hover{border-color:var(--p);background:var(--phl);transform:translateY(-1px)}
.upload-zone.dragover{border-color:var(--p);background:var(--phl);transform:scale(1.012);box-shadow:0 0 0 4px var(--phl)}
.upload-zone .icon{font-size:2rem;margin-bottom:.35rem;display:block}
.upload-zone .label{font-size:.82rem;font-weight:600;color:var(--text);pointer-events:none}
.upload-zone .hint{font-size:.7rem;color:var(--muted);margin-top:.2rem;pointer-events:none}

.field{display:grid;gap:.2rem;margin-bottom:.8rem}
.field-label{display:flex;justify-content:space-between;align-items:center}
.field label{font-size:.78rem;font-weight:700}.field .val{font-size:.78rem;font-weight:600;color:var(--p);min-width:2rem;text-align:right}
.field select,.field input[type=text]{width:100%;padding:.52rem .8rem;border-radius:var(--radius-sm);border:1px solid var(--border);background:var(--bg);color:var(--text);font-size:.85rem;transition:border .2s;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2712%27 height=%278%27%3E%3Cpath d=%27M1 1l5 5 5-5%27 stroke=%27%237a756c%27 stroke-width=%271.5%27 fill=%27none%27 stroke-linecap=%27round%27/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right .7rem center;padding-right:2rem}
.field select:focus,.field input[type=text]:focus{outline:none;border-color:var(--p);box-shadow:0 0 0 3px var(--phl)}
.field input[type=range]{width:100%;height:4px;-webkit-appearance:none;appearance:none;background:var(--border);border-radius:2px;outline:none;margin-top:.25rem}
.field input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:16px;height:16px;border-radius:50%;background:var(--p);cursor:pointer;border:2px solid var(--surface);box-shadow:var(--shadow);transition:transform .15s}
.field input[type=range]::-webkit-slider-thumb:hover{transform:scale(1.12)}
.field input[type=range]::-moz-range-thumb{width:16px;height:16px;border-radius:50%;background:var(--p);cursor:pointer;border:2px solid var(--surface)}
.seg{display:flex;background:var(--s2);border:1px solid var(--border);border-radius:var(--radius-sm);overflow:hidden}
.seg label{flex:1;cursor:pointer;text-align:center;padding:.42rem .2rem;font-size:.72rem;font-weight:700;transition:all var(--transition)}
.seg input[type=radio]{display:none}.seg label span{display:block;padding:.18rem .12rem;border-radius:7px;transition:all var(--transition)}
.seg input:checked+span{background:var(--p);color:#fff;box-shadow:0 2px 8px rgba(11,88,64,.25)}
.swatches{display:flex;gap:.45rem;flex-wrap:wrap;margin-top:.25rem}
.swatch{width:34px;height:34px;border-radius:999px;cursor:pointer;border:3px solid transparent;transition:all var(--transition);flex-shrink:0}
.swatch:hover{transform:scale(1.1);z-index:2}
.swatch.selected{border-color:var(--text);transform:scale(1.08);box-shadow:0 0 0 2px var(--surface),0 0 0 4px var(--p)}
.swatch .check{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transition:opacity .12s;font-size:.65rem;color:#fff}
.swatch.selected .check{opacity:1}

.btn{padding:.7rem 1.2rem;border:none;border-radius:999px;cursor:pointer;font-weight:700;font-size:.85rem;transition:all var(--transition);display:inline-flex;align-items:center;gap:.45rem;white-space:nowrap}
.btn:active{transform:scale(.96)}
.btn-p{background:linear-gradient(135deg,var(--p),var(--ph));color:#fff;box-shadow:0 2px 12px rgba(11,88,64,.25)}
.btn-p:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 4px 20px rgba(11,88,64,.35)}
.btn-s{background:var(--s2);color:var(--text);border:1px solid var(--border)}
.btn-s:hover:not(:disabled){background:var(--border);transform:translateY(-1px)}
.btn:disabled{opacity:.4;cursor:not-allowed;transform:none!important}
.btn-spinner{width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite;display:none}
.btn.loading .btn-text{opacity:.6}.btn.loading .btn-spinner{display:block}
@keyframes spin{to{transform:rotate(360deg)}}

.status{margin-top:.65rem;padding:.6rem .9rem;border-radius:var(--radius-sm);background:var(--s2);border:1px solid var(--border);font-size:.78rem;min-height:2rem;line-height:1.4}
.status.ok{border-color:var(--p);background:var(--phl);color:var(--p)}
.status.err{border-color:#b02a2a;background:#fef2f2;color:#b02a2a}
[data-theme=dark] .status.err{border-color:#e05050;background:#2a1010;color:#f08080}
.prog{height:5px;background:var(--s2);border-radius:999px;overflow:hidden;border:1px solid var(--border);margin-top:.45rem}
.prog>span{display:block;height:100%;width:0%;background:linear-gradient(90deg,var(--p),var(--pulse));transition:width .3s ease;border-radius:999px}
.notice{font-size:.74rem;padding:.6rem .8rem;border-radius:var(--radius-sm);background:var(--phl);border:1px solid var(--border);margin-top:.65rem;line-height:1.4}

.preview-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:.9rem}
@media(max-width:780px){.preview-grid{grid-template-columns:1fr}}
.card{background:var(--s2);border:1px solid var(--border);border-radius:var(--radius);padding:.75rem}
.card h3{margin:0 0 .4rem;font-size:.78rem;font-weight:700;display:flex;align-items:center;gap:.3rem}
.pframe{aspect-ratio:4/5;display:grid;place-items:center;background:var(--bg);border-radius:var(--radius-sm);overflow:hidden;border:1px solid var(--border-light);position:relative}
.pframe canvas{width:100%;height:100%;object-fit:contain;display:block}
.checker{background-image:linear-gradient(45deg,#c8c4bc 25%,transparent 25%),linear-gradient(-45deg,#c8c4bc 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#c8c4bc 75%),linear-gradient(-45deg,transparent 75%,#c8c4bc 75%);background-size:10px 10px;background-position:0 0,0 5px,5px -5px,-5px 0}
.note{font-size:.65rem;color:var(--muted);margin-top:.3rem;line-height:1.3}

.quality-panel{margin-top:.75rem;padding:.65rem .75rem;border-radius:var(--radius-sm);background:var(--s2);border:1px solid var(--border)}
.q-header{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}
.q-ring{width:40px;height:40px;border-radius:50%;flex-shrink:0;display:grid;place-items:center;font-size:.8rem;font-weight:800;color:#fff;background:var(--muted)}
.q-ring.good{background:linear-gradient(135deg,var(--p),var(--pulse))}
.q-ring.warn{background:linear-gradient(135deg,#e8a020,#d4870e)}
.q-ring.bad{background:linear-gradient(135deg,#d93a3a,#b02a2a)}
.q-info{flex:1;min-width:0}
.q-info .q-label{font-size:.75rem;font-weight:700;color:var(--text)}
.q-info .q-desc{font-size:.65rem;color:var(--muted)}
.q-bar{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:.3rem}
.q-bar>span{display:block;height:100%;border-radius:2px;transition:width .5s ease}
.q-bar>span.good{background:linear-gradient(90deg,var(--p),var(--pulse))}
.q-bar>span.warn{background:linear-gradient(90deg,#e8a020,#f5c542)}
.q-bar>span.bad{background:linear-gradient(90deg,#d93a3a,#f06060)}
.q-items{display:grid;gap:3px;margin-top:.4rem}
.q-item{display:flex;align-items:center;gap:.4rem;padding:.2rem .35rem;border-radius:5px;font-size:.65rem;font-weight:600}
.q-item .icon{font-size:.6rem;width:14px;text-align:center}
.q-item.pass{color:var(--p)}.q-item.fail{color:#b02a2a}.q-item.warn{color:#c49020}

.bottom-bar{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.8rem;padding:.8rem 0 0;border-top:1px solid var(--border)}
.bottom-bar .btn{flex:1;min-width:0;justify-content:center}

#ov{position:fixed;inset:0;background:rgba(0,0,0,.5);display:grid;place-items:center;z-index:999;backdrop-filter:blur(8px)}
#ov .box{background:var(--surface);border-radius:var(--radius-xl);padding:2.2rem 2.5rem;text-align:center;max-width:360px;width:90%;box-shadow:var(--shadow-lg)}
#ov h2{margin:0 0 .35rem;font-size:1.1rem}#ov p{color:var(--muted);font-size:.8rem;margin:0 0 .9rem;line-height:1.4}
#mb{height:7px;background:var(--s2);border-radius:999px;overflow:hidden;border:1px solid var(--border)}
#mb>span{display:block;height:100%;background:linear-gradient(90deg,var(--p),var(--pulse));transition:width .3s ease;border-radius:999px}
#ms{margin-top:.5rem;font-size:.75rem;color:var(--muted)}
#rw{font-size:.72rem;padding:.45rem .7rem;border-radius:var(--radius-sm);background:#fef7e8;border:1px solid #f0d98c;margin-top:.4rem;display:flex;align-items:center;gap:.35rem;flex-wrap:wrap}
[data-theme=dark] #rw{background:#2a2410;border-color:#5a4c20;color:#e8d080}
#rw a{color:var(--p);font-weight:700;cursor:pointer;text-decoration:underline}

.site-footer{margin-top:1.5rem;padding:1.5rem 0 2rem;border-top:1px solid var(--border);text-align:center}
.site-footer .author{font-size:.85rem;font-weight:700;color:var(--text);margin-bottom:.3rem}
.site-footer .author span{color:var(--p)}.site-footer .tagline{font-size:.72rem;color:var(--muted);margin-bottom:1rem}
.site-footer .social-row{display:flex;justify-content:center;gap:2rem;margin-bottom:1rem;flex-wrap:wrap}
.site-footer .social-item{text-align:center;width:120px}
.site-footer .social-item img{width:110px;height:110px;border-radius:12px;border:1px solid var(--border);display:block;margin:0 auto .3rem;transition:transform var(--transition),box-shadow var(--transition)}
.site-footer .social-item img:hover{transform:scale(1.05);box-shadow:var(--shadow-lg)}
.site-footer .social-item .label{font-size:.68rem;color:var(--muted);font-weight:600}
.toast{position:fixed;bottom:1.5rem;right:1.5rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:.7rem 1rem;box-shadow:var(--shadow-lg);font-size:.8rem;font-weight:600;z-index:100;display:flex;align-items:center;gap:.45rem;max-width:300px}
.toast .close{margin-left:auto;cursor:pointer;opacity:.4;font-size:.75rem;padding:2px 5px;border-radius:4px}
.toast .close:hover{opacity:1;background:var(--s2)}

@media(max-width:768px){
  .btn,.swatch,.seg label{touch-action:manipulation}
  .upload-zone{padding:1.5rem 1rem}
  .btn{min-height:44px}
  .swatch{width:34px;height:34px}
  .site-footer{padding:.8rem 0;margin-top:.5rem}
  .topbar .brand small{display:none}
  .pills,.notice{display:none!important}
}
@media(max-width:480px){
  .shell{padding:.4rem}
  .panel{padding:.8rem;border-radius:.8rem}
  .card{padding:.5rem}
  .upload-zone{padding:1rem}
  .field{margin-bottom:.5rem}
}
'''

JS = r'''(function(){
"use strict";
var root=document.documentElement,tbtn=document.getElementById("tbtn"),up=document.getElementById("upload"),dropZone=document.getElementById("dropZone"),sz=document.getElementById("sz"),sm=document.getElementById("sm"),bgcf=document.getElementById("bgcf"),swatches=document.getElementById("swatches"),genBtn=document.getElementById("genBtn"),dlBtn=document.getElementById("dlBtn"),sb=document.getElementById("sb"),pw=document.getElementById("pw"),pb=document.getElementById("pb"),sc=document.getElementById("sc"),mc=document.getElementById("mc"),rc=document.getElementById("rc"),sx=sc.getContext("2d"),mx=mc.getContext("2d"),rx=rc.getContext("2d"),fn=document.getElementById("fn"),mn=document.getElementById("mn"),rn=document.getElementById("rn"),rw=document.getElementById("rw"),lrBtn=document.getElementById("lrBtn"),photoName=document.getElementById("photoName"),photoDims=document.getElementById("photoDims"),photoInfo=document.getElementById("photoInfo"),ov=document.getElementById("ov"),mbi=document.getElementById("mbi"),ms=document.getElementById("ms");
var srcImg=null,faceRes=null,rmbgSess=null,dlURL=null,dlBlob=null,cropRect=null,dragState=null,cachedAl=null,cachedComp=null,animFrom=null,animTo=null,animStart=0,needsRedraw=false,pulsePhase=0,renderId=null;
dropZone.addEventListener("click",function(){upload.click();});
var FM="https://cdn.jsdelivr.net/npm/@vladmandic/face-api@1.7.13/model",RM="https://huggingface.co/briaai/RMBG-1.4/resolve/main/onnx/model_quantized.onnx";
var vx=0,vy=0,vw=0,vh=0;
function setStatus(m,c){sb.textContent=m;sb.className="status"+(c?" "+c:"");}
function setProg(p){pw.classList.remove("hidden");pb.style.width=p+"%";if(p>=100)setTimeout(function(){pw.classList.add("hidden");},500);}
function showToast(msg,d){d=d||2500;var t=document.createElement("div");t.className="toast";t.innerHTML="<span>"+msg+'</span><span class="close">\u2715</span>';document.body.appendChild(t);t.querySelector(".close").addEventListener("click",function(){t.remove();});setTimeout(function(){if(t.parentNode)t.remove();},d);}
function getSpecRatio(){var d=sz.value.split("x").map(Number);return d[0]/d[1];}
function gcd(a,b){while(b){var t=b;b=a%b;a=t;}return a;}
function imgToCx(x){return (x-vx)/vw*sc.width;}
function imgToCy(y){return (y-vy)/vh*sc.height;}
function cxToImg(x){return x/sc.width*vw+vx;}
function cyToImg(y){return y/sc.height*vh+vy;}
function easeOut(t){return 1-Math.pow(1-t,3);}
function startRenderLoop(){if(renderId)return;!function loop(){var isAnim=!!animFrom;if(isAnim){var t=Math.min(1,(Date.now()-animStart)/350),e=easeOut(t),a=animFrom,to=animTo;cropRect.cx=a.cx+(to.cx-a.cx)*e;cropRect.cy=a.cy+(to.cy-a.cy)*e;cropRect.pw=a.pw+(to.pw-a.pw)*e;cropRect.ph=a.ph+(to.ph-a.ph)*e;if(t>=1){cropRect=to;animFrom=null;}needsRedraw=true;}pulsePhase=(pulsePhase+0.035)%(Math.PI*2);if(needsRedraw){drawCropOverlay();updatePreview();needsRedraw=false;}renderId=requestAnimationFrame(loop);}();}
function setStep(n){document.querySelectorAll(".step-dot").forEach(function(el,i){el.classList.toggle("done",i+1<n);el.classList.toggle("active",i+1===n);});document.querySelectorAll(".step-connector").forEach(function(el,i){el.classList.toggle("done",i+1<n);});}
var th=window.matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light";root.setAttribute("data-theme",th);tbtn.textContent=th==="dark"?"\u2600\ufe0f":"\U0001f319";tbtn.addEventListener("click",function(){th=th==="dark"?"light":"dark";root.setAttribute("data-theme",th);this.textContent=th==="dark"?"\u2600\ufe0f":"\U0001f319";});
document.querySelectorAll("input[name=bg]").forEach(function(r){r.addEventListener("change",function(){var v=document.querySelector("input[name=bg]:checked").value;bgcf.style.display=v==="color"?"":"none";var rf=document.getElementById("rf");rf.className="pframe"+(v==="transparent"?" checker":"");});});
document.querySelectorAll("input[name=fmt]").forEach(function(r){r.addEventListener("change",function(){var v=document.querySelector("input[name=fmt]:checked").value;document.getElementById("qualField").classList.toggle("hidden",v!=="jpeg");});});
document.getElementById("qual").addEventListener("input",function(){document.getElementById("qualVal").textContent=this.value+"%";});
sm.addEventListener("change",function(){needsRedraw=true;});
swatches.addEventListener("click",function(e){var sw=e.target.closest(".swatch");if(!sw)return;swatches.querySelectorAll(".swatch").forEach(function(s){s.classList.remove("selected");});sw.classList.add("selected");});

async function loadFace(){mbi.style.width="15%";ms.textContent="\u68c0\u6d4b\u73af\u5883\u2026";await new Promise(function(r){setTimeout(r,300);});mbi.style.width="30%";ms.textContent="\u52a0\u8f7d tinyFaceDetector\u2026";await faceapi.nets.tinyFaceDetector.loadFromUri(FM);mbi.style.width="65%";ms.textContent="\u52a0\u8f7d faceLandmark68Net\u2026";await faceapi.nets.faceLandmark68Net.loadFromUri(FM);mbi.style.width="100%";ms.textContent="\u6a21\u578b\u52a0\u8f7d\u5b8c\u6210!";await new Promise(function(r){setTimeout(r,400);});ov.classList.add("hidden");}
loadFace().catch(function(e){ms.textContent="\u52a0\u8f7d\u5931\u8d25: "+e.message;setTimeout(function(){ov.classList.add("hidden");},2500);});
async function loadRmbg(){setStatus("\u6b63\u5728\u52a0\u8f7d RMBG \u6a21\u578b\uff08\u9996\u6b21\u7ea650MB\uff09\u2026");rw.classList.add("hidden");genBtn.disabled=true;ort.env.wasm.wasmPaths="https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/";try{rmbgSess=await ort.InferenceSession.create(RM,{executionProviders:["wasm"]});setStatus("RMBG \u6a21\u578b\u52a0\u8f7d\u5b8c\u6210","ok");genBtn.disabled=!srcImg;showToast("RMBG \u5df2\u5c31\u7eea");}catch(e){setStatus("RMBG \u52a0\u8f7d\u5931\u8d25: "+e.message,"err");rmbgSess=null;genBtn.disabled=!srcImg;}}
lrBtn.addEventListener("click",function(e){e.preventDefault();loadRmbg();});

function fitDraw(cv,ctx,img){var W=cv.parentElement.clientWidth||480,H=cv.parentElement.clientHeight||580,r=img.width/img.height,w=r>W/H?W:H*r,h=r>W/H?W/r:H;cv.width=w;cv.height=h;ctx.clearRect(0,0,cv.width,cv.height);ctx.drawImage(img,0,0,cv.width,cv.height);}
async function detectFace(cv){try{var det=await faceapi.detectSingleFace(cv,new faceapi.TinyFaceDetectorOptions({inputSize:416,scoreThreshold:0.38})).withFaceLandmarks();return det||null;}catch(e){return null;}}
function drawLM(ctx,det){if(!det||!det._sx)return;ctx.save();var pts=det.landmarks.positions,sx=det._sx,sy=det._sy;ctx.fillStyle="rgba(1,212,168,.6)";pts.forEach(function(p){var px=imgToCx(p.x*sx),py=imgToCy(p.y*sy);ctx.beginPath();ctx.arc(px,py,2,0,Math.PI*2);ctx.fill();});ctx.fillStyle="rgba(255,200,50,.8)";for(var i=36;i<48;i++){var p=pts[i];var px=imgToCx(p.x*sx),py=imgToCy(p.y*sy);ctx.beginPath();ctx.arc(px,py,3,0,Math.PI*2);ctx.fill();}var b=det.detection.box;ctx.strokeStyle="rgba(1,212,168,.5)";ctx.lineWidth=1.5;ctx.setLineDash([4,4]);ctx.strokeRect(imgToCx(b.x*sx),imgToCy(b.y*sy),b.width*sx/vw*sc.width,b.height*sy/vh*sc.height);ctx.setLineDash([]);ctx.restore();}
startRenderLoop();
setTimeout(function(){checkQuality();},100);

async function rmbgInfer(bmp){if(!rmbgSess)return null;var S=1024,t=document.createElement("canvas");t.width=S;t.height=S;t.getContext("2d").drawImage(bmp,0,0,S,S);var d=t.getContext("2d").getImageData(0,0,S,S).data,f=new Float32Array(3*S*S);for(var i=0;i<S*S;i++){f[i]=d[i*4]/255-0.5;f[S*S+i]=d[i*4+1]/255-0.5;f[2*S*S+i]=d[i*4+2]/255-0.5;}var tn=new ort.Tensor("float32",f,[1,3,S,S]),out=await rmbgSess.run({[rmbgSess.inputNames[0]]:tn}),raw=out[rmbgSess.outputNames[0]].data,mn=Infinity,MX=-Infinity;for(var i=0;i<raw.length;i++){if(raw[i]<mn)mn=raw[i];if(raw[i]>MX)MX=raw[i];}var range=MX-mn||1,al=new Uint8ClampedArray(S*S);for(var i=0;i<S*S;i++)al[i]=((raw[i]-mn)/range)*255;return al;}
function drawMask(al){if(!al){mc.width=200;mc.height=250;mx.fillStyle="rgba(128,128,128,.08)";mx.fillRect(0,0,200,250);return;}var S=1024;mc.width=S;mc.height=S;var id=mx.createImageData(S,S);for(var i=0;i<S*S;i++){id.data[i*4]=al[i];id.data[i*4+1]=al[i];id.data[i*4+2]=al[i];id.data[i*4+3]=255;}mx.putImageData(id,0,0);}
function composite(bmp,al){var iw=bmp.width,ih=bmp.height,bgT=document.querySelector("input[name=bg]:checked").value,out=document.createElement("canvas");out.width=iw;out.height=ih;var oc=out.getContext("2d");if(bgT==="color"){var sw=swatches.querySelector(".swatch.selected");oc.fillStyle=sw?sw.dataset.color:"#2f62ff";oc.fillRect(0,0,iw,ih);}if(bgT==="original"||!al){oc.drawImage(bmp,0,0);return out;}var mask=document.createElement("canvas");mask.width=1024;mask.height=1024;var mc2=mask.getContext("2d"),mid=mc2.createImageData(1024,1024);for(var i=0;i<1024*1024;i++){mid.data[i*4]=255;mid.data[i*4+1]=255;mid.data[i*4+2]=255;mid.data[i*4+3]=al[i];}mc2.putImageData(mid,0,0);var maskS=document.createElement("canvas");maskS.width=iw;maskS.height=ih;maskS.getContext("2d").drawImage(mask,0,0,iw,ih);var img=document.createElement("canvas");img.width=iw;img.height=ih;var ic=img.getContext("2d");ic.drawImage(bmp,0,0);ic.globalCompositeOperation="destination-in";ic.drawImage(maskS,0,0);oc.drawImage(img,0,0);return out;}
function cropCanvas(bmp,det,comp,rect){var dims=sz.value.split("x").map(Number),tw=dims[0],th=dims[1],iw=bmp.width,ih=bmp.height,cx,cy,pw2,ph;if(rect){cx=rect.cx;cy=rect.cy;pw2=rect.pw;ph=rect.ph;}else{var ratio=tw/th,hsVal=0.42,tm2=0.35,fcx=iw/2,fT=ih*0.12,fB=ih*0.5;if(det&&det._sx){var sx=det._sx,sy=det._sy,pts=det.landmarks.positions,lx=0,rx2=0;for(var i=36;i<42;i++)lx+=pts[i].x*sx;for(var i=42;i<48;i++)rx2+=pts[i].x*sx;fcx=(lx/6+rx2/6)/2;var b=det.detection.box;fT=b.y*sy;fB=(b.y+b.height)*sy;}else if(det){var pts=det.landmarks.positions,lx=0,rx2=0;for(var i=36;i<42;i++)lx+=pts[i].x;for(var i=42;i<48;i++)rx2+=pts[i].x;fcx=(lx/6+rx2/6)/2;var b=det.detection.box;fT=b.y;fB=b.y+b.height;}var fh=fB-fT,ph2=fh/hsVal;pw2=ph2*ratio;cx=fcx-pw2/2;cy=fT-ph2*tm2;cx=Math.max(0,Math.min(cx,iw-pw2));cy=Math.max(0,Math.min(cy,ih-ph2));ph=Math.min(ph2,ih-cy);pw2=Math.min(pw2,iw-cx);}var out=document.createElement("canvas");out.width=tw;out.height=th;out.getContext("2d").drawImage(comp,cx,cy,pw2,ph,0,0,tw,th);return out;}
function buildSheet(single){var mode=sm.value;if(mode==="single")return single;var cfg=mode==="s33"?{cols:3,rows:3,sw:1748,sh:1240}:{cols:2,rows:4,sw:1748,sh:1240},sh=document.createElement("canvas");sh.width=cfg.sw;sh.height=cfg.sh;var c=sh.getContext("2d");c.fillStyle="#fff";c.fillRect(0,0,cfg.sw,cfg.sh);var gap=28,cw=Math.floor((cfg.sw-gap*(cfg.cols+1))/cfg.cols),ch=Math.floor((cfg.sh-gap*(cfg.rows+1))/cfg.rows);for(var r=0;r<cfg.rows;r++)for(var col=0;col<cfg.cols;col++){var x=gap+col*(cw+gap),y=gap+r*(ch+gap);c.drawImage(single,x,y,cw,ch);c.strokeStyle="#d0d0d0";c.lineWidth=1.2;c.strokeRect(x,y,cw,ch);}return sh;}
function resize_image(canvas,tw,th){var c=document.createElement("canvas");c.width=tw;c.height=th;c.getContext("2d").drawImage(canvas,0,0,tw,th);return c;}
function getPixelsPerMeter(dpi){return Math.round(dpi/0.0254);}
function crc32(t){for(var c=-1,i=0;i<t.length;i++){c^=t[i];for(var j=0;j<8;j++)c=(c&1)?(c>>>1)^0xEDB88320:c>>>1;}return (c^-1)>>>0;}
function injectDPI(pngBlob,dpi){return new Promise(function(res,rej){var r=new FileReader();r.onload=function(){var a=new Uint8Array(r.result),ppm=getPixelsPerMeter(dpi),pos=8;while(pos+4<a.length){var len=(a[pos]<<24)|(a[pos+1]<<16)|(a[pos+2]<<8)|a[pos+3];var type=String.fromCharCode(a[pos+4],a[pos+5],a[pos+6],a[pos+7]);if(type==="IDAT"){var phys=new Uint8Array(21);phys[0]=0;phys[1]=0;phys[2]=0;phys[3]=9;phys[4]=112;phys[5]=72;phys[6]=89;phys[7]=115;phys[8]=ppm>>24&255;phys[9]=ppm>>16&255;phys[10]=ppm>>8&255;phys[11]=ppm&255;phys[12]=phys[8];phys[13]=phys[9];phys[14]=phys[10];phys[15]=phys[11];phys[16]=1;var cd=new Uint8Array(phys.subarray(4,17)),cr=crc32(cd);phys[17]=cr>>24&255;phys[18]=cr>>16&255;phys[19]=cr>>8&255;phys[20]=cr&255;var out=new Uint8Array(a.length+21);out.set(a.subarray(0,pos),0);out.set(phys,pos);out.set(a.subarray(pos),pos+21);res(new Blob([out],{type:"image/png"}));return;}pos+=12+len;}res(pngBlob);};r.onerror=rej;r.readAsArrayBuffer(pngBlob);});}
function formatSize(b){if(!b)return"\u2014";if(b<1024)return b+" B";if(b<1048576)return(b/1024).toFixed(1)+" KB";return(b/1048576).toFixed(1)+" MB";}
function injectJPEGDPI(jpegBlob,dpi){return new Promise(function(res,rej){var r=new FileReader();r.onload=function(){var a=new Uint8Array(r.result);if(a[0]!==255||a[1]!==216){res(jpegBlob);return;}var app0=new Uint8Array(18);app0[0]=255;app0[1]=224;app0[2]=0;app0[3]=16;app0[4]=74;app0[5]=70;app0[6]=73;app0[7]=70;app0[8]=0;app0[9]=1;app0[10]=2;app0[11]=1;app0[12]=dpi>>8&255;app0[13]=dpi&255;app0[14]=app0[12];app0[15]=app0[13];app0[16]=0;app0[17]=0;var out=new Uint8Array(a.length+18);out.set(a.subarray(0,2),0);out.set(app0,2);out.set(a.subarray(2),20);res(new Blob([out],{type:"image/jpeg"}));};r.onerror=rej;r.readAsArrayBuffer(jpegBlob);});}
function initCropRect(bmp,det){
  var iw=bmp.width,ih=bmp.height,ratio=getSpecRatio();
  var fcx=iw/2,fT=ih*0.12,fB=ih*0.5;
  if(det&&det._sx){var sx=det._sx,sy=det._sy,pts=det.landmarks.positions,lx=0,rx2=0;for(var i=36;i<42;i++)lx+=pts[i].x*sx;for(var i=42;i<48;i++)rx2+=pts[i].x*sx;fcx=(lx/6+rx2/6)/2;var b=det.detection.box;fT=b.y*sy;fB=(b.y+b.height)*sy;}else if(det){var pts=det.landmarks.positions,lx=0,rx2=0;for(var i=36;i<42;i++)lx+=pts[i].x;for(var i=42;i<48;i++)rx2+=pts[i].x;fcx=(lx/6+rx2/6)/2;var b=det.detection.box;fT=b.y;fB=b.y+b.height;}
  var fh=fB-fT,hsVal=0.42,tm2=0.35,ph=fh/hsVal,pw=ph*ratio,cy=fT-ph*tm2,cx=fcx-pw/2;
  cx=Math.max(0,Math.min(cx,iw-pw));cy=Math.max(0,Math.min(cy,ih-ph));
  var target={cx:cx,cy:cy,pw:pw,ph:ph,fcx:fcx,fT:fT,fB:fB,fh:fh};
  var from={cx:fcx-10,cy:fT-ph*0.15,pw:20,ph:20/ratio,fcx:fcx,fT:fT,fB:fB,fh:fh};
  cropRect=from;animFrom=from;animTo=target;animStart=Date.now();
}
function drawFaceGuide(ctx,det,W,H,iw,ih){
  if(!cropRect)return;ctx.save();
  var ccx=imgToCx(cropRect.cx),ccy=imgToCy(cropRect.cy),cpw=cropRect.pw/vw*W,cph=cropRect.ph/vh*H;
  var sw=W/vw,sh=H/vh;
  // --- Alignment reference inside crop area ---
  // Center vertical line (subtle)
  ctx.strokeStyle="rgba(255,255,255,.15)";ctx.lineWidth=1;ctx.setLineDash([3,5]);
  ctx.beginPath();ctx.moveTo(ccx+cpw/2,ccy);ctx.lineTo(ccx+cpw/2,ccy+cph);ctx.stroke();ctx.setLineDash([]);
  // Center horizontal line (subtle crosshair)
  ctx.strokeStyle="rgba(255,255,255,.1)";ctx.lineWidth=1;ctx.setLineDash([3,5]);
  ctx.beginPath();ctx.moveTo(ccx,ccy+cph/2);ctx.lineTo(ccx+cpw,ccy+cph/2);ctx.stroke();ctx.setLineDash([]);
  
  // --- Target face area (ghost outline based on settings) ---
  var hsVal=parseFloat(document.getElementById("hs").value),tm2=parseFloat(document.getElementById("tm").value);
  // Eye level is at (topMargin + faceHeight*0.36) from top of crop
  var eyeY=ccy+cph*(tm2+hsVal*0.36),eyeX=ccx+cpw/2;
  // Draw eye level reference line
  ctx.strokeStyle="rgba(255,200,50,.25)";ctx.lineWidth=1.5;ctx.setLineDash([4,6]);
  ctx.beginPath();ctx.moveTo(ccx+10,eyeY);ctx.lineTo(ccx+cpw-10,eyeY);ctx.stroke();ctx.setLineDash([]);
  // Eye level label
  ctx.fillStyle="rgba(255,200,50,.4)";ctx.font="9px system-ui,sans-serif";ctx.textAlign="left";
  ctx.fillText("\u773c\u775b\u53c2\u8003\u7ebf",ccx+15,eyeY-3);
  
  // Draw target face ellipse (where face SHOULD be based on settings)
  if(cropRect.fh){
    var targetFh=cropRect.ph*hsVal; // face height = crop height * head ratio
    var targetFw=targetFh*0.78; // face width ≈ 78% of face height
    var targetFcx=ccx+cpw/2; // centered horizontally
    var targetFcy=ccy+cph*tm2+cropRect.fh/cropRect.ph*cph*0.5; // positioned based on top margin
    // Ghost face fill (subtle)
    var grad=ctx.createRadialGradient(targetFcx,targetFcy,0,targetFcx,targetFcy,targetFw*0.6);
    grad.addColorStop(0,"rgba(0,220,200,.08)");
    grad.addColorStop(1,"rgba(0,220,200,.02)");
    ctx.fillStyle=grad;
    ctx.beginPath();ctx.ellipse(targetFcx,targetFcy,targetFw*0.5,targetFh*0.5,0,0,Math.PI*2);ctx.fill();
    // Ghost face outline
    ctx.strokeStyle="rgba(0,220,200,.3)";ctx.lineWidth=1.5;ctx.setLineDash([4,6]);
    ctx.beginPath();ctx.ellipse(targetFcx,targetFcy,targetFw*0.5,targetFh*0.5,0,0,Math.PI*2);ctx.stroke();ctx.setLineDash([]);
    // Chin dot
    ctx.fillStyle="rgba(0,220,200,.25)";ctx.beginPath();ctx.arc(targetFcx,targetFcy+targetFh*0.48,3,0,Math.PI*2);ctx.fill();
    // Top of head marker
    ctx.fillStyle="rgba(0,220,200,.2)";ctx.beginPath();ctx.arc(targetFcx,targetFcy-targetFh*0.48,3,0,Math.PI*2);ctx.fill();
    // Label
    ctx.fillStyle="rgba(0,220,200,.35)";ctx.font="bold 8px system-ui,sans-serif";ctx.textAlign="center";
    ctx.fillText("\u76ee\u6807\u8138\u90e8\u4f4d\u7f6e",targetFcx,targetFcy+targetFh*0.5+12);
  }
  
  // --- Detected face overlay (where face IS) ---
  if(det&&det._sx&&cropRect){var sx=det._sx,sy=det._sy;var pts=det.landmarks.positions;var ly=0;for(var i=36;i<48;i++)ly+=pts[i].y;ly=ly/12*sy;var eh=(pts[8].y-pts[27].y)*sy*2.4,ew=eh*0.82;var fcx=cropRect.fcx;
    ctx.strokeStyle="rgba(255,180,50,.35)";ctx.fillStyle="rgba(255,180,50,.08)";ctx.lineWidth=2;ctx.setLineDash([]);
    ctx.beginPath();ctx.ellipse(imgToCx(fcx),imgToCy(ly),ew*sw/2,eh*sh/2,0,0,Math.PI*2);ctx.fill();ctx.stroke();
    // Detected eye dots
    ctx.fillStyle="rgba(255,180,50,.5)";[37,46].forEach(function(i){var p=pts[i];ctx.beginPath();ctx.arc(imgToCx(p.x*sx),imgToCy(p.y*sy),4,0,Math.PI*2);ctx.fill();});
    // Chin dot
    ctx.fillStyle="rgba(255,180,50,.35)";ctx.beginPath();ctx.arc(imgToCx(pts[8].x*sx),imgToCy(pts[8].y*sy),3,0,Math.PI*2);ctx.fill();
    // Detected label
    ctx.fillStyle="rgba(255,180,50,.35)";ctx.font="bold 8px system-ui,sans-serif";ctx.textAlign="center";
    ctx.fillText("\u68c0\u6d4b\u5230\u7684\u8138",imgToCx(fcx),imgToCy(ly)-eh*sh*0.5-6);
  }else{
    // No face detected - show generic ghost
    ctx.strokeStyle="rgba(180,180,180,.15)";ctx.fillStyle="rgba(180,180,180,.04)";ctx.lineWidth=1.5;ctx.setLineDash([4,8]);
    var cx2=ccx+cpw/2,cy2=ccy+cph*0.35,eh2=cph*0.35,ew2=eh2*0.78;
    ctx.beginPath();ctx.ellipse(cx2,cy2,ew2,eh2,0,0,Math.PI*2);ctx.fill();ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle="rgba(180,180,180,.15)";ctx.font="bold 8px system-ui,sans-serif";ctx.textAlign="center";
    ctx.fillText("\u8138\u90e8\u53c2\u8003\u4f4d\u7f6e",cx2,cy2+eh2+12);
  }
  
  // --- Head size indicator ---
  if(cropRect.fh){var actualPct=Math.round(cropRect.fh/cropRect.ph*100),targetPct=Math.round(hsVal*100);
    ctx.fillStyle="rgba(255,255,255,.5)";ctx.font="bold 9px system-ui,sans-serif";ctx.textAlign="right";
    ctx.fillText(targetPct+"%\u5934\u50CF\u76ee\u6807 | "+actualPct+"%\u5b9e\u9645",ccx+cpw-10,ccy+cph+14);
  }
  ctx.restore();
}
function drawCropOverlay(){
  if(!srcImg||!cropRect){sx.clearRect(0,0,sc.width,sc.height);return;}
  var W=sc.width,H=sc.height,iw=srcImg.width,ih=srcImg.height;
  sx.clearRect(0,0,W,H);sx.drawImage(srcImg,vx,vy,vw,vh,0,0,W,H);
  var ccx=imgToCx(cropRect.cx),ccy=imgToCy(cropRect.cy),cpw=cropRect.pw/vw*W,cph=cropRect.ph/vh*H;
  // Dark overlay outside crop area
  sx.fillStyle="rgba(0,0,0,.32)";sx.fillRect(0,0,W,ccy);sx.fillRect(0,ccy+cph,W,H-ccy-cph);sx.fillRect(0,ccy,ccx,cph);sx.fillRect(ccx+cpw,ccy,W-ccx-cpw,cph);
  // Face reference guide ON TOP of dark overlay (like passportphotosnap)
  drawFaceGuide(sx,faceRes,W,H,iw,ih);
  var glow=0.15+0.12*Math.sin(pulsePhase),isAnim=!!animFrom;
  sx.save();sx.shadowColor="rgba(255,255,255,"+glow+")";sx.shadowBlur=12+8*Math.sin(pulsePhase*0.7);sx.strokeStyle="#fff";sx.lineWidth=isAnim?3-1.5*(1-Math.min(1,(Date.now()-animStart)/350)):2.5;sx.setLineDash([6,4]);sx.strokeRect(ccx,ccy,cpw,cph);sx.setLineDash([]);sx.restore();
  var hs=16;["nw","ne","sw","se"].forEach(function(c,i){var x=i%2===0?ccx:ccx+cpw-hs,y=i<2?ccy:ccy+cph-hs;sx.fillStyle="#fff";sx.fillRect(x,y,hs,hs);sx.strokeStyle="var(--p)";sx.lineWidth=2.5;sx.strokeRect(x,y,hs,hs);});
  if(dragState){sx.save();sx.strokeStyle="rgba(0,220,200,.5)";sx.lineWidth=1;sx.setLineDash([6,4]);sx.beginPath();sx.moveTo(0,ccy);sx.lineTo(ccx,ccy);sx.moveTo(ccx+cpw,ccy);sx.lineTo(W,ccy);sx.moveTo(0,ccy+cph);sx.lineTo(ccx,ccy+cph);sx.moveTo(ccx+cpw,ccy+cph);sx.lineTo(W,ccy+cph);sx.moveTo(ccx,0);sx.lineTo(ccx,ccy);sx.moveTo(ccx,ccy+cph);sx.lineTo(ccx,H);sx.moveTo(ccx+cpw,0);sx.lineTo(ccx+cpw,ccy);sx.moveTo(ccx+cpw,ccy+cph);sx.lineTo(ccx+cpw,H);sx.stroke();sx.setLineDash([]);sx.restore();}
  var specD=sz.value.split("x").map(Number),g=gcd(specD[0],specD[1]),ratioLabel=specD[0]/g+":"+specD[1]/g;var dimLabel=Math.round(cropRect.pw)+"\u00d7"+Math.round(cropRect.ph)+"px  "+ratioLabel;sx.font="bold 11px system-ui,sans-serif";var dm=sx.measureText(dimLabel),dw=dm.width+12,dh=18;if(ccy>dh+6){sx.fillStyle="rgba(0,0,0,.5)";sx.fillRect(ccx+cpw/2-dw/2,ccy-dh-4,dw,dh);sx.fillStyle="#fff";sx.fillText(dimLabel,ccx+cpw/2-dm.width/2,ccy-9);}else if(H-ccy-cph>dh+6){sx.fillStyle="rgba(0,0,0,.5)";sx.fillRect(ccx+cpw/2-dw/2,ccy+cph+4,dw,dh);sx.fillStyle="#fff";sx.fillText(dimLabel,ccx+cpw/2-dm.width/2,ccy+cph+dh-4);}
  if(faceRes&&faceRes._sx){var pts=faceRes.landmarks.positions;[36,39,42,45].forEach(function(i){var p=pts[i];var px=imgToCx(p.x*faceRes._sx),py=imgToCy(p.y*faceRes._sy);sx.fillStyle="rgba(255,200,50,.5)";sx.beginPath();sx.arc(px,py,3,0,Math.PI*2);sx.fill();});}
  var zmLabel="\u7f29\u653e: "+Math.round(iw/vw*100)+"%";sx.fillStyle="rgba(0,0,0,.45)";sx.fillRect(8,H-28,92,20);sx.fillStyle="#fff";sx.font="11px system-ui,sans-serif";sx.fillText(zmLabel,12,H-14);
  if(cropRect.fh){var hsPct=Math.round(cropRect.fh/cropRect.ph*100),tmPct=Math.round((cropRect.cy-cropRect.fT)/cropRect.ph*100);sx.fillStyle="rgba(0,0,0,.45)";sx.fillRect(W-108,H-28,100,20);sx.fillStyle="#fff";sx.font="11px system-ui,sans-serif";sx.fillText(hsPct+"%\u5934\u50CF | "+tmPct+"%\u9876\u9648",W-100,H-14);sx.fillStyle="rgba(0,0,0,.4)";sx.fillRect(W-108,H-50,100,18);sx.fillStyle="rgba(255,255,255,.7)";sx.font="10px system-ui,sans-serif";sx.fillText("\u6807\u51c6\u53c2\u8003: ~60% | ~15%",W-100,H-38);}
  if(cropRect.cy<vy||cropRect.cy+cropRect.ph>vy+vh||cropRect.cx<vx||cropRect.cx+cropRect.pw>vx+vw){sx.fillStyle="rgba(255,50,50,.12)";sx.fillRect(0,0,W,H);var warn=Math.max(0,250-250*(Date.now()%3000)/3000);sx.fillStyle="rgba(255,50,50,"+Math.min(1,warn/255)+")";sx.font="bold 14px system-ui,sans-serif";sx.textAlign="center";sx.fillText("\u26a0 \u88c1\u5207\u6846\u8d85\u51fa\u89c6\u56fe\uff0c\u7f29\u5c0f\u67e5\u770b",W/2,40);sx.textAlign="start";}
}
function updatePreview(){
  if(!srcImg||!cropRect){rc.width=0;rc.height=0;rn.textContent="\u7b49\u5f85\u751f\u6210\u2026";return;}
  var srcComp=cachedComp||srcImg;
  try{var cropped=cropCanvas(srcImg,faceRes,srcComp,cropRect);var display=sm.value==="single"?cropped:buildSheet(cropped);var PW=rc.parentElement.clientWidth||480,PH=rc.parentElement.clientHeight||580,scale=Math.min(PW/display.width,PH/display.height,1);rc.width=display.width*scale;rc.height=display.height*scale;rx.drawImage(display,0,0,rc.width,rc.height);var dims=sz.value.split("x").map(Number);rn.textContent="\u9884\u89c8 "+display.width+"x"+display.height+"px\uff08"+dims[0]+"x"+dims[1]+"\uff09";}catch(e){rn.textContent="\u9884\u89c8\u66f4\u65b0\u5931\u8d25";}
}
function getDragTarget(mx,my){
  if(!cropRect)return null;var imgX=cxToImg(mx),imgY=cyToImg(my);var ccx=imgToCx(cropRect.cx),ccy=imgToCy(cropRect.cy),cpw=cropRect.pw/vw*sc.width,cph=cropRect.ph/vh*sc.height,hs=20;
  var corners=[{x:ccx,y:ccy},{x:ccx+cpw-hs,y:ccy},{x:ccx,y:ccy+cph-hs},{x:ccx+cpw-hs,y:ccy+cph-hs}];for(var i=0;i<corners.length;i++){var c=corners[i];if(mx>=c.x&&mx<=c.x+hs&&my>=c.y&&my<=c.y+hs)return{type:i<2?(i===0?"nw":"ne"):(i===2?"sw":"se"),origin:{cx:cropRect.cx,cy:cropRect.cy,pw:cropRect.pw,ph:cropRect.ph},start:{ix:imgX,iy:imgY}};}
  if(mx>=ccx&&mx<=ccx+cpw&&my>=ccy&&my<=ccy+cph)return{type:"move",origin:{cx:cropRect.cx,cy:cropRect.cy},start:{ix:imgX,iy:imgY}};
  return null;
}
function applyDrag(mx,my){
  if(!dragState||!cropRect)return;var imgX=cxToImg(mx),imgY=cyToImg(my),iw=srcImg.width,ih=srcImg.height,dx=imgX-dragState.start.ix,dy=imgY-dragState.start.iy;
  if(dragState.type==="move"){var nc=dragState.origin;cropRect.cx=Math.max(0,Math.min(nc.cx+dx,iw-cropRect.pw));cropRect.cy=Math.max(0,Math.min(nc.cy+dy,ih-cropRect.ph));}else{var ratio=getSpecRatio(),o=dragState.origin;if(dragState.type==="nw"){var ndx=o.cx+dx,ndy=o.cy+dy;var npw=o.pw+(o.cx-ndx),nph=npw/ratio;cropRect.cy=Math.max(0,o.cy+(o.ph-nph));cropRect.cx=Math.max(0,ndx);cropRect.pw=Math.min(npw,iw-cropRect.cx);cropRect.ph=cropRect.pw/ratio;}else if(dragState.type==="ne"){var nw2=o.pw+dx;cropRect.pw=Math.max(50,Math.min(nw2,iw-o.cx));cropRect.ph=cropRect.pw/ratio;cropRect.cy=Math.max(0,o.cy+(o.ph-cropRect.ph));}else if(dragState.type==="sw"){var nw3=o.pw-dx;cropRect.cx=Math.max(0,o.cx+dx);cropRect.pw=Math.max(50,Math.min(nw3,iw-cropRect.cx));cropRect.ph=cropRect.pw/ratio;}else if(dragState.type==="se"){var nw4=o.pw+dx;cropRect.pw=Math.max(50,Math.min(nw4,iw-o.cx));cropRect.ph=cropRect.pw/ratio;}cropRect.cx=Math.max(0,Math.min(cropRect.cx,iw-cropRect.pw));cropRect.cy=Math.max(0,Math.min(cropRect.cy,ih-cropRect.ph));}
}
function save_photos(canvas,fmt,dpi,qual){return new Promise(function(res,rej){var mt=fmt==="jpeg"?"image/jpeg":"image/png",q=fmt==="jpeg"?qual/100:undefined;canvas.toBlob(function(b){if(!b){rej(new Error("Blob creation failed"));return;}var onSize=function(b2){document.getElementById("sizeVal").textContent=formatSize(b2.size);};if(fmt==="png"){injectDPI(b,dpi).then(function(b2){onSize(b2);res({blob:b2,ext:".png"});}).catch(function(){onSize(b);res({blob:b,ext:".png"});});}else{injectJPEGDPI(b,dpi).then(function(b2){onSize(b2);res({blob:b2,ext:".jpg"});}).catch(function(){onSize(b);res({blob:b,ext:".jpg"});});}},mt,q);});}
async function handleFile(file){if(!file)return;cropRect=null;dragState=null;animFrom=null;animTo=null;cachedAl=null;cachedComp=null;dlBlob=null;vx=0;vy=0;vw=0;vh=0;needsRedraw=true;if(dlURL){URL.revokeObjectURL(dlURL);dlURL=null;}setStatus("\u6b63\u5728\u52a0\u8f7d\u56fe\u7247\u5e76\u68c0\u6d4b\u4eba\u8138\u2026");photoName.textContent=file.name;genBtn.disabled=true;dlBtn.disabled=true;if(dlURL){URL.revokeObjectURL(dlURL);dlURL=null;}srcImg=await createImageBitmap(file);photoDims.textContent=srcImg.width+"x"+srcImg.height+"px";photoInfo.classList.remove("hidden");fitDraw(sc,sx,srcImg);faceRes=await detectFace(sc);if(faceRes){var _sx=srcImg.width/sc.width,_sy=srcImg.height/sc.height;faceRes._sx=_sx;faceRes._sy=_sy;}vx=0;vy=0;vw=srcImg.width;vh=srcImg.height;initCropRect(srcImg,faceRes);drawCropOverlay();drawLM(sx,faceRes);fn.textContent=faceRes?"\u2713 \u68c0\u6d4b\u5230\u4eba\u8138\uff0c\u9884\u8bbe\u88c1\u5207\u6846\u5df2\u81ea\u52a8\u5c45\u4e2d":"\u26a0 \u672a\u68c0\u6d4b\u5230\uff0c\u88c1\u5207\u6846\u5c45\u4e2d\u4f30\u7b97\u3002\u53ef\u62d6\u62fd\u8c03\u6574";drawMask(null);mn.textContent="\u70b9\u51fb\u300c\u751f\u6210\u8bc1\u4ef6\u7167\u300d\u540e\u83b7\u53d6\u62a0\u56fe";rn.textContent="\u62d6\u62fd\u88c1\u5207\u6846\u9884\u89c8\u6548\u679c";rc.width=0;rc.height=0;cachedAl=null;cachedComp=null;var bt=document.querySelector("input[name=bg]:checked").value;if(bt!=="original"&&!rmbgSess)rw.classList.remove("hidden");genBtn.disabled=false;setStep(2);setStatus(faceRes?"\u2713 \u5df2\u5c31\u7eea\uff01\u62d6\u62fd\u88c1\u5207\u6846\u8c03\u6574\u4f4d\u7f6e\uff0c\u7136\u540e\u70b9\u51fb\u751f\u6210\u3002":"\u5df2\u52a0\u8f7d\uff0c\u53ef\u62d6\u62fd\u88c1\u5207\u6846\u8c03\u6574\u4f4d\u7f6e\u3002",faceRes?"ok":"");showToast("\u7167\u7247\u5df2\u52a0\u8f7d ("+srcImg.width+"\u00d7"+srcImg.height+")");}
up.addEventListener("change",function(e){handleFile(e.target.files[0]);});

// Drag & drop
var dragCounter=0;
dropZone.addEventListener("dragenter",function(e){e.preventDefault();e.stopPropagation();dragCounter++;if(dragCounter===1){this.classList.add("dragover");}});
dropZone.addEventListener("dragleave",function(e){e.preventDefault();e.stopPropagation();dragCounter--;if(dragCounter===0){this.classList.remove("dragover");}});
dropZone.addEventListener("dragover",function(e){e.preventDefault();e.stopPropagation();});
dropZone.addEventListener("drop",function(e){e.preventDefault();e.stopPropagation();this.classList.remove("dragover");dragCounter=0;var f=e.dataTransfer.files;if(f.length)handleFile(f[0]);});

async function genClick(){
  if(!srcImg){showToast("\u8bf7\u5148\u4e0a\u4f20\u7167\u7247");return;}
  genBtn.disabled=true;genBtn.classList.add("loading");dlBtn.disabled=true;
  setStatus("\u6b65\u9aa4 1/3\uff1a\u51c6\u5907\u2026");setProg(8);
  await new Promise(function(r){setTimeout(r,30);});
  var bt=document.querySelector("input[name=bg]:checked").value,al=null;
  if(bt!=="original"){
    if(rmbgSess){
      setStatus("\u6b65\u9aa4 2/3\uff1aRMBG \u63a8\u7406\u2026");setProg(22);
      try{al=await rmbgInfer(srcImg);setProg(62);drawMask(al);mn.textContent="RMBG-1.4 alpha mask \u2713";}catch(e){setStatus("RMBG \u63a8\u7406\u51fa\u9519: "+e.message,"err");}
    }else{setStatus("\u6b65\u9aa4 2/3\uff1aRMBG \u672a\u52a0\u8f7d\uff0c\u7eaf\u8272\u586b\u5145\u3002");setProg(40);}
  }else{setStatus("\u6b65\u9aa4 2/3\uff1a\u4fdd\u7559\u539f\u80cc\u666f\u3002");setProg(40);}
  setStatus("\u6b65\u9aa4 3/3\uff1a\u88c1\u5207\u5408\u6210\u2026");setProg(72);await new Promise(function(r){setTimeout(r,30);});
  var comp=composite(srcImg,al);cachedComp=comp;
  var single=cropCanvas(srcImg,faceRes,comp,cropRect);
  var fmt=document.querySelector("input[name=fmt]:checked").value,dpi=300,qual=parseInt(document.getElementById("qual").value);
  try{
    var resized=resize_image(single,parseInt(sz.value.split("x")[0]),parseInt(sz.value.split("x")[1]));
    var result=await save_photos(resized,fmt,dpi,qual);
    dlBlob=result.blob;
    var ext=result.ext;
    if(dlURL)URL.revokeObjectURL(dlURL);
    dlURL=URL.createObjectURL(dlBlob);
  }catch(e){setStatus("\u5bfc\u51fa\u5931\u8d25\uff0c\u5df2\u4f7f\u7528\u9ed8\u8ba4\u683c\u5f0f","err");}
  dlBtn.disabled=false;
  setProg(100);checkQuality();
  var display=sm.value==="single"?single:buildSheet(single);
  var PW=rc.parentElement.clientWidth||480,PH=rc.parentElement.clientHeight||580,scale=Math.min(PW/display.width,PH/display.height,1);
  rc.width=display.width*scale;rc.height=display.height*scale;rx.drawImage(display,0,0,rc.width,rc.height);
  var dims=sz.value.split("x").map(Number);
  rn.textContent=display.width+"x"+display.height+"px\uff08"+dims[0]+"x"+dims[1]+"\uff09";
  setStatus("\u2713 \u751f\u6210\u5b8c\u6210\uff0c\u70b9\u51fb\u4e0b\u8f7d\u3002","ok");
  genBtn.classList.remove("loading");genBtn.disabled=false;
}
genBtn.addEventListener("click",genClick);

dlBtn.addEventListener("click",function(){
  if(!dlURL||!dlBlob)return;
  var fmt=document.querySelector("input[name=fmt]:checked").value,fname="id-photo-"+(fmt==="png"?".png":".jpg");
  var a=document.createElement("a");a.href=dlURL;a.download=fname;a.click();
});

function sharePhoto(){
  var url=window.location.href;
  if(navigator.share)navigator.share({title:"ID Photo Studio",text:"\u62cd\u8bc1\u4ef6\u7167\u4e0d\u6c42\u4eba\uff0c\u5206\u4eab\u7ed9\u9700\u8981\u7684\u4eba",url:url}).catch(function(){});
  else navigator.clipboard.writeText(url).then(function(){showToast("\u94fe\u63a5\u5df2\u590d\u5236\u5230\u526a\u8d34\u677f");}).catch(function(){showToast("\u590d\u5236\u5931\u8d25");});
}
document.querySelector(".share-btn").addEventListener("click",sharePhoto);

function checkQuality(){
  var qp=document.getElementById("qPanel");if(!qp)return;
  if(!faceRes){qp.classList.add("hidden");return;}
  qp.classList.remove("hidden");
  var ring=document.getElementById("qRing"),bar=document.getElementById("qBar"),items=document.getElementById("qItems");
  var score=0,checks=[];
  if(faceRes.detection.score>0.9){score+=30;checks.push({icon:"\u2713",text:"\u4eba\u8138\u6e05\u6670",cls:"pass"});}else{checks.push({icon:"\u26a0",text:"\u4eba\u8138\u6a21\u7cca",cls:"warn"});}
  var iw=srcImg.width,ih=srcImg.height,minDim=Math.min(parseInt(sz.value.split("x")[0])*2,parseInt(sz.value.split("x")[1])*2);
  if(iw>=minDim&&ih>=minDim){score+=30;checks.push({icon:"\u2713",text:"\u5206\u8fa8\u7387\u5408\u683c",cls:"pass"});}else{checks.push({icon:"\u26a0",text:"\u5206\u8fa8\u7387\u8fc7\u4f4e",cls:"warn"});}
  if(cropRect&&cropRect.pw>0&&cropRect.ph>0){score+=20;checks.push({icon:"\u2713",text:"\u88c1\u5207\u533a\u57df\u6709\u6548",cls:"pass"});}
  var bgT=document.querySelector("input[name=bg]:checked").value;
  if(bgT!=="original"&&rmbgSess){score+=20;checks.push({icon:"\u2713",text:"\u62a0\u56fe\u6a21\u5757\u5c31\u7eea",cls:"pass"});}
  ring.textContent=Math.round(score/10)+"/10";
  ring.className="q-ring"+(score>=80?" good":score>=50?" warn":" bad");
  bar.style.width=score+"%";
  bar.className=score>=80?"good":score>=50?"warn":"bad";
  items.innerHTML="";
  checks.forEach(function(c){var d=document.createElement("div");d.className="q-item "+c.cls;d.innerHTML="<span class=icon>"+c.icon+"</span>"+c.text;items.appendChild(d);});
}
})();
'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>ID Photo Studio - 在线证件照制作 | 羊在四方</title>
  <link rel="icon" href="data:image/png;base64,{ICON_B64}"/>
  <script src="https://cdn.jsdelivr.net/npm/face-api.js@0.22.2/dist/face-api.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/ort.min.js"></script>
  <style>{CSS}</style>
</head>
<body>
<div id="ov"><div class="box">
  <h2>加载人脸检测模型</h2>
  <p>首次约 400KB，之后由浏览器缓存。</p>
  <div id="mb"><span id="mbi" style="width:5%"></span></div>
  <div id="ms">加载中…</div>
</div></div>

<div class="shell">
  <header class="topbar">
    <div class="brand"><div class="brand-logo"><img src="data:image/png;base64,{ICON_B64}" alt="logo"/></div><div class="brand-info"><span class="brand-name">ID Photo Studio</span><span class="brand-sub">在线证件照制作 · 羊在四方</span></div></div>
    <div class="top-actions"><button class="tbtn" id="tbtn">🌙</button></div>
  </header>

  <!-- Desktop grid layout: CSS grid-template-areas splits left (upload+settings) / right (preview+bottom) -->
  <div class="workspace">

    <!-- Left column: upload area -->
    <div class="panel" id="leftPanel">
      <!-- Upload: label triggers hidden file input (no CSS overlay, no JS click handler) -->
      <label class="upload-zone" id="dropZone">
        <span class="icon">📁</span>
        <div class="label">上传照片或拖拽到此处</div>
        <div class="hint">支持 JPG / PNG / WebP</div>
      </label>
      <input id="upload" type="file" accept="image/*" style="display:none"/>

      <div id="photoInfo" class="hidden" style="font-size:.73rem;color:var(--muted);margin:-.3rem 0 .5rem;padding:.35rem .55rem;background:var(--s2);border-radius:7px;display:flex;justify-content:space-between">
        <span id="photoName">—</span><span id="photoDims">—</span>
      </div>
      <button id="rstViewBtn" class="hidden" style="border:none;background:var(--s2);border:1px solid var(--border);border-radius:8px;padding:.3rem .7rem;font-size:.72rem;cursor:pointer;color:var(--text);margin-bottom:.5rem" onclick="vx=0;vy=0;vw=srcImg.width;vh=srcImg.height;needsRedraw=true">⟲ 重置视角</button>

      <hr style="border:none;border-top:1px solid var(--border);margin:.3rem 0"/>

      <div class="field"><label>证件照规格</label><select id="sz">
        <option value="295x413">一寸 25×35mm</option>
        <option value="413x579">二寸 35×49mm</option>
        <option value="413x531">小二寸/申根 35×45mm</option>
        <option value="600x600">美国签证 51×51mm</option>
        <option value="358x441">身份证 26×32mm</option>
        <option value="390x567">护照 33×48mm</option>
      </select></div>

      <div class="field"><label>背景类型</label>
        <div class="seg">
          <label><input type="radio" name="bg" value="color" checked><span>纯色背景</span></label>
          <label><input type="radio" name="bg" value="transparent"><span>透明背景</span></label>
          <label><input type="radio" name="bg" value="original"><span>保留原背景</span></label>
        </div>
      </div>

      <div class="field" id="bgcf"><label>背景颜色</label>
        <div class="swatches" id="swatches">
          <div class="swatch selected" data-color="#ffffff" style="background:#fff;border-color:#d0d0d0"><span class="check">✓</span></div>
          <div class="swatch" data-color="#d9d9d9" style="background:#d9d9d9"><span class="check">✓</span></div>
          <div class="swatch" data-color="#d92f2f" style="background:#d92f2f"><span class="check">✓</span></div>
          <div class="swatch" data-color="#2f62ff" style="background:#2f62ff"><span class="check">✓</span></div>
          <div class="swatch" data-color="#0b5840" style="background:#0b5840"><span class="check">✓</span></div>
        </div>
      </div>

      <div class="field"><div class="field-label"><label>头像占比</label><span class="val" id="hsv">42%</span></div><input id="hs" type="range" min="0.28" max="0.78" step="0.01" value="0.42" oninput="document.getElementById('hsv').textContent=Math.round(this.value*100)+'%';needsRedraw=true"/></div>
      <div class="field"><div class="field-label"><label>额头留白 <small style="font-weight:400;color:var(--muted)">（头顶到裁切框顶部的距离）</small></label><span class="val" id="tmv">35%</span></div><input id="tm" type="range" min="0.05" max="0.40" step="0.01" value="0.35" oninput="document.getElementById('tmv').textContent=Math.round(this.value*100)+'%';needsRedraw=true"/></div>

      <div class="field"><label>排版模式</label><select id="sm">
        <option value="single">单张导出</option>
        <option value="s33">五寸 3×3 拼版</option>
        <option value="s24">六寸 2×4 拼版</option>
      </select></div>

      <div class="field"><label>输出格式</label>
        <div class="seg">
          <label><input type="radio" name="fmt" value="png" checked><span>PNG</span></label>
          <label><input type="radio" name="fmt" value="jpeg"><span>JPEG</span></label>
        </div>
      </div>

      <div class="field hidden" id="qualField"><div class="field-label"><label>JPEG 质量</label><span class="val" id="qualVal">92%</span></div><input id="qual" type="range" min="10" max="100" value="92"/></div>

      <div id="qPanel" class="quality-panel hidden">
        <div class="q-header">
          <div class="q-ring" id="qRing">--</div>
          <div class="q-info">
            <div class="q-label">AI 合格检测</div>
            <div class="q-desc">基于人脸检测与图像分析</div>
            <div class="q-bar"><span id="qBar" style="width:0%"></span></div>
          </div>
        </div>
        <div class="q-items" id="qItems"></div>
      </div>

      <div id="rw" class="hidden">⚠ 请下载抠图模型 <a href="#" id="lrBtn">点击加载（约50MB）</a></div>

      <div style="display:flex;gap:.5rem;margin-top:.8rem">
        <button class="btn btn-p" id="genBtn" disabled><span class="btn-spinner"></span><span class="btn-text">✨ 生成证件照</span></button>
      </div>

      <div class="status" id="sb">等待上传图片。</div>
      <div class="prog hidden" id="pw"><span id="pb"></span></div>
    </div>

    <!-- Right column: previews + bottom actions -->
    <div class="panel" id="rightPanel">
      <div class="preview-grid">
        <section class="card"><h3>① 原图 + 人脸</h3><div class="pframe" style="position:relative"><canvas id="sc"></canvas></div><p class="note" id="fn">上传后自动检测人脸关键点。滚轮缩放，拖拽平移。</p></section>
        <section class="card"><h3>② 最终效果</h3><div class="pframe" id="rf"><canvas id="rc"></canvas></div><p class="note" id="rn">裁切合成预览。</p></section>
      </div>

      <div class="notice"><strong>🔒 纯前端处理</strong> — 所有运算在浏览器中完成，照片不上传服务器。</div>

      <div class="bottom-bar">
        <button class="btn btn-p" id="dlBtn" disabled>⬇ 下载</button>
        <button class="btn btn-s share-btn">↗ 分享</button>
      </div>

      <span id="mn" style="display:none"></span>
      <canvas id="mc" style="display:none"></canvas>
    </div>

  </div>

  <footer class="site-footer">
    <div class="author">作者：<span>羊在四方</span></div>
    <div class="tagline">纯前端证件照制作工具 · 照片不上传服务器 · 隐私安全</div>
    <div class="social-row">
      <div class="social-item">
        <img src="data:image/jpeg;base64,{QR_B64}" alt="扫码关注" loading="lazy" decoding="async"/>
        <div class="label">📱 扫码关注</div>
      </div>
      <div class="social-item">
        <img src="data:image/jpeg;base64,{DONATE_B64}" alt="赞赏支持" loading="lazy" decoding="async"/>
        <div class="label">☕ 赞赏支持</div>
      </div>
    </div>
    <div class="copyright">© 2026 羊在四方</div>
  </footer>
</div>

<script>{JS}</script>
</body>
</html>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Written {len(html)} bytes to {path}')
