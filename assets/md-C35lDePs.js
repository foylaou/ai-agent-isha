import{E as e,I as t,R as n,S as r,X as i,_ as a,_t as o,g as s,gt as c,ht as l,st as u}from"./modules/shiki-CJ0GDf1v.js";import{n as d,t as f}from"./slidev/context-foiinn_W.js";import{t as p}from"./slidev/default-Dwrhu5ya.js";import{w as m}from"./modules/unplugin-icons-B-pq-eQi.js";import{t as h}from"./gsap-Bi_c5vh2.js";var g={class:`flex items-center justify-center gap-6 mt-10`},_={class:`flex justify-center gap-2 mb-2 text-[10px] font-bold`},v={class:`relative`,style:{height:`168px`}},y={__name:`slides.md__slidev_26`,setup(y){let{$slidev:b,$nav:x,$clicksContext:S,$clicks:C,$page:w,$renderContext:T,$frontmatter:E}=d();S.setup();let D=u(),O=u(),k=u(),A=u(),j=u(`json`);return t(()=>{if(!D.value||!O.value||!k.value||!A.value)return;h.set(O.value,{opacity:0,y:8}),h.set(k.value,{opacity:1}),h.set(A.value,{opacity:0});let e=h.timeline({repeat:-1,repeatDelay:.6});e.to(D.value,{scale:1.08,duration:.3,yoyo:!0,repeat:3}),e.call(()=>j.value=`json`),e.to(O.value,{opacity:1,y:0,duration:.4}),e.to({},{duration:1.4}),e.call(()=>j.value=`xml`),e.to(k.value,{opacity:0,duration:.3}),e.to(A.value,{opacity:1,duration:.3},`<`),e.to({},{duration:1.4}),e.to(O.value,{opacity:0,y:8,duration:.3},`+=0.2`),e.set(k.value,{opacity:1}),e.set(A.value,{opacity:0})}),(t,u)=>{let d=m;return n(),a(p,o(e(l(f)(l(E),25))),{default:i(()=>[u[5]||=s(`h1`,null,`這堂課用到的多模態：OCR`,-1),s(`div`,g,[u[2]||=s(`div`,{class:`rounded-2xl border-2 p-2 text-center w-36`},[s(`img`,{src:`/ai-agent-isha/%E8%AB%8B%E5%81%87.png`,class:`w-full rounded-lg border`}),s(`div`,{class:`text-xs font-bold mt-2`},`請假單掃描檔`)],-1),u[3]||=s(`div`,{class:`text-2xl text-gray-400`},`→`,-1),s(`div`,{ref_key:`ocrBox`,ref:D,class:`rounded-2xl border-2 border-amber-300 bg-amber-50 px-6 py-6 text-center`},[r(d,{class:`w-8 h-8 mx-auto mb-2 text-amber-600`}),u[0]||=s(`div`,{class:`text-sm font-bold text-amber-700`},`OCR`,-1)],512),u[4]||=s(`div`,{class:`text-2xl text-gray-400`},`→`,-1),s(`div`,{ref_key:`resultPanel`,ref:O,class:`rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-3 w-72`},[s(`div`,_,[s(`span`,{class:c(j.value===`json`?`text-emerald-700`:`text-gray-300`)},`JSON`,2),u[1]||=s(`span`,{class:`text-gray-300`},`/`,-1),s(`span`,{class:c(j.value===`xml`?`text-emerald-700`:`text-gray-300`)},`XML`,2)]),s(`div`,v,[s(`pre`,{ref_key:`jsonBlock`,ref:k,class:`absolute inset-0 text-[9px] leading-snug bg-white rounded-lg border p-2 overflow-hidden font-mono whitespace-pre-wrap`},`{
  "姓名": "小明",
  "部門": "IT",
  "職位": "前端工程師",
  "日期": "7/30",
  "請假類型": "病假",
  "請假時間": {
    "起": "114/07/30",
    "迄": "114/08/05",
    "共": "7 天"
  },
  "請假原因": "車禍手術"
}`,512),s(`pre`,{ref_key:`xmlBlock`,ref:A,class:`absolute inset-0 text-[9px] leading-snug bg-white rounded-lg border p-2 overflow-hidden font-mono whitespace-pre-wrap`},`<請假單>
  <姓名>小明</姓名>
  <部門>IT</部門>
  <職位>前端工程師</職位>
  <日期>7/30</日期>
  <請假類型>病假</請假類型>
  <請假時間 起="114/07/30" 迄="114/08/05" 共="7天" />
  <請假原因>車禍手術</請假原因>
</請假單>`,512)])],512)]),u[6]||=s(`div`,{class:`text-center text-sm text-gray-500 mt-8`},`圖片轉成結構化資料，語言模型才能繼續處理——後面「請假代理人」實做會用到`,-1)]),_:1},16)}}};export{y as default};