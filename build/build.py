# -*- coding: utf-8 -*-
"""로마자 언어 학습 페이지 생성기.

  python3 build/build.py

build/langs/*.py 를 모두 읽어 저장소 루트에 <file> 을 쓰고,
index.html 의 언어 전환 바도 같이 맞춰 준다.
언어를 추가하려면 build/langs/ 에 파일 하나를 더 놓기만 하면 된다."""
import io, json, os, re, glob, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'langs')

CSS = '''
:root{
  --paper:#EDEEE6; --paper-2:#F8F8F3; --ink:#1A1B1D; --ink-soft:#5C5F5A; --red:#C4402E;
  --serif:"__SERIF__",'Times New Roman',serif;
  --sans:"IBM Plex Sans KR",-apple-system,'Malgun Gothic',sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
  --grid:__GRID__; --grid-line:__GL__; --grid-line-hard:__GLH__;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-weight:300;line-height:1.7;-webkit-font-smoothing:antialiased}
.wrap{max-width:980px;margin:0 auto;padding:0 20px 100px}

header{position:relative;padding:56px 0 38px;border-bottom:1px solid var(--grid-line-hard);margin-bottom:38px}
header::before{content:"";position:absolute;inset:0;
  background-image:linear-gradient(var(--grid-line) 1px,transparent 1px),linear-gradient(90deg,var(--grid-line) 1px,transparent 1px);
  background-size:34px 34px;opacity:.4;
  -webkit-mask-image:linear-gradient(to bottom,#000,transparent 92%);mask-image:linear-gradient(to bottom,#000,transparent 92%);pointer-events:none}
.langbar{position:relative;display:flex;gap:0;border:1px solid var(--grid-line-hard);border-radius:2px;overflow:hidden;max-width:430px;background:var(--paper-2);margin:0 0 28px}
.langbar a{flex:1;text-align:center;padding:9px 6px;text-decoration:none;border-right:1px solid var(--grid-line);
  font-family:var(--mono);font-size:10px;letter-spacing:.14em;color:var(--ink-soft);transition:background .15s,color .15s}
.langbar a:last-child{border-right:0}
.langbar a b{display:block;font-family:var(--sans);font-size:13px;font-weight:500;letter-spacing:0;margin-top:2px}
.langbar a:hover{background:rgba(0,0,0,.04)}
.langbar a[aria-current="page"]{background:var(--grid);color:var(--paper-2)}
.eyebrow{position:relative;font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--grid)}
h1{position:relative;font-family:var(--serif);font-weight:700;font-size:clamp(40px,7.4vw,70px);line-height:1.05;letter-spacing:-.01em;margin:14px 0 0}
h1 .jp{display:block;font-size:.44em;color:var(--grid);letter-spacing:.04em;margin-top:8px;font-style:italic}
.lede{position:relative;max-width:50ch;margin:22px 0 0;color:var(--ink-soft);font-size:15.5px}
.lede b{color:var(--ink);font-weight:500}

.maintabs{position:sticky;top:0;z-index:30;display:flex;background:var(--paper-2);
  border:1px solid var(--grid-line-hard);border-radius:2px;overflow:hidden;margin:0 0 42px;box-shadow:0 6px 18px -14px rgba(0,0,0,.5)}
.mtab{flex:1;background:transparent;border:0;border-right:1px solid var(--grid-line);padding:12px 6px 13px;cursor:pointer;
  font-family:var(--mono);font-size:10px;letter-spacing:.18em;color:var(--ink-soft);transition:background .15s,color .15s}
.mtab:last-child{border-right:0}
.mtab b{display:block;font-family:var(--sans);font-size:15px;font-weight:600;letter-spacing:0;margin-top:3px}
.mtab:hover{background:rgba(0,0,0,.04)}
.mtab[aria-selected="true"]{background:var(--grid);color:var(--paper-2)}
.mtab:focus-visible{outline:2px solid var(--red);outline-offset:-2px}

section{margin:0 0 64px}
section[hidden]{display:none}
h2{font-family:var(--serif);font-weight:700;font-size:25px;margin:0 0 6px;display:flex;align-items:baseline;gap:12px}
h2 .num{font-family:var(--mono);font-size:12px;font-weight:500;color:var(--red);letter-spacing:.1em}
.sub{color:var(--ink-soft);font-size:14px;margin:0 0 26px;max-width:74ch}
.sub b{color:var(--ink);font-weight:500}

.rowlabel{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--grid);margin:26px 0 10px;display:flex;align-items:center;gap:10px}
.rowlabel::after{content:"";flex:1;height:1px;background:var(--grid-line)}

.vrules{display:grid;grid-template-columns:repeat(auto-fit,minmax(252px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard);margin:0 0 30px}
.vrule{background:var(--paper-2);padding:15px 17px 16px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.vrule .t{font-family:var(--serif);font-size:17.5px;font-weight:700;display:flex;align-items:baseline;gap:9px}
.vrule .t i{font-style:normal;font-family:var(--mono);font-size:10px;letter-spacing:.12em;color:var(--red)}
.vrule p{margin:8px 0 0;font-size:12.8px;line-height:1.62;color:var(--ink-soft)}
.vrule p b{color:var(--ink);font-weight:500}
.vrule p em{font-style:normal;color:var(--red);font-weight:500}
.vrule .fr{font-family:var(--serif);font-size:14px;color:var(--grid);font-weight:600}

.vocab{display:grid;grid-template-columns:repeat(auto-fill,minmax(152px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.vc{background:var(--paper-2);padding:11px 13px 12px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.vc .w{font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.28;display:block}
.vc .r{font-family:var(--serif);font-size:11.5px;color:var(--grid);display:block;margin-top:3px;line-height:1.4;font-style:italic}
.vc .p{font-size:11px;color:var(--grid);display:block;line-height:1.45;margin-top:3px}
.vc .m{font-size:12.5px;font-weight:500;display:block;margin-top:6px}
.vc.warn .w{color:var(--red)}

.exs{display:grid;grid-template-columns:repeat(auto-fill,minmax(272px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard);margin-top:14px}
.exc{background:var(--paper);padding:13px 16px 14px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.vex .ej{display:block;font-family:var(--serif);font-size:16px;font-weight:500;line-height:1.5}
.vex .er{display:block;font-size:11.5px;line-height:1.5;color:var(--grid);margin-top:4px}
.vex .ek{display:block;font-size:12.6px;color:var(--ink-soft);margin-top:3px}
.exc .vex{margin-top:0}

.pairs{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.pair{background:var(--paper-2);padding:16px 17px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.pair .glyphs{font-family:var(--serif);font-size:26px;font-weight:700;line-height:1.25}
.pair .glyphs em{font-style:normal;color:var(--red)}
.pair p{margin:8px 0 0;font-size:12.8px;line-height:1.58;color:var(--ink-soft)}
.pair p b{color:var(--ink);font-weight:500}

.notes{border-top:1px solid var(--grid-line-hard)}
.note{display:grid;grid-template-columns:104px 1fr;gap:18px;padding:14px 2px;border-bottom:1px solid var(--grid-line)}
.note .g{font-family:var(--serif);font-size:21px;font-weight:700;line-height:1.2;color:var(--grid)}
.note p{margin:0;font-size:13.6px;color:var(--ink-soft)}
.note p b{color:var(--ink);font-weight:500}
.note p em{font-style:normal;color:var(--red);font-weight:500}

.vset{margin:20px 0 0}
.vsethead{margin:0 0 11px}
.vsethead .n{font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.3}
.vsethead .n i{font-style:normal;color:var(--grid);opacity:.5;font-weight:400;margin:0 3px}
.vsethead .tp{font-size:12.6px;line-height:1.6;color:var(--ink-soft);margin-top:4px;max-width:72ch}
.vsethead .tp b{color:var(--ink);font-weight:500}
.vsethead .tp em{font-style:normal;color:var(--red);font-weight:500}
.vsethead .tp .fr{font-family:var(--serif);color:var(--grid);font-weight:600}

.verbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.verb{background:var(--paper-2);padding:15px 17px 15px;position:relative;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.verb .vhead{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;padding-right:60px}
.verb .vj{font-family:var(--serif);font-size:24px;font-weight:700;line-height:1.2}
.verb .vr{font-size:12px;color:var(--grid)}
.verb .vm{font-size:14px;font-weight:500;margin-top:4px}
.vgrp{position:absolute;top:13px;right:15px;font-family:var(--mono);font-size:9px;letter-spacing:.08em;color:var(--grid);
  border:1px solid var(--grid-line);border-radius:2px;padding:1px 5px;line-height:1.6}
.vgrp.ex{color:var(--red);border-color:rgba(196,64,46,.45)}
.vconj{display:flex;margin:12px 0 0;border-top:1px solid var(--grid-line);border-bottom:1px solid var(--grid-line)}
.vconj div{flex:1;padding:7px 4px 8px;text-align:center}
.vconj div+div{border-left:1px solid var(--grid-line)}
.vconj .l{display:block;font-family:var(--mono);font-size:9px;letter-spacing:.14em;color:var(--grid);opacity:.7}
.vconj .v{font-family:var(--serif);font-size:16px;font-weight:600;line-height:1.4}
.vconj .v em{font-style:normal;color:var(--red)}
.verb .vex{margin-top:12px}

.talks{display:grid;grid-template-columns:repeat(auto-fill,minmax(272px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.talk{background:var(--paper-2);padding:15px 17px 15px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.talk .tj{font-family:var(--serif);font-size:19px;font-weight:600;line-height:1.4;display:block}
.talk .tr{display:block;font-size:11.5px;line-height:1.5;color:var(--grid);margin-top:5px}
.talk .tk{display:block;font-size:13.4px;font-weight:500;margin-top:5px}
.talk .tn{display:block;font-size:12px;line-height:1.58;color:var(--ink-soft);margin-top:9px;padding-top:9px;border-top:1px solid var(--grid-line)}
.talk .tn b{color:var(--ink);font-weight:500}
.talk .tn .fr{font-family:var(--serif);color:var(--grid);font-weight:600}
.talk.star{background:var(--paper)}
.talk.star .tj{color:var(--red)}

.conjs{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.conj{background:var(--paper-2);padding:15px 17px 15px;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard)}
.conj .chead{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.conj .cw{font-family:var(--serif);font-size:23px;font-weight:700;line-height:1.2}
.conj .cp{font-size:12.5px;color:var(--grid)}
.conj .cm{font-size:14px;font-weight:500;margin-top:4px}
.conj .cn{font-size:12.2px;line-height:1.58;color:var(--ink-soft);margin-top:9px;padding-top:9px;border-top:1px solid var(--grid-line)}
.conj .cn b{color:var(--ink);font-weight:500}
.conj .cn .fr{font-family:var(--serif);color:var(--grid);font-weight:600}
.conj .cn em{font-style:normal;color:var(--red);font-weight:500}
.conj .vex{margin-top:11px}
.conj.star{background:var(--paper)}
.conj.star .cw{color:var(--red)}

.quiz{border:1px solid var(--grid-line-hard);background:var(--paper-2)}
.quizbar{display:flex;flex-wrap:wrap;gap:8px;padding:12px 14px;border-bottom:1px solid var(--grid-line)}
.chip{background:transparent;border:1px solid var(--grid-line-hard);border-radius:2px;padding:6px 12px;
  font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--ink-soft);cursor:pointer;transition:.15s}
.chip:hover{background:rgba(0,0,0,.04)}
.chip[aria-pressed="true"]{background:var(--grid);border-color:var(--grid);color:var(--paper-2)}
.chip:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.stage{padding:34px 20px 30px;text-align:center}
.square{position:relative;width:220px;height:170px;margin:0 auto;border:1px solid var(--grid-line-hard);background:var(--paper);
  display:flex;align-items:center;justify-content:center}
.square::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:1px dashed var(--grid-line)}
.square::after{content:"";position:absolute;top:0;bottom:0;left:50%;border-left:1px dashed var(--grid-line)}
#qWord{font-family:var(--serif);font-weight:700;font-size:32px;line-height:1.25;position:relative;z-index:1;padding:0 14px;word-break:break-word}
#qTag{position:absolute;bottom:7px;left:0;right:0;z-index:1;font-family:var(--mono);font-size:9px;letter-spacing:.14em;color:var(--grid);opacity:.55}
#mark{position:absolute;inset:0;z-index:2;pointer-events:none}
#mark path,#mark circle{fill:none;stroke:var(--red);stroke-width:5;stroke-linecap:round;opacity:.9}
.choices{margin:28px auto 0;max-width:460px;display:grid;grid-template-columns:repeat(2,1fr);gap:0;
  border-top:1px solid var(--grid-line-hard);border-left:1px solid var(--grid-line-hard)}
.choice{background:var(--paper-2);border:0;border-right:1px solid var(--grid-line-hard);border-bottom:1px solid var(--grid-line-hard);
  padding:14px 8px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:3px;transition:background .12s;position:relative}
.choice .cr{font-size:17px;font-weight:500;color:var(--ink)}
.choice .ck{font-size:11.5px;color:var(--ink-soft)}
.choice .cn{position:absolute;top:5px;left:7px;font-family:var(--mono);font-size:9px;color:var(--grid);opacity:.45}
.choice:hover:not(:disabled){background:rgba(0,0,0,.045)}
.choice:focus-visible{outline:2px solid var(--red);outline-offset:-2px}
.choice:disabled{cursor:default}
.choice.ok{background:var(--grid)}
.choice.ok .cr,.choice.ok .ck,.choice.ok .cn{color:var(--paper-2);opacity:1}
.choice.no{background:rgba(196,64,46,.12)}
.choice.no .cr{color:var(--red);text-decoration:line-through}
.choice.dim{opacity:.4}
.verdict{min-height:26px;margin:16px 0 0;font-size:14px;letter-spacing:.02em}
.verdict.ok{color:var(--grid)}
.verdict.no{color:var(--red)}
.score{display:flex;justify-content:center;gap:26px;padding:13px;border-top:1px solid var(--grid-line);
  font-family:var(--mono);font-size:11.5px;color:var(--ink-soft);letter-spacing:.08em;flex-wrap:wrap}
.score b{color:var(--ink);font-weight:500}

footer{border-top:1px solid var(--grid-line-hard);padding-top:22px;font-size:12.5px;color:var(--ink-soft)}
footer b{color:var(--ink);font-weight:500}

@media (max-width:640px){
  .note{grid-template-columns:78px 1fr;gap:12px}
  .square{width:100%;max-width:280px;height:150px}
  #qWord{font-size:26px}
  .langbar{max-width:none}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
'''

JS = r'''
const $ = s=>document.querySelector(s);
const DATA = __DATA__;

/* ── 메인 탭 ── */
const TABS = [
  {id:'sound', en:'SOUND', jp:'소리'},
  {id:'drill', en:'DRILL', jp:'연습'},
  {id:'word',  en:'WORDS', jp:'단어'},
  {id:'verb',  en:'VERBS', jp:'동사'},
  {id:'talk',  en:'TALK',  jp:'회화'}
];
let tab='sound';
const mtabs=$('#maintabs');
TABS.forEach(t=>{
  const b=document.createElement('button');
  b.className='mtab';b.setAttribute('role','tab');b.setAttribute('aria-selected',t.id===tab);
  b.innerHTML=`${t.en}<b>${t.jp}</b>`;
  b.onclick=()=>{tab=t.id;applyTab();window.scrollTo(0,0)};
  mtabs.appendChild(b);
});
function applyTab(){
  document.querySelectorAll('section[data-tab]').forEach(sec=>{sec.hidden = sec.dataset.tab!==tab});
  [...mtabs.children].forEach((c,i)=>c.setAttribute('aria-selected',TABS[i].id===tab));
}

/* ── 공통 렌더러 ── */
const rules = list => list.map(r=>
  `<div class="vrule"><div class="t"><i>${r[0]}</i>${r[1]}</div><p>${r[2]}</p></div>`).join('');

const exBlock = e =>
  `<div class="vex"><span class="ej">${e[0]}</span><span class="er">${e[1]}</span><span class="ek">${e[2]}</span></div>`;

function vocab(groups){
  return groups.map(g=>{
    const cells=g.items.map(w=>
      `<div class="vc${w[4]?' warn':''}"><span class="w">${w[0]}</span>${w[1]?`<span class="r">${w[1]}</span>`:''}
        <span class="p">${w[2]}</span><span class="m">${w[3]}</span></div>`).join('');
    const exs=(g.ex||[]).map(e=>`<div class="exc">${exBlock(e)}</div>`).join('');
    return `<div class="rowlabel">${g.label}</div><div class="vocab">${cells}</div>`
      + (exs?`<div class="exs">${exs}</div>`:'');
  }).join('');
}

function verbs(sets){
  return sets.map(st=>{
    const cards=st.items.map(v=>{
      const badge = v[9] ? `<span class="vgrp ex">${v[3]} · 불규칙</span>` : `<span class="vgrp">${v[3]}</span>`;
      return `<div class="verb">${badge}
        <div class="vhead"><span class="vj">${v[0]}</span><span class="vr">${v[1]}</span></div>
        <div class="vm">${v[2]}</div>
        <div class="vconj">
          <div><span class="l">${DATA.p1}</span><span class="v">${v[4]}</span></div>
          <div><span class="l">${DATA.p2}</span><span class="v">${v[5]}</span></div>
        </div>${exBlock([v[6],v[7],v[8]])}</div>`;
    }).join('');
    return `<div class="vset"><div class="vsethead"><div class="n">${st.n}</div><div class="tp">${st.tip}</div></div>
      <div class="verbs">${cards}</div></div>`;
  }).join('');
}

function talks(groups){
  return groups.map(g=>{
    const cards=g.items.map(t=>
      `<div class="talk${t[4]?' star':''}"><span class="tj">${t[0]}</span><span class="tr">${t[1]}</span>
        <span class="tk">${t[2]}</span>${t[3]?`<span class="tn">${t[3]}</span>`:''}</div>`).join('');
    return `<div class="rowlabel">${g.label}</div><div class="talks">${cards}</div>`;
  }).join('');
}

function conjs(groups){
  return groups.map(g=>{
    const cards=g.items.map(c=>
      `<div class="conj${c[7]?' star':''}"><div class="chead"><span class="cw">${c[0]}</span><span class="cp">${c[1]}</span></div>
        <div class="cm">${c[2]}</div><div class="cn">${c[3]}</div>${exBlock([c[4],c[5],c[6]])}</div>`).join('');
    return `<div class="rowlabel">${g.label}</div><div class="conjs">${cards}</div>`;
  }).join('');
}

$('#sRules').innerHTML = rules(DATA.soundRules);
$('#sList').innerHTML  = vocab(DATA.soundGroups);
$('#pairs').innerHTML  = DATA.pairs.map(p=>
  `<div class="pair"><div class="glyphs">${p[0]}</div><p>${p[1]}</p></div>`).join('');
$('#notes').innerHTML  = DATA.notes.map(n=>
  `<div class="note"><div class="g">${n[0]}</div><p>${n[1]}</p></div>`).join('');
$('#nRules').innerHTML = rules(DATA.numRules);   $('#nList').innerHTML = vocab(DATA.numGroups);
$('#tRules').innerHTML = rules(DATA.timeRules);  $('#tList').innerHTML = vocab(DATA.timeGroups);
$('#plRules').innerHTML= rules(DATA.placeRules); $('#plList').innerHTML= vocab(DATA.placeGroups);
$('#vRules').innerHTML = rules(DATA.verbRules);  $('#vList').innerHTML = verbs(DATA.verbSets);
$('#kRules').innerHTML = rules(DATA.talkRules);  $('#kList').innerHTML = talks(DATA.talkGroups);
$('#cRules').innerHTML = rules(DATA.conjRules);  $('#cList').innerHTML = conjs(DATA.conjGroups);

/* ── 퀴즈 ── */
const POOLS = DATA.quiz.map((q,i)=>({id:i,label:q.label})).concat([{id:'all',label:'전체'}]);
let active=new Set([0]);
const bar=$('#quizbar');
POOLS.forEach(p=>{
  const b=document.createElement('button');
  b.className='chip';b.textContent=p.label;b.setAttribute('aria-pressed',p.id===0);
  b.onclick=()=>{
    if(p.id==='all') active=new Set(DATA.quiz.map((_,i)=>i));
    else if(active.has(p.id)&&active.size>1) active.delete(p.id);
    else active.add(p.id);
    [...bar.children].forEach((c,i)=>{
      const pid=POOLS[i].id;
      c.setAttribute('aria-pressed', pid==='all'?false:active.has(pid));
    });
    build();
  };
  bar.appendChild(b);
});

let queue=[],cur=null,ok=0,no=0,answered=false,pool=[];
function build(){
  const list=[];
  DATA.quiz.forEach((q,i)=>{ if(active.has(i)) q.items.forEach(it=>list.push({w:it[0],r:it[1],m:it[2],tag:q.label})); });
  const uniq=new Map();
  list.forEach(x=>uniq.set(x.r,{r:x.r,m:x.m}));
  if(uniq.size<4) DATA.quiz.forEach(q=>q.items.forEach(it=>uniq.set(it[1],{r:it[1],m:it[2]})));
  pool=[...uniq.values()];
  queue=list.sort(()=>Math.random()-.5);
  ok=0;no=0;next();
}
function options(c){
  const wrong=pool.filter(x=>x.r!==c.r).sort(()=>Math.random()-.5).slice(0,3);
  return [{r:c.r,m:c.m},...wrong].sort(()=>Math.random()-.5);
}
function renderChoices(){
  const box=$('#choices');box.innerHTML='';
  if(!cur) return;
  options(cur).forEach((o,i)=>{
    const b=document.createElement('button');
    b.className='choice';
    b.innerHTML=`<span class="cn">${i+1}</span><span class="cr">${o.r}</span><span class="ck">${o.m}</span>`;
    b.onclick=()=>pick(o.r,b);
    box.appendChild(b);
  });
}
function next(){
  answered=false;$('#mark').innerHTML='';
  $('#verdict').textContent='';$('#verdict').className='verdict';
  if(!queue.length){
    cur=null;$('#qWord').textContent='○';$('#qTag').textContent='';$('#choices').innerHTML='';
    $('#verdict').textContent='끝. 칩을 눌러 다음 범위로.';$('#verdict').className='verdict ok';
  }else{
    cur=queue[0];$('#qWord').textContent=cur.w;$('#qTag').textContent=cur.tag;renderChoices();
  }
  score();
}
function score(){
  $('#sOk').textContent=ok;$('#sNo').textContent=no;$('#sLeft').textContent=queue.length;
  const t=ok+no;$('#sPct').textContent=t?Math.round(ok/t*100)+'%':'—';
}
function maru(){$('#mark').innerHTML='<circle cx="50%" cy="50%" r="58" stroke-dasharray="365" stroke-dashoffset="365"><animate attributeName="stroke-dashoffset" from="365" to="0" dur=".38s" fill="freeze"/></circle>'}
function batsu(){$('#mark').innerHTML='<path d="M30 30 L110 110" stroke-dasharray="113" stroke-dashoffset="113"><animate attributeName="stroke-dashoffset" from="113" to="0" dur=".2s" fill="freeze"/></path><path d="M110 30 L30 110" stroke-dasharray="113" stroke-dashoffset="113"><animate attributeName="stroke-dashoffset" from="113" to="0" dur=".2s" begin=".16s" fill="freeze"/></path>'}
function pick(r,btn){
  if(!cur||answered) return;
  answered=true;
  const good=r===cur.r;
  [...$('#choices').children].forEach(b=>{
    b.disabled=true;
    const v=b.querySelector('.cr').textContent;
    if(v===cur.r) b.classList.add('ok');
    else if(b===btn) b.classList.add('no');
    else b.classList.add('dim');
  });
  queue.shift();
  if(good){ok++;maru();$('#verdict').textContent='○  '+cur.m;$('#verdict').className='verdict ok';setTimeout(next,640);}
  else{no++;batsu();
    $('#verdict').innerHTML=`×  ${cur.w} = <b>${cur.r}</b> · ${cur.m} — 아무 키나 눌러 계속`;
    $('#verdict').className='verdict no';
    queue.splice(Math.min(3,queue.length),0,cur);
    setTimeout(()=>{if(answered) next()},1800);}
  score();
}
document.addEventListener('keydown',e=>{
  if(answered){ if(e.key.length===1||e.key==='Enter'){e.preventDefault();next()} return; }
  const n=parseInt(e.key,10);
  if(n>=1&&n<=4){const b=$('#choices').children[n-1];if(b){e.preventDefault();b.click()}}
});
build();
applyTab();
'''

SECTIONS = [
 ('sound','01','__S1__','__S1SUB__','<div class="vrules" id="sRules"></div><div id="sList"></div>'),
 ('sound','02','헷갈리는 짝','따로 외우면 계속 섞입니다. 반드시 나란히 놓고 차이 한 가지만 잡으세요.','<div class="pairs" id="pairs"></div>'),
 ('sound','03','소리 노트','글자는 맞게 읽어도 소리가 틀리는 지점, 그리고 한국인이 특히 어려워하는 자리입니다.','<div class="notes" id="notes"></div>'),
 ('drill','04','꺼내기 연습','단어를 보고 맞는 발음을 고르세요. 키보드 <b>1~4</b>로도 됩니다. 틀린 것은 뒤쪽에 다시 섞여 들어옵니다.',
  '''<div class="quiz">
    <div class="quizbar" id="quizbar"></div>
    <div class="stage">
      <div class="square"><span id="qWord"></span><span id="qTag"></span><svg id="mark" viewBox="0 0 140 140" aria-hidden="true"></svg></div>
      <div class="choices" id="choices" role="group" aria-label="보기"></div>
      <p class="verdict" id="verdict" role="status" aria-live="polite"></p>
    </div>
    <div class="score"><span>맞음 <b id="sOk">0</b></span><span>틀림 <b id="sNo">0</b></span><span>남음 <b id="sLeft">0</b></span><span>정답률 <b id="sPct">—</b></span></div>
  </div>'''),
 ('word','05','숫자와 값','가격, 인원, 개수. 숫자를 못 읽으면 아무것도 안 됩니다.','<div class="vrules" id="nRules"></div><div id="nList"></div>'),
 ('word','06','때 — 시간 · 날짜 · 계절','몇 시에 열고 며칠에 돌아가는지. 예약과 일정은 전부 여기서 나옵니다.','<div class="vrules" id="tRules"></div><div id="tList"></div>'),
 ('word','07','장소 — 층 · 방향 · 시설','「몇 층이에요?」와 「직진해서 오른쪽」. 이 둘이면 건물 안에서도 길 위에서도 헤매지 않습니다.','<div class="vrules" id="plRules"></div><div id="plList"></div>'),
 ('verb','08','__S8__','__S8SUB__','<div class="vrules" id="vRules"></div><div id="vList"></div>'),
 ('talk','09','말이 트이는 순간','단어를 외웠으면 이제 말을 걸 차례입니다. 빨간 문장은 <b>가장 효율 좋은 것</b> — 이것만 골라도 됩니다.','<div class="vrules" id="kRules"></div><div id="kList"></div>'),
 ('talk','10','문장 잇는 말','<b>「그리고 · 그런데 · 하지만 · 그래서」</b>에 해당하는 말과, 말이 막혔을 때 시간을 버는 말.','<div class="vrules" id="cRules"></div><div id="cList"></div>'),
]

LANGBAR = [('index.html','JAPANESE','일본어')]  # main() 에서 언어 파일을 읽어 채운다

def build(L):
    css = CSS.replace('__SERIF__',L['serif']).replace('__GRID__',L['grid']).replace('__GL__',L['gl']).replace('__GLH__',L['glh'])
    secs=[]
    for tab,num,title,sub,body in SECTIONS:
        title = title.replace('__S1__',L['s1']).replace('__S8__',L['s8'])
        sub = sub.replace('__S1SUB__',L['s1sub']).replace('__S8SUB__',L['s8sub'])
        secs.append(f'''<section data-tab="{tab}">
  <h2><span class="num">{num}</span>{title}</h2>
  <p class="sub">{sub}</p>
  {body}
</section>''')
    bar=''.join(
      f'<a href="{h}"{" aria-current=\"page\"" if h==L["file"] else ""}>{en}<b>{kr}</b></a>'
      for h,en,kr in LANGBAR)
    html=f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{L['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={L['serif'].replace(' ','+')}:ital,wght@0,500;0,600;0,700;1,500&family=IBM+Plex+Sans+KR:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="langbar">{bar}</div>
  <div class="eyebrow">{L['eyebrow']}</div>
  <h1>{L['h1']}<span class="jp">{L['h1sub']}</span></h1>
  <p class="lede">{L['lede']}</p>
</header>

<nav class="maintabs" id="maintabs" role="tablist" aria-label="학습 영역"></nav>

{chr(10).join(secs)}

<footer>{L['foot']}</footer>

</div>
<script>
{JS.replace('__DATA__', json.dumps(L['data'], ensure_ascii=False))}
</script>
</body>
</html>
'''
    io.open(os.path.join(ROOT, L['file']),'w',encoding='utf-8').write(html)
    print('wrote', L['file'], len(html))


def load_langs():
    """build/langs/*.py 에서 LANG 딕셔너리를 모아 order 순으로 돌려준다."""
    out = []
    for path in sorted(glob.glob(os.path.join(LANGS_DIR, '*.py'))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith('_'):
            continue
        spec = importlib.util.spec_from_file_location('lang_' + name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.LANG)
    return sorted(out, key=lambda l: l.get('order', 99))


def sync_index(langs):
    """index.html(일본어)의 언어 전환 바를 langs 목록에 맞춘다."""
    p = os.path.join(ROOT, 'index.html')
    s = io.open(p, encoding='utf-8').read()
    links = ['    <a href="index.html" aria-current="page">JAPANESE<b>일본어</b></a>']
    for L in langs:
        en, kr = L['nav']
        links.append('    <a href="%s">%s<b>%s</b></a>' % (L['file'], en, kr))
    block = '<div class="langbar">\n' + '\n'.join(links) + '\n  </div>'
    new, n = re.subn(r'<div class="langbar">.*?</div>', lambda m: block, s, count=1, flags=re.S)
    if n != 1:
        print('!! index.html 에 langbar 블록이 없어 건너뜀')
        return
    if new != s:
        io.open(p, 'w', encoding='utf-8').write(new)
        print('synced index.html langbar')
    else:
        print('index.html langbar 그대로')


def main():
    langs = load_langs()
    global LANGBAR
    LANGBAR = [('index.html', 'JAPANESE', '일본어')] + [(L['file'],) + tuple(L['nav']) for L in langs]
    for L in langs:
        build(L)
    sync_index(langs)


if __name__ == '__main__':
    main()
