---
theme: default
title: 介紹地端運作生成式 AI 實做
info: |
  6 小時實作課程
  Part 1 上午場：認識 AI｜Part 2 下午場：使用 AI
class: text-center
transition: slide-left
mdc: true
---

# 介紹地端運作生成式 AI 實做

<div class="text-lg opacity-70 mt-4">6 小時實作課程</div>

<div class="text-sm opacity-50 mt-8">
Part 1 上午場：認識 AI｜Part 2 下午場：使用 AI
</div>

---
layout: default
---

# 什麼是「基礎模型」？

<div class="text-sm text-gray-500 mb-2">生成式 AI，不只是語言生成</div>

<div class="flex items-center justify-center gap-3 mt-10">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 p-4 w-48">
    <div class="text-blue-700 font-bold text-center mb-3 text-sm">資料（Data）</div>
    <div class="space-y-1.5">
      <div class="bg-white rounded-lg border px-3 py-1.5 flex items-center gap-2 text-xs"><lucide-file-text class="w-3.5 h-3.5 text-blue-500 shrink-0" />文字</div>
      <div class="bg-white rounded-lg border px-3 py-1.5 flex items-center gap-2 text-xs"><lucide-image class="w-3.5 h-3.5 text-blue-500 shrink-0" />圖像</div>
      <div class="bg-white rounded-lg border px-3 py-1.5 flex items-center gap-2 text-xs"><lucide-mic class="w-3.5 h-3.5 text-blue-500 shrink-0" />語音</div>
      <div class="bg-white rounded-lg border px-3 py-1.5 flex items-center gap-2 text-xs"><lucide-database class="w-3.5 h-3.5 text-blue-500 shrink-0" />結構化資料</div>
      <div class="bg-white rounded-lg border px-3 py-1.5 flex items-center gap-2 text-xs"><lucide-box class="w-3.5 h-3.5 text-blue-500 shrink-0" />3D 訊號</div>
    </div>
  </div>

  <div class="flex flex-col items-center gap-1">
    <div class="text-xs font-bold text-gray-500">Training</div>
    <div class="text-2xl text-gray-400">→</div>
  </div>

  <div class="rounded-2xl border-2 border-gray-300 bg-white p-5 w-40 flex flex-col items-center text-center">
    <lucide-layers class="w-9 h-9 text-gray-700 mb-2" />
    <div class="font-bold text-sm leading-tight">Foundation<br/>Model</div>
    <div class="text-[10px] text-gray-400 mt-2 leading-snug">同一顆模型<br/>吃各種模態資料</div>
  </div>

  <div class="flex flex-col items-center gap-1">
    <div class="text-xs font-bold text-gray-500">Adaptation</div>
    <div class="text-2xl text-gray-400">→</div>
  </div>

  <div class="rounded-2xl border-2 border-amber-300 bg-amber-50 p-4 w-52">
    <div class="text-amber-700 font-bold text-center mb-3 text-sm">任務（Tasks）</div>
    <div class="space-y-1.5 text-xs">
      <div class="bg-white rounded-lg border px-3 py-1.5">問答 Question Answering</div>
      <div class="bg-white rounded-lg border px-3 py-1.5">情感分析 Sentiment Analysis</div>
      <div class="bg-white rounded-lg border px-3 py-1.5">資訊擷取 Info Extraction</div>
      <div class="bg-white rounded-lg border px-3 py-1.5">圖像描述 Image Captioning</div>
      <div class="bg-white rounded-lg border px-3 py-1.5">物件辨識 Object Recognition</div>
      <div class="bg-white rounded-lg border px-3 py-1.5">指令遵循 Instruction Following</div>
    </div>
  </div>
</div>

---
layout: default
---

# 例子一：翻譯模型

<div class="text-sm text-gray-500 mb-2">同一顆模型，adapt 到「翻譯」這個任務</div>

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const inBubble = ref()
const modelBox1 = ref()
const outEn = ref()
const outJa = ref()
const outKo = ref()

onMounted(() => {
  const outs = [outEn.value, outJa.value, outKo.value]
  if (!inBubble.value || !modelBox1.value || outs.some(e => !e)) return

  gsap.set(inBubble.value, { opacity: 0, y: 10 })
  gsap.set(outs, { opacity: 0, x: -10 })

  gsap.timeline({ repeat: -1, repeatDelay: 1 })
    .to(inBubble.value, { opacity: 1, y: 0, duration: 0.4 })
    .to(modelBox1.value, { scale: 1.06, duration: 0.25, yoyo: true, repeat: 3 }, '+=0.2')
    .to(outs, { opacity: 1, x: 0, duration: 0.4, stagger: 0.15 }, '+=0.1')
    .to({}, { duration: 1.3 })
    .to([inBubble.value, ...outs], { opacity: 0, duration: 0.3 }, '+=0.2')
    .set(inBubble.value, { y: 10 })
    .set(outs, { x: -10 })
})
</script>

<div class="flex items-center justify-center gap-6 mt-16">
  <div ref="inBubble" class="rounded-2xl bg-blue-50 border-2 border-blue-300 px-6 py-5 text-center w-32">
    <div class="text-xs text-gray-400 mb-1">輸入</div>
    <div class="text-lg font-bold">你好</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div ref="modelBox1" class="rounded-2xl bg-white border-2 border-gray-300 px-7 py-6 text-center">
    <lucide-languages class="w-8 h-8 mx-auto mb-2 text-gray-700" />
    <div class="font-bold text-sm">翻譯模型</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div class="flex flex-col gap-3">
    <div ref="outEn" class="rounded-xl bg-emerald-50 border-2 border-emerald-300 px-4 py-2 flex items-center gap-3 text-sm">
      <span class="text-[10px] font-bold text-emerald-600 w-6">EN</span><span class="font-bold">Hello</span>
    </div>
    <div ref="outJa" class="rounded-xl bg-emerald-50 border-2 border-emerald-300 px-4 py-2 flex items-center gap-3 text-sm">
      <span class="text-[10px] font-bold text-emerald-600 w-6">JA</span><span class="font-bold">こんにちは</span>
    </div>
    <div ref="outKo" class="rounded-xl bg-emerald-50 border-2 border-emerald-300 px-4 py-2 flex items-center gap-3 text-sm">
      <span class="text-[10px] font-bold text-emerald-600 w-6">KO</span><span class="font-bold">안녕하세요</span>
    </div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">同一句輸入，adapt 到不同語言的輸出——這就是「任務調適」</div>

---
layout: default
---

# 例子二：文字生成影像

<div class="text-sm text-gray-500 mb-2">同一種能力，adapt 到「生成圖像」這個任務</div>

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const promptCard = ref()
const modelBox2 = ref()
const spinner = ref()
const resultImg = ref()

onMounted(() => {
  if (!promptCard.value || !modelBox2.value || !spinner.value || !resultImg.value) return

  gsap.set(promptCard.value, { opacity: 0, y: 10 })
  gsap.set(spinner.value, { opacity: 0 })
  gsap.set(resultImg.value, { opacity: 0 })

  gsap.timeline({ repeat: -1, repeatDelay: 1 })
    .to(promptCard.value, { opacity: 1, y: 0, duration: 0.4 })
    .to(modelBox2.value, { scale: 1.06, duration: 0.25, yoyo: true, repeat: 3 }, '+=0.2')
    .to(spinner.value, { opacity: 1, duration: 0.3 }, '+=0.1')
    .to({}, { duration: 1.2 })
    .to(spinner.value, { opacity: 0, duration: 0.3 })
    .to(resultImg.value, { opacity: 1, duration: 0.5 }, '<')
    .to({}, { duration: 1.4 })
    .to([promptCard.value, resultImg.value], { opacity: 0, duration: 0.3 }, '+=0.2')
    .set(promptCard.value, { y: 10 })
    .set(spinner.value, { opacity: 0 })
})
</script>

<div class="flex items-center justify-center gap-6 mt-14">
  <div ref="promptCard" class="rounded-2xl bg-blue-50 border-2 border-blue-300 px-5 py-4 w-56 text-sm leading-snug">
    <div class="text-xs text-gray-400 mb-1">Prompt</div>
    給我一隻布偶貓，躺在沙發上慵懶睡覺的樣子
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div ref="modelBox2" class="rounded-2xl bg-white border-2 border-gray-300 px-6 py-6 text-center">
    <lucide-image class="w-8 h-8 mx-auto mb-2 text-gray-700" />
    <div class="font-bold text-sm">文字生成影像模型</div>
    <div class="text-[10px] text-gray-400 mt-1">Stable Diffusion／Nano Banana</div>
  </div>
  <div class="text-3xl text-gray-400">→</div>
  <div class="relative w-36 h-36 rounded-2xl border-2 border-amber-300 bg-amber-50 flex items-center justify-center overflow-hidden">
    <div ref="spinner" class="loading-spinner"></div>
    <img ref="resultImg" src="/cat.jpeg" class="absolute inset-0 w-full h-full object-cover" />
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">
輸入變成一句「文字描述」、輸出變成一張「圖片」——模型沒換，換的是任務
</div>
<div class="text-center text-xs text-gray-400 italic mt-3">
→ 後面會看到：Agent 也是同一顆基礎模型，被 adapt 成「任務規劃」的能力
</div>

<style>
.loading-spinner {
  width: 32px;
  height: 32px;
  border: 4px solid #fcd34d;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>

---
layout: default
---

# 生成式 AI 概論

<div class="text-sm text-gray-500 mb-2">從一篇論文，到全民都在用</div>

<div class="flex items-center justify-between mt-14 px-4">

  <div class="flex flex-col items-center gap-2 w-40">
    <div class="w-16 h-16 rounded-full bg-blue-500 text-white flex items-center justify-center"><lucide-file-text class="w-7 h-7" /></div>
    <div class="text-xs font-bold text-gray-400">2017</div>
    <div class="text-sm font-bold text-center leading-tight">Attention Is<br/>All You Need</div>
    <div class="text-[10px] text-gray-500 text-center">Google · Transformer 架構誕生</div>
  </div>

  <div class="flex-1 border-t-2 border-dashed border-gray-300 mx-1 mb-16"></div>

  <div class="flex flex-col items-center gap-2 w-40">
    <div class="w-16 h-16 rounded-full bg-emerald-500 text-white flex items-center justify-center"><lucide-message-square class="w-7 h-7" /></div>
    <div class="text-xs font-bold text-gray-400">2022</div>
    <div class="text-sm font-bold text-center leading-tight">ChatGPT 問世</div>
    <div class="text-[10px] text-gray-500 text-center">OpenAI · 生成式 AI 走入大眾</div>
  </div>

  <div class="flex-1 border-t-2 border-dashed border-gray-300 mx-1 mb-16"></div>

  <div class="flex flex-col items-center gap-2 w-40">
    <div class="w-16 h-16 rounded-full bg-amber-500 text-white flex items-center justify-center"><lucide-globe class="w-7 h-7" /></div>
    <div class="text-xs font-bold text-gray-400">2023 - 2026</div>
    <div class="text-sm font-bold text-center leading-tight">百家爭鳴</div>
    <div class="text-[10px] text-gray-500 text-center">開源與閉源模型並起</div>
  </div>

</div>

<div class="text-center text-xs text-gray-400 italic mt-10">
→ 這條線索到本課程後段還會再出現：從 Transformer 到 Google ADK
</div>

---
layout: default
---

# 2026 AI 模型地圖

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 p-6">
    <div class="text-blue-700 font-bold text-center mb-4">閉源前沿模型</div>
    <div class="flex flex-wrap gap-2 justify-center">
      <span class="bg-white rounded-full border px-3 py-1 text-sm">ChatGPT / GPT 系列（OpenAI）</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Claude 系列（Anthropic）</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Gemini 系列（Google）</span>
    </div>
    <div class="text-xs text-gray-500 mt-4 text-center">透過 API／訂閱使用，模型本身不公開</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6">
    <div class="text-emerald-700 font-bold text-center mb-4">開源／開權重模型</div>
    <div class="flex flex-wrap gap-2 justify-center">
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Llama（Meta）</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Gemma（Google）</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Qwen（Alibaba）</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">DeepSeek</span>
      <span class="bg-white rounded-full border px-3 py-1 text-sm">Mistral</span>
    </div>
    <div class="text-xs text-gray-500 mt-4 text-center">可下載、可地端部署、部分可商用</div>
  </div>
</div>

---
layout: default
---

# 授權方式的差異

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 p-6">
    <div class="font-bold text-lg mb-3">閉源</div>
    <ul class="text-sm text-gray-600 space-y-2 list-disc pl-4">
      <li>依 API 呼叫次數／token 用量計費</li>
      <li>模型跑在對方雲端，資料會經過第三方</li>
      <li>無法自行修改或離線使用</li>
    </ul>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6">
    <div class="font-bold text-lg mb-3 text-emerald-700">開源</div>
    <ul class="text-sm text-gray-600 space-y-2 list-disc pl-4">
      <li>下載模型權重，自行部署</li>
      <li>依授權（Apache 2.0／MIT 等）可能可自由商用</li>
      <li>資料留在自己的機器上</li>
    </ul>
  </div>
</div>

---
layout: default
---

# 這一年最大的轉變：開源追上來了

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="mb-3 flex justify-center"><lucide-trending-up class="w-8 h-8 text-blue-500" /></div>
    <div class="font-bold mb-2">效能追近</div>
    <div class="text-sm text-gray-600">開源模型在許多任務上逐漸逼近閉源前沿模型</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="mb-3 flex justify-center"><lucide-zap class="w-8 h-8 text-amber-500" /></div>
    <div class="font-bold mb-2">量化技術成熟</div>
    <div class="text-sm text-gray-600">大型模型經量化後，能塞進一般消費級顯卡</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="mb-3 flex justify-center"><lucide-wrench class="w-8 h-8 text-emerald-500" /></div>
    <div class="font-bold mb-2">地端生態成熟</div>
    <div class="text-sm text-gray-600">Ollama、llama.cpp 等工具讓部署變得簡單</div>
  </div>
</div>

---
layout: default
---

# 為什麼要地端跑？

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-blue-500 text-white flex items-center justify-center mb-4"><lucide-lock class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">隱私與資料主權</div>
    <div class="text-sm text-gray-600">敏感資料不需要送到第三方雲端</div>
  </div>
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-emerald-500 text-white flex items-center justify-center mb-4"><lucide-wifi-off class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">離線可用</div>
    <div class="text-sm text-gray-600">沒有網路也能運作，不依賴外部服務穩定性</div>
  </div>
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-amber-500 text-white flex items-center justify-center mb-4"><lucide-dollar-sign class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">成本可控</div>
    <div class="text-sm text-gray-600">用量越大，地端硬體的邊際成本越划算</div>
  </div>
</div>

---
layout: default
---

# GPU 規格概念：VRAM 比算力更重要

<div class="text-center text-base mt-8 mb-10">
  <b class="text-amber-600">跑得動、跑不動，關鍵在顯示記憶體（VRAM）容量</b>，不是計算速度
</div>

<div class="grid grid-cols-3 gap-6">
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="text-xs text-gray-400 mb-2">入門</div>
    <div class="w-full h-3 bg-blue-100 rounded-full mb-3"><div class="w-1/3 h-3 bg-blue-400 rounded-full"></div></div>
    <div class="text-sm text-gray-600">可跑小型模型（約 7B 以下）</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="text-xs text-gray-400 mb-2">進階</div>
    <div class="w-full h-3 bg-emerald-100 rounded-full mb-3"><div class="w-2/3 h-3 bg-emerald-400 rounded-full"></div></div>
    <div class="text-sm text-gray-600">可跑中型模型（約 13～30B）</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <div class="text-xs text-gray-400 mb-2">高階</div>
    <div class="w-full h-3 bg-amber-100 rounded-full mb-3"><div class="w-full h-3 bg-amber-400 rounded-full"></div></div>
    <div class="text-sm text-gray-600">可跑大型／多顯卡模型（70B 以上）</div>
  </div>
</div>

<div class="text-center text-xs text-gray-400 mt-6">＊實際型號與規格，第 3 節 Ollama 部署再詳細介紹</div>

---
layout: default
---

# 什麼是 Token 與 Context Window？

<div class="mt-10">
  <div class="text-sm text-gray-600 mb-3">一段文字會先被拆成一個個 <b class="text-blue-600">token</b>：</div>
  <div class="flex flex-wrap gap-2 mb-8">
    <span class="bg-blue-100 rounded px-2 py-1 text-sm">生成式</span>
    <span class="bg-blue-100 rounded px-2 py-1 text-sm">AI</span>
    <span class="bg-blue-100 rounded px-2 py-1 text-sm">可以</span>
    <span class="bg-blue-100 rounded px-2 py-1 text-sm">地端</span>
    <span class="bg-blue-100 rounded px-2 py-1 text-sm">運作</span>
  </div>

  <div class="text-sm text-gray-600 mb-3">模型一次能「記住」多少 token，就是它的 <b class="text-emerald-600">context window（上下文視窗）</b>：</div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-4 flex items-center gap-2 flex-wrap">
    <span class="bg-white rounded px-2 py-1 text-xs">token</span>
    <span class="bg-white rounded px-2 py-1 text-xs">token</span>
    <span class="bg-white rounded px-2 py-1 text-xs">token</span>
    <span class="text-gray-400 text-xs">...</span>
    <span class="bg-white rounded px-2 py-1 text-xs">token</span>
    <span class="ml-auto text-xs text-emerald-700 font-bold">超過視窗就會被「忘記」</span>
  </div>
</div>

---
layout: default
---

# 成本怎麼算？（示意）

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 p-6">
    <div class="text-blue-700 font-bold mb-3 text-center">雲端 API</div>
    <div class="text-center text-2xl font-bold text-blue-600 mb-2">用量 × 單價</div>
    <div class="text-xs text-gray-500 text-center">用越多、付越多，沒有上限</div>
  </div>
  <div class="rounded-2xl border-2 border-amber-300 bg-amber-50 p-6">
    <div class="text-amber-700 font-bold mb-3 text-center">地端硬體</div>
    <div class="text-center text-2xl font-bold text-amber-600 mb-2">硬體攤提 + 電費</div>
    <div class="text-xs text-gray-500 text-center">固定成本先付，用越多邊際成本越低</div>
  </div>
</div>

<div class="text-center text-xs text-gray-400 mt-8">＊示意公式，非實際數字，用量夠大時地端通常較划算</div>

---
layout: default
---

# 小結：接下來動手做

<div class="mt-10 space-y-3 text-sm">
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-file-text class="w-5 h-5 text-blue-500 shrink-0" /><span>生成式 AI 從 Transformer 一路發展到今天的百家爭鳴</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-unlock class="w-5 h-5 text-emerald-500 shrink-0" /><span>開源模型追上來了，加上量化技術，地端部署變得可行</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-cpu class="w-5 h-5 text-amber-500 shrink-0" /><span>VRAM、token、context window 是評估地端方案的基本概念</span></div>
</div>

<div class="text-center mt-10 text-amber-600 font-bold">→ 下一節：生成式 AI 應用</div>

---
layout: center
class: text-center
---

# 生成式 AI 應用

<div class="text-sm opacity-60 mt-4">以文件生成為例</div>

---
layout: default
---

# 同一個任務，能選的模型不只一種

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-file-text class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-2">請假單</div>
    <div class="text-xs text-gray-500">從 PDF／PNG／DOCX 擷取人事時地物</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-message-square class="w-8 h-8 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold mb-2">會議記錄</div>
    <div class="text-xs text-gray-500">開會內容整理成會議通知</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-file-text class="w-8 h-8 mx-auto mb-3 text-amber-500" />
    <div class="font-bold mb-2">報告／摘要</div>
    <div class="text-xs text-gray-500">整理資料、生成正式文件</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">這堂課後面的兩個實做都是文件生成——但同一個任務，能用的模型不只一種，怎麼選？</div>

---
layout: default
---

# 模型選型的三個維度

<div class="mt-8 space-y-6">
  <div class="rounded-2xl border-2 p-4">
    <div class="flex items-center justify-between mb-2">
      <span class="font-bold text-blue-600">雲端</span>
      <span class="text-xs text-gray-400">vs</span>
      <span class="font-bold text-emerald-600">地端</span>
    </div>
    <div class="flex gap-4 text-xs text-gray-500">
      <div class="flex-1">免部署、隨時最新，但要連網、資料會經過第三方</div>
      <div class="flex-1 text-right">資料留在本地、可離線，但要自己顧硬體</div>
    </div>
  </div>
  <div class="rounded-2xl border-2 p-4">
    <div class="flex items-center justify-between mb-2">
      <span class="font-bold text-blue-600">大型模型</span>
      <span class="text-xs text-gray-400">vs</span>
      <span class="font-bold text-emerald-600">小型模型</span>
    </div>
    <div class="flex gap-4 text-xs text-gray-500">
      <div class="flex-1">品質好、通用性強，但較貴、較慢</div>
      <div class="flex-1 text-right">快、便宜、好部署，但複雜任務可能不夠準</div>
    </div>
  </div>
  <div class="rounded-2xl border-2 p-4">
    <div class="flex items-center justify-between mb-2">
      <span class="font-bold text-blue-600">通用模型</span>
      <span class="text-xs text-gray-400">vs</span>
      <span class="font-bold text-emerald-600">任務導向模型</span>
    </div>
    <div class="flex gap-4 text-xs text-gray-500">
      <div class="flex-1">什麼任務都能做，彈性最高</div>
      <div class="flex-1 text-right">針對特定任務調校，更準、更穩定</div>
    </div>
  </div>
</div>

---
layout: default
---

# 以文件生成為例：該選哪一種？

<table class="w-full mt-10 text-sm border-collapse">
  <thead>
    <tr class="border-b-2">
      <th class="text-left py-2 px-3">情境</th>
      <th class="text-left py-2 px-3 text-emerald-600">建議選型</th>
      <th class="text-left py-2 px-3 text-gray-500">為什麼</th>
    </tr>
  </thead>
  <tbody class="text-gray-600">
    <tr class="border-b"><td class="py-2 px-3 font-bold">請假單擷取人事時地物</td><td class="py-2 px-3">小型／任務導向 + 地端</td><td class="py-2 px-3">欄位固定、任務簡單；內容常有個資，適合地端</td></tr>
    <tr class="border-b"><td class="py-2 px-3 font-bold">會議記錄生成通知</td><td class="py-2 px-3">中大型模型</td><td class="py-2 px-3">需要組織語言、掌握語境，能力要求較高</td></tr>
    <tr class="border-b"><td class="py-2 px-3 font-bold">大量批次處理文件</td><td class="py-2 px-3">小型 + 地端</td><td class="py-2 px-3">追求速度與成本，沒有 API 用量上限</td></tr>
  </tbody>
</table>

---
layout: default
---

# 什麼是提示工程？

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const resultVague = ref()
const resultGood = ref()

onMounted(() => {
  if (!resultVague.value || !resultGood.value) return
  gsap.set([resultVague.value, resultGood.value], { opacity: 0, y: 8 })

  gsap.timeline({ repeat: -1, repeatDelay: 0.8 })
    .to({}, { duration: 0.6 })
    .to([resultVague.value, resultGood.value], { opacity: 1, y: 0, duration: 0.4, stagger: 0.15 })
    .to({}, { duration: 1.8 })
    .to([resultVague.value, resultGood.value], { opacity: 0, y: 8, duration: 0.3 }, '+=0.2')
})
</script>

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="rounded-2xl border-2 p-4">
    <div class="font-bold text-gray-500 mb-2 text-center flex items-center justify-center gap-1"><lucide-x class="w-4 h-4" /> 模糊的提示</div>
    <div class="rounded-lg bg-gray-50 border p-2 text-xs text-gray-600">「幫我看這張請假單」</div>
    <div class="text-[10px] text-gray-400 mt-2 text-center">沒有角色、沒有格式、沒有範例——每次結果都不一樣</div>
    <div class="flex justify-center my-2 text-lg text-gray-300">↓</div>
    <div ref="resultVague" class="rounded-lg bg-red-50 border border-red-200 p-2 text-[10px] text-gray-600 leading-relaxed">
      「這張單子好像是請假申請，日期不太確定，原因大概跟手術有關，實際天數請再確認……」
    </div>
    <div class="text-[10px] text-red-500 mt-2 text-center">自然語言、格式不固定——程式難以直接接續處理</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-4">
    <div class="font-bold text-emerald-700 mb-2 text-center flex items-center justify-center gap-1"><lucide-check class="w-4 h-4" /> 結構化的提示</div>
    <div class="rounded-lg bg-white border p-2 text-[10px] text-gray-600 leading-relaxed">
      你是人事助理。請從這張請假單擷取：<br/>
      姓名、請假日期、原因、天數<br/>
      並以 JSON 格式輸出，欄位缺漏請填 null
    </div>
    <div class="text-[10px] text-emerald-600 mt-2 text-center">給角色、給格式、給規則——結果穩定可預期</div>
    <div class="flex justify-center my-2 text-lg text-emerald-300">↓</div>
    <pre ref="resultGood" class="rounded-lg bg-white border p-2 text-[9px] font-mono leading-snug whitespace-pre-wrap">{
  "姓名": "小明",
  "請假日期": "114/07/30 - 114/08/05",
  "原因": "車禍手術",
  "天數": 7
}</pre>
  </div>
</div>

---
layout: default
---

# 提示工程的局限

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-repeat class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-2">每次都要重寫</div>
    <div class="text-xs text-gray-500">同樣的任務，下次還是要從頭打一次提示</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-users class="w-8 h-8 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold mb-2">寫法因人而異</div>
    <div class="text-xs text-gray-500">每個人寫的提示不一樣，結果也不一致</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-share-2 class="w-8 h-8 mx-auto mb-3 text-amber-500" />
    <div class="font-bold mb-2">無法複用／分享</div>
    <div class="text-xs text-gray-500">寫得好的提示只存在自己的對話紀錄裡</div>
  </div>
</div>

---
layout: default
---

# 從 Prompt 到 Skill

<div class="flex items-center justify-center gap-6 mt-14">
  <div class="rounded-2xl border-2 p-6 text-center w-52">
    <div class="font-bold text-gray-500 mb-2">Prompt</div>
    <div class="text-xs text-gray-500">一次性、每次重寫<br/>結果不穩定</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6 w-64">
    <div class="font-bold text-emerald-700 mb-3 text-center">Skill</div>
    <div class="flex flex-col gap-2 text-xs">
      <div class="bg-white rounded border p-2 flex items-center gap-2"><lucide-list-checks class="w-4 h-4 text-emerald-600 shrink-0" /> 指令（角色、規則）</div>
      <div class="bg-white rounded border p-2 flex items-center gap-2"><lucide-lightbulb class="w-4 h-4 text-emerald-600 shrink-0" /> 範例（Few-shot）</div>
      <div class="bg-white rounded border p-2 flex items-center gap-2"><lucide-braces class="w-4 h-4 text-emerald-600 shrink-0" /> 輸出格式</div>
    </div>
    <div class="text-xs text-emerald-600 mt-3 text-center">有名字、包裝好、可重複呼叫</div>
  </div>
</div>

---
layout: default
---

# 生成式 AI，也很會寫程式

<div class="text-sm text-gray-500 mb-2">訓練資料裡有大量程式碼——這也是一種「任務」</div>

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-code class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-2">會寫多種語言</div>
    <div class="text-xs text-gray-500">Python、JavaScript、Shell…能讀也能寫</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-terminal class="w-8 h-8 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold mb-2">能在電腦上執行</div>
    <div class="text-xs text-gray-500">搭配 code execution／computer use，寫完就能直接跑</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-settings class="w-8 h-8 mx-auto mb-3 text-amber-500" />
    <div class="font-bold mb-2">依環境調整寫法</div>
    <div class="text-xs text-gray-500">看使用者裝了什麼工具，動態選擇對應的程式庫</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">Skill 不只是「文字指令」，也可以是「教 AI 怎麼寫程式解決這個任務」</div>

---
layout: default
---

# Skill 檔案長什麼樣子？

<div class="text-sm text-gray-500 mb-3">一個 Skill，就是一個有名字、有說明、有步驟的檔案（SKILL.md）</div>

<div class="text-sm">

```markdown
---
name: your-skill-name              # Skill 的名字
description: 這個 Skill 是做什麼的、什麼情況該使用它
---
# 你的 Skill 名稱

## Instructions（操作步驟）
[給 Claude 清楚、一步一步的操作說明]

## Examples（範例）
[具體示範這個 Skill 怎麼被使用]
```

</div>

<div class="text-center text-sm text-gray-500 mt-4">name／description 讓 AI 知道「什麼時候該用」，Instructions／Examples 教它「怎麼用」</div>

---
layout: default
---

# 範例：文件生成 Skill

<div class="text-sm text-gray-500 mb-3">在 open computer 環境下，Skill 可以「現場寫程式」因應使用者的環境</div>

<div class="text-sm">

```markdown
---
name: generate-document
description: 根據使用者提供的內容與所在環境，動態產生格式化文件（Word／PDF／Markdown）
---
# 文件生成 Skill

## Instructions
1. 確認使用者要的檔案格式與內容
2. 檢查目前電腦環境裝了哪些工具／函式庫
3. 撰寫並執行對應的程式碼，產生檔案
4. 回傳檔案路徑，讓使用者可以直接開啟

## Examples
使用者：「幫我把這份會議記錄整理成 Word 文件」
→ 判斷環境已有 python-docx，寫程式產生 .docx 並回傳
```

</div>

<div class="text-center text-sm text-gray-500 mt-4">同一個 Skill，換一台電腦環境不同，寫出來的程式也會不一樣——這正是本課程兩個實做的基礎</div>

---
layout: default
---

# 接下來的兩個實做，都是文件生成的 Skill

<div class="grid grid-cols-2 gap-8 mt-12">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 p-6 text-center">
    <lucide-file-text class="w-9 h-9 mx-auto mb-3 text-blue-500" />
    <div class="font-bold text-lg mb-2">請假代理人 Skill</div>
    <div class="text-sm text-gray-600">PDF／PNG（OCR）／DOCX → 擷取人事時地物</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6 text-center">
    <lucide-message-square class="w-9 h-9 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold text-lg mb-2">會議秘書 Skill</div>
    <div class="text-sm text-gray-600">開會內容 → 生成會議通知</div>
  </div>
</div>

---
layout: default
---

# 什麼是多模態？

<div class="grid grid-cols-4 gap-4 mt-12">
  <div class="rounded-2xl border-2 p-5 text-center">
    <lucide-file-text class="w-8 h-8 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-sm">文字</div>
  </div>
  <div class="rounded-2xl border-2 p-5 text-center">
    <lucide-image class="w-8 h-8 mx-auto mb-2 text-emerald-500" />
    <div class="font-bold text-sm">圖片</div>
  </div>
  <div class="rounded-2xl border-2 p-5 text-center">
    <lucide-mic class="w-8 h-8 mx-auto mb-2 text-amber-500" />
    <div class="font-bold text-sm">音訊</div>
  </div>
  <div class="rounded-2xl border-2 p-5 text-center">
    <lucide-video class="w-8 h-8 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-sm">影片</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">生成式 AI 不再只能處理文字，輸入輸出都可以是圖片、聲音、影片</div>

---
layout: default
---

# 這堂課用到的多模態：OCR

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const ocrBox = ref()
const resultPanel = ref()
const jsonBlock = ref()
const xmlBlock = ref()
const format = ref('json')

onMounted(() => {
  if (!ocrBox.value || !resultPanel.value || !jsonBlock.value || !xmlBlock.value) return

  gsap.set(resultPanel.value, { opacity: 0, y: 8 })
  gsap.set(jsonBlock.value, { opacity: 1 })
  gsap.set(xmlBlock.value, { opacity: 0 })

  const tl = gsap.timeline({ repeat: -1, repeatDelay: 0.6 })
  tl.to(ocrBox.value, { scale: 1.08, duration: 0.3, yoyo: true, repeat: 3 })
  tl.call(() => format.value = 'json')
  tl.to(resultPanel.value, { opacity: 1, y: 0, duration: 0.4 })
  tl.to({}, { duration: 1.4 })
  tl.call(() => format.value = 'xml')
  tl.to(jsonBlock.value, { opacity: 0, duration: 0.3 })
  tl.to(xmlBlock.value, { opacity: 1, duration: 0.3 }, '<')
  tl.to({}, { duration: 1.4 })
  tl.to(resultPanel.value, { opacity: 0, y: 8, duration: 0.3 }, '+=0.2')
  tl.set(jsonBlock.value, { opacity: 1 })
  tl.set(xmlBlock.value, { opacity: 0 })
})
</script>

<div class="flex items-center justify-center gap-6 mt-10">
  <div class="rounded-2xl border-2 p-2 text-center w-36">
    <img src="/請假.png" class="w-full rounded-lg border" />
    <div class="text-xs font-bold mt-2">請假單掃描檔</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div ref="ocrBox" class="rounded-2xl border-2 border-amber-300 bg-amber-50 px-6 py-6 text-center">
    <lucide-scan class="w-8 h-8 mx-auto mb-2 text-amber-600" />
    <div class="text-sm font-bold text-amber-700">OCR</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div ref="resultPanel" class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-3 w-72">
    <div class="flex justify-center gap-2 mb-2 text-[10px] font-bold">
      <span :class="format === 'json' ? 'text-emerald-700' : 'text-gray-300'">JSON</span>
      <span class="text-gray-300">/</span>
      <span :class="format === 'xml' ? 'text-emerald-700' : 'text-gray-300'">XML</span>
    </div>
    <div class="relative" style="height: 168px;">
      <pre ref="jsonBlock" class="absolute inset-0 text-[9px] leading-snug bg-white rounded-lg border p-2 overflow-hidden font-mono whitespace-pre-wrap">{
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
}</pre>
      <pre ref="xmlBlock" class="absolute inset-0 text-[9px] leading-snug bg-white rounded-lg border p-2 overflow-hidden font-mono whitespace-pre-wrap">&lt;請假單&gt;
  &lt;姓名&gt;小明&lt;/姓名&gt;
  &lt;部門&gt;IT&lt;/部門&gt;
  &lt;職位&gt;前端工程師&lt;/職位&gt;
  &lt;日期&gt;7/30&lt;/日期&gt;
  &lt;請假類型&gt;病假&lt;/請假類型&gt;
  &lt;請假時間 起="114/07/30" 迄="114/08/05" 共="7天" /&gt;
  &lt;請假原因&gt;車禍手術&lt;/請假原因&gt;
&lt;/請假單&gt;</pre>
    </div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-8">圖片轉成結構化資料，語言模型才能繼續處理——後面「請假代理人」實做會用到</div>

---
layout: default
---

# 什麼是 MCP？

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const examples = [
  { label: '資料庫', query: '幫我看資料庫裡面 112 年是否有 XXX 稽核資料？' },
  { label: '行事曆', query: '幫我確認 12 號是否有空，我想在上午 10 點安排會議' },
  { label: '文件', query: '幫我確認公司請假規則' },
  { label: '外部 API（搜尋）', query: '幫我查查最近跟食安有關的新聞' },
]

const activeIdx = ref(0)
const queryBubble = ref()

onMounted(() => {
  if (!queryBubble.value) return
  gsap.set(queryBubble.value, { opacity: 0, y: -8 })

  const tl = gsap.timeline({ repeat: -1 })
  examples.forEach((_, i) => {
    tl.call(() => activeIdx.value = i)
    tl.to(queryBubble.value, { opacity: 1, y: 0, duration: 0.4 })
    tl.to({}, { duration: 1.6 })
    tl.to(queryBubble.value, { opacity: 0, y: -8, duration: 0.3 }, '+=0.2')
    tl.to({}, { duration: 0.2 })
  })
})
</script>

<div class="text-center text-base mt-4 mb-4">
  <b class="text-blue-600">Model Context Protocol</b>——讓 AI 模型跟外部工具、資料溝通的標準協定
</div>

<div ref="queryBubble" class="mx-auto mb-5 max-w-lg rounded-xl bg-white border-2 border-blue-300 px-4 py-2 text-center text-sm">
  {{ examples[activeIdx].query }}
</div>

<div class="flex items-center justify-center gap-6">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 px-6 py-10 text-center font-bold">AI 模型</div>
  <div class="flex flex-col items-center gap-1">
    <div class="text-[10px] text-gray-400 font-bold">MCP</div>
    <div class="text-2xl text-gray-300">⇄</div>
  </div>
  <div class="grid grid-cols-2 gap-3">
    <div class="rounded-xl border-2 p-3 text-center text-xs flex flex-col items-center gap-1 transition-all duration-300" :class="activeIdx === 0 ? 'border-blue-400 bg-blue-50 scale-105' : 'border-gray-200 bg-white opacity-60'">
      <lucide-database class="w-5 h-5" :class="activeIdx === 0 ? 'text-blue-500' : 'text-gray-400'" />資料庫
    </div>
    <div class="rounded-xl border-2 p-3 text-center text-xs flex flex-col items-center gap-1 transition-all duration-300" :class="activeIdx === 1 ? 'border-blue-400 bg-blue-50 scale-105' : 'border-gray-200 bg-white opacity-60'">
      <lucide-calendar class="w-5 h-5" :class="activeIdx === 1 ? 'text-blue-500' : 'text-gray-400'" />行事曆
    </div>
    <div class="rounded-xl border-2 p-3 text-center text-xs flex flex-col items-center gap-1 transition-all duration-300" :class="activeIdx === 2 ? 'border-blue-400 bg-blue-50 scale-105' : 'border-gray-200 bg-white opacity-60'">
      <lucide-file-text class="w-5 h-5" :class="activeIdx === 2 ? 'text-blue-500' : 'text-gray-400'" />文件
    </div>
    <div class="rounded-xl border-2 p-3 text-center text-xs flex flex-col items-center gap-1 transition-all duration-300" :class="activeIdx === 3 ? 'border-blue-400 bg-blue-50 scale-105' : 'border-gray-200 bg-white opacity-60'">
      <lucide-globe class="w-5 h-5" :class="activeIdx === 3 ? 'text-blue-500' : 'text-gray-400'" />外部 API
    </div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-8">常見比喻：<b>USB-C for AI</b>——不用每個工具都做一個專屬接頭</div>

---
layout: default
---

# MCP 解決的問題

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 p-6">
    <div class="font-bold text-gray-500 mb-3 text-center">沒有 MCP</div>
    <div class="text-sm text-gray-600 text-center">每個模型都要為每個工具客製化串接</div>
    <div class="text-center text-2xl font-bold text-gray-400 mt-4">M × N 種串接</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6">
    <div class="font-bold text-emerald-700 mb-3 text-center">有了 MCP</div>
    <div class="text-sm text-gray-600 text-center">模型與工具都只要接上同一種協定</div>
    <div class="text-center text-2xl font-bold text-emerald-600 mt-4">M + N 個連接點</div>
  </div>
</div>

---
layout: default
---

# MCP 在這堂課的應用

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-file-text class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-2">MCP 讀取文本</div>
    <div class="text-xs text-gray-500">讓 Agent 直接讀取文件內容，不用手動貼上</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-scan class="w-8 h-8 mx-auto mb-3 text-amber-500" />
    <div class="font-bold mb-2">文字 OCR 萃取內容</div>
    <div class="text-xs text-gray-500">掃描檔／圖片先轉成文字，才能被模型處理</div>
  </div>
</div>

<div class="text-center text-xs text-gray-400 mt-8">＊後面「外掛程式」小節會實際示範</div>

---
layout: default
---

# 什麼是 A2A？

<div class="text-center text-base mt-6 mb-8">
  <b class="text-emerald-600">Agent-to-Agent</b>——讓不同 Agent 之間可以互相溝通、協作的協定
</div>

<div class="grid grid-cols-2 gap-8">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 p-6 text-center">
    <lucide-plug class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-1">MCP</div>
    <div class="text-xs text-gray-500">Agent 對 工具／資料</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6 text-center">
    <lucide-users class="w-8 h-8 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold mb-1">A2A</div>
    <div class="text-xs text-gray-500">Agent 對 Agent</div>
  </div>
</div>

---
layout: default
---

# 為什麼這堂課會用到 A2A？

<div class="flex items-center justify-center gap-4 mt-16">
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 px-5 py-6 text-center text-sm font-bold">會議秘書<br/>Agent</div>
  <div class="flex flex-col items-center gap-1">
    <div class="text-[10px] text-emerald-600 font-bold text-center">A2A：<br/>詢問空檔</div>
    <div class="text-2xl text-emerald-400">⇄</div>
  </div>
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 px-5 py-6 text-center text-sm font-bold">行事曆<br/>Agent</div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">Agent 詢問另一個 Agent、多個 Agent 互連——這堂課後面會實際做出來</div>

---
layout: center
class: text-center
---

# AI Agent 概念與 Workflow Agents

Build Multi-agents via ADK

<div class="text-sm opacity-60 mt-4">
節錄自參考資料｜Google Cloud Day Taipei '26 Hands-on-Lab（第 12～17 頁）
</div>

---
layout: two-cols
---

# 什麼是 AI Agent

<div class="text-base leading-relaxed space-y-6 pr-8 mt-10">
  <p>一個根據其可用的 <b class="text-blue-600">inputs</b> 及 <b class="text-blue-600">tools</b>，<b class="text-emerald-600">推理如何最好地達成目標</b>的應用程式</p>
  <p><b class="text-amber-600">Model：</b>用於對想達成的目標進行推理、確定計劃並生成回覆</p>
  <p><b class="text-amber-600">Tools：</b>透過呼叫其他 APIs 或服務來獲取數據、執行操作或交易</p>
  <p><b class="text-amber-600">Orchestration：</b>維護記憶與狀態（包括用於規劃的方法）、tools、獲取的數據等</p>
</div>

::right::

<div class="rounded-2xl border p-6 shadow mt-10 bg-white">
  <div class="flex gap-4">
    <div class="flex-1 rounded-xl bg-amber-50 border-2 border-amber-300 p-4">
      <div class="text-amber-600 font-bold text-center text-sm mb-3">Orchestration</div>
      <div class="bg-white rounded-lg border p-3 text-sm text-center mb-3">角色、目標與指令</div>
      <div class="bg-white rounded-lg border p-3 text-sm text-center mb-3">
        記憶
        <div class="flex gap-2 mt-2">
          <div class="flex-1 border border-dashed rounded px-1 py-1 text-xs">短期記憶</div>
          <div class="flex-1 border border-dashed rounded px-1 py-1 text-xs">長期記憶</div>
        </div>
      </div>
      <div class="bg-white rounded-lg border p-3 text-sm text-center leading-tight">基於 Model 的推理與規劃<br/>（問題分解與反思）</div>
    </div>
    <div class="flex flex-col gap-4 flex-1">
      <div class="rounded-lg bg-emerald-50 border-2 border-emerald-400 p-3 text-sm text-center">
        <div class="text-emerald-700 font-bold mb-1">Generative AI Models</div>
        (Agent 可使用多個 models)
      </div>
      <div class="rounded-lg bg-blue-50 border-2 border-blue-300 p-3">
        <div class="text-blue-700 font-bold text-center text-sm mb-3">Tools</div>
        <div class="grid grid-cols-2 gap-2 text-xs text-center">
          <div class="bg-white rounded border p-2">APIs</div>
          <div class="bg-white rounded border p-2">Functions</div>
          <div class="bg-white rounded border p-2">Databases</div>
          <div class="bg-white rounded border p-2">Agents</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!--
Orchestration 與 Tools 雙向箭頭在此版面以並排區塊呈現，箭頭語意保留在講者說明中。
-->

---
layout: default
---

# AI Agent 演進

<div class="flex items-end justify-between mt-24 px-2 w-full">

  <div class="flex flex-col items-center gap-2">
    <div class="w-11 h-11 rounded-full bg-blue-500 text-white flex items-center justify-center text-[10px] font-bold">LLM</div>
    <div class="px-2 py-1 rounded-full bg-blue-500 text-white text-[10px] font-bold whitespace-nowrap">LLM + Prompt</div>
  </div>

  <div class="flex-1 border-t-2 border-gray-300 mx-1 mb-5"></div>

  <div class="flex flex-col items-center gap-2">
    <div class="flex gap-1">
      <div class="w-11 h-11 rounded-full bg-blue-500 text-white flex items-center justify-center text-[10px] font-bold">LLM</div>
      <div class="w-11 h-11 rounded-full bg-emerald-500 text-white flex items-center justify-center text-[10px] font-bold">RAG</div>
    </div>
    <div class="px-2 py-1 rounded-full bg-blue-500 text-white text-[10px] font-bold whitespace-nowrap">LLM + Retrieval</div>
  </div>

  <div class="flex-1 border-t-2 border-gray-300 mx-1 mb-5"></div>

  <div class="flex flex-col items-center gap-2">
    <div class="flex gap-1">
      <div class="w-11 h-11 rounded-full bg-blue-500 text-white flex items-center justify-center text-[10px] font-bold">LLM</div>
      <div class="w-11 h-11 rounded-full bg-emerald-500 text-white flex items-center justify-center text-[10px] font-bold">RAG</div>
      <div class="w-11 h-11 rounded-full bg-orange-500 text-white flex items-center justify-center text-[9px] font-bold">Tools</div>
    </div>
    <div class="px-2 py-1 rounded-full bg-blue-500 text-white text-[10px] font-bold text-center leading-tight">LLM + Retrieval<br/>+ Actions</div>
  </div>

  <div class="flex-1 border-t-2 border-gray-300 mx-1 mb-5"></div>

  <div class="flex flex-col items-center gap-2">
    <div class="w-18 h-18 rounded-full border-2 border-blue-400 flex items-center justify-center flex-wrap gap-0.5 p-1">
      <div class="w-6 h-6 rounded-full bg-blue-500 text-white flex items-center justify-center text-[7px]">LLM</div>
      <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-[7px]">RAG</div>
      <div class="w-6 h-6 rounded-full bg-orange-500 text-white flex items-center justify-center text-[6px]">Tools</div>
    </div>
    <div class="px-2 py-1 rounded-full bg-blue-500 text-white text-[10px] font-bold text-center leading-tight">+ 多種 Tools &<br/>推理循環</div>
  </div>

  <div class="flex-1 border-t-2 border-gray-300 mx-1 mb-5"></div>

  <div class="flex flex-col items-center gap-2">
    <div class="relative w-24 h-18">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-12 h-12 rounded-full border-2 border-blue-400 bg-white flex items-center justify-center flex-wrap gap-0.5 p-0.5">
        <div class="w-4 h-4 rounded-full bg-blue-500"></div>
        <div class="w-4 h-4 rounded-full bg-emerald-500"></div>
        <div class="w-4 h-4 rounded-full bg-orange-500"></div>
      </div>
      <div class="absolute bottom-0 left-0 w-12 h-12 rounded-full border-2 border-blue-400 bg-white flex items-center justify-center flex-wrap gap-0.5 p-0.5">
        <div class="w-4 h-4 rounded-full bg-blue-500"></div>
        <div class="w-4 h-4 rounded-full bg-emerald-500"></div>
        <div class="w-4 h-4 rounded-full bg-orange-500"></div>
      </div>
      <div class="absolute bottom-0 right-0 w-12 h-12 rounded-full border-2 border-blue-400 bg-white flex items-center justify-center flex-wrap gap-0.5 p-0.5">
        <div class="w-4 h-4 rounded-full bg-blue-500"></div>
        <div class="w-4 h-4 rounded-full bg-emerald-500"></div>
        <div class="w-4 h-4 rounded-full bg-orange-500"></div>
      </div>
    </div>
    <div class="px-2 py-1 rounded-full bg-blue-500 text-white text-[10px] font-bold whitespace-nowrap">Multi Agent 系統</div>
  </div>

</div>

---
layout: default
---

# 什麼時候需要 Workflow Agents？

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-blue-500 text-white flex items-center justify-center mb-4"><lucide-cloud class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">可預測性</div>
    <div class="text-sm text-gray-600">基於 Agent 類型與配置，保證其執行流程。</div>
  </div>
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-emerald-500 text-white flex items-center justify-center mb-4"><lucide-check class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">高可靠性</div>
    <div class="text-sm text-gray-600">確保任務始終一致地按照要求的順序或模式運行。</div>
  </div>
  <div class="rounded-2xl border-2 p-6">
    <div class="w-14 h-14 rounded-full bg-amber-500 text-white flex items-center justify-center mb-4"><lucide-network class="w-7 h-7" /></div>
    <div class="font-bold text-lg mb-2">高結構化</div>
    <div class="text-sm text-gray-600">允許您透過在清晰的控制結構中組合 Agent，來建構複雜的流程。</div>
  </div>
</div>

---
layout: default
---

# Sequential Agent

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const seqCrabWrap = ref()
const seqState = ref('idle')

onMounted(() => {
  const el = seqCrabWrap.value
  if (!el) return
  gsap.set(el, { left: '8%', top: '50%', opacity: 0, xPercent: -50, yPercent: -50 })
  gsap.timeline({ repeat: -1, repeatDelay: 0.6 })
    .call(() => seqState.value = 'idle')
    .to(el, { opacity: 1, duration: 0.4 })
    .call(() => seqState.value = 'walk')
    .to(el, { left: '42%', duration: 1, ease: 'power1.inOut' }, '+=0.4')
    .call(() => seqState.value = 'typing')
    .to({}, { duration: 0.9 })
    .call(() => seqState.value = 'walk')
    .to(el, { left: '58%', duration: 0.8, ease: 'power1.inOut' }, '+=0.2')
    .call(() => seqState.value = 'typing')
    .to({}, { duration: 0.9 })
    .call(() => seqState.value = 'walk')
    .to(el, { left: '92%', duration: 1, ease: 'power1.inOut' }, '+=0.2')
    .call(() => seqState.value = 'report')
    .to({}, { duration: 1.2 })
    .to(el, { opacity: 0, duration: 0.4 }, '+=0.3')
    .set(el, { left: '8%' })
    .call(() => seqState.value = 'idle')
})
</script>

<div class="mt-16">
  <div class="relative h-20">
    <div ref="seqCrabWrap" class="absolute z-30" style="top: 40%;">
      <PixelCrab :state="seqState" :size="44" />
    </div>
  </div>
  <div class="flex items-center justify-center gap-4">
    <div class="rounded-xl bg-amber-100 border-2 border-amber-300 px-8 py-10 text-lg font-bold">輸入</div>
    <div class="text-3xl text-gray-400">→</div>
    <div class="rounded-2xl bg-amber-50 border-2 border-amber-300 p-8">
      <div class="text-amber-600 font-bold text-center text-lg mb-4">SequentialAgent</div>
      <div class="flex items-center gap-4">
        <div class="rounded-xl bg-amber-200 px-6 py-7 text-center">
          <div class="text-sm font-bold mb-2">sub_agents_1</div>
          <div class="flex justify-center"><lucide-bot class="w-7 h-7 text-amber-600" /></div>
        </div>
        <div class="text-2xl text-amber-600">→</div>
        <div class="rounded-xl bg-amber-200 px-6 py-7 text-center">
          <div class="text-sm font-bold mb-2">sub_agents_2</div>
          <div class="flex justify-center"><lucide-bot class="w-7 h-7 text-amber-600" /></div>
        </div>
      </div>
    </div>
    <div class="text-3xl text-gray-400">→</div>
    <div class="rounded-xl bg-amber-100 border-2 border-amber-300 px-8 py-10 text-lg font-bold">輸出</div>
  </div>
</div>

---
layout: default
---

# Parallel Agent

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const crabWrapA = ref()
const crabWrapB = ref()
const crabWrapC = ref()
const parState = ref('idle')

onMounted(() => {
  const els = [crabWrapA.value, crabWrapB.value, crabWrapC.value]
  if (els.some(e => !e)) return

  const targets = [
    { sub: '38%', subTop: '35%', out: '92%', outTop: '22%' },
    { sub: '50%', subTop: '50%', out: '92%', outTop: '50%' },
    { sub: '62%', subTop: '65%', out: '92%', outTop: '78%' },
  ]

  els.forEach(el => gsap.set(el, { left: '8%', top: '50%', opacity: 0, xPercent: -50, yPercent: -50 }))

  const tl = gsap.timeline({ repeat: -1, repeatDelay: 0.6 })
  tl.call(() => parState.value = 'idle')
  tl.to(els, { opacity: 1, duration: 0.4 })
  tl.call(() => parState.value = 'walk')
  els.forEach((el, i) => {
    tl.to(el, { left: targets[i].sub, top: targets[i].subTop, duration: 1, ease: 'power1.inOut' }, '<')
  })
  tl.call(() => parState.value = 'typing')
  tl.to({}, { duration: 0.9 })
  tl.call(() => parState.value = 'walk')
  els.forEach((el, i) => {
    tl.to(el, { left: targets[i].out, top: targets[i].outTop, duration: 1, ease: 'power1.inOut' }, '<')
  })
  tl.call(() => parState.value = 'report')
  tl.to({}, { duration: 1 })
  tl.to(els, { opacity: 0, duration: 0.4 }, '+=0.4')
  tl.set(els, { left: '8%', top: '50%' })
  tl.call(() => parState.value = 'idle')
})
</script>

<div class="mt-10">
  <div class="relative h-20">
    <div ref="crabWrapA" class="absolute z-30">
      <PixelCrab :state="parState" :size="32" />
    </div>
    <div ref="crabWrapB" class="absolute z-30">
      <PixelCrab :state="parState" :size="32" />
    </div>
    <div ref="crabWrapC" class="absolute z-30">
      <PixelCrab :state="parState" :size="32" />
    </div>
  </div>
  <div class="flex items-center justify-center gap-4">
    <div class="rounded-xl bg-amber-100 border-2 border-amber-300 px-8 py-10 text-lg font-bold">輸入</div>
    <div class="text-3xl text-gray-400">→</div>
    <div class="rounded-2xl bg-amber-50 border-2 border-amber-300 p-8">
      <div class="text-amber-600 font-bold text-center text-lg mb-4">Parallel Agent</div>
      <div class="flex gap-5">
        <div class="rounded-xl bg-amber-200 px-6 py-6 text-center">
          <div class="text-sm font-bold mb-2">sub_agents_1</div>
          <div class="flex justify-center"><lucide-bot class="w-7 h-7 text-amber-600" /></div>
        </div>
        <div class="rounded-xl bg-amber-200 px-6 py-6 text-center">
          <div class="text-sm font-bold mb-2">sub_agents_2</div>
          <div class="flex justify-center"><lucide-bot class="w-7 h-7 text-amber-600" /></div>
        </div>
        <div class="rounded-xl bg-amber-200 px-6 py-6 text-center">
          <div class="text-sm font-bold mb-2">sub_agents_3</div>
          <div class="flex justify-center"><lucide-bot class="w-7 h-7 text-amber-600" /></div>
        </div>
      </div>
    </div>
    <div class="flex flex-col gap-3 text-base font-bold text-gray-600">
      <div>→ 輸出_1</div>
      <div>→ 輸出_2</div>
      <div>→ 輸出_3</div>
    </div>
  </div>
</div>

---
layout: default
---

# LoopAgent

<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

const loopCrabWrap = ref()
const loopState = ref('idle')

onMounted(() => {
  const el = loopCrabWrap.value
  if (!el) return
  gsap.set(el, { left: '8%', top: '50%', opacity: 0, xPercent: -50, yPercent: -50 })

  const stops = ['32%', '44%', '56%', '68%']
  const tl = gsap.timeline({ repeat: -1, repeatDelay: 0.6 })
  tl.call(() => loopState.value = 'idle')
  tl.to(el, { opacity: 1, duration: 0.4 })
  stops.forEach(pos => {
    tl.call(() => loopState.value = 'walk')
    tl.to(el, { left: pos, duration: 0.6, ease: 'power1.inOut' }, '+=0.3')
    tl.call(() => loopState.value = 'typing')
    tl.to({}, { duration: 0.5 })
  })
  tl.call(() => loopState.value = 'idle')
  tl.to(el, { opacity: 0, duration: 0.3 }, '+=0.2')
  tl.set(el, { left: stops[0] })
  tl.to(el, { opacity: 1, duration: 0.3 })
  stops.slice(1).forEach(pos => {
    tl.call(() => loopState.value = 'walk')
    tl.to(el, { left: pos, duration: 0.6, ease: 'power1.inOut' }, '+=0.3')
    tl.call(() => loopState.value = 'typing')
    tl.to({}, { duration: 0.5 })
  })
  tl.call(() => loopState.value = 'walk')
  tl.to(el, { left: '90%', duration: 0.8, ease: 'power1.inOut' }, '+=0.4')
  tl.call(() => loopState.value = 'report')
  tl.to({}, { duration: 1 })
  tl.to(el, { opacity: 0, duration: 0.3 }, '+=0.2')
  tl.set(el, { left: '8%' })
  tl.call(() => loopState.value = 'idle')
})
</script>

<div class="mt-16">
  <div class="relative h-20">
    <div ref="loopCrabWrap" class="absolute z-30" style="top: 50%;">
      <PixelCrab :state="loopState" :size="40" />
    </div>
  </div>
  <div class="flex items-center justify-center gap-4">
    <div class="rounded-xl bg-amber-100 border-2 border-amber-300 px-8 py-10 text-lg font-bold">輸入</div>
    <div class="text-3xl text-gray-400">→</div>
    <div class="rounded-2xl bg-amber-50 border-2 border-amber-300 p-8 w-[480px]">
      <div class="flex items-center justify-between mb-4">
        <div class="text-amber-600 font-bold text-base flex items-center gap-1"><lucide-bot class="w-5 h-5" /> Loop Agent</div>
        <div class="text-xs text-gray-500">sync 迴圈（Loop）max_iterations=2</div>
      </div>
      <div class="flex gap-1">
        <div class="flex-1 rounded-xl bg-amber-200 px-3 py-6 text-center text-xs font-bold">sub_agents_1</div>
        <div class="flex-1 rounded-xl bg-amber-200 px-3 py-6 text-center text-xs font-bold">sub_agents_2</div>
        <div class="flex-1 rounded-xl bg-amber-200 px-3 py-6 text-center text-xs font-bold">sub_agents_3</div>
        <div class="flex-1 rounded-xl bg-amber-200 px-3 py-6 text-center text-xs font-bold">sub_agents_4</div>
      </div>
      <div class="text-center text-sm text-gray-500 mt-4">符合結束條件（Exit condition）</div>
    </div>
    <div class="text-3xl text-gray-400">→</div>
    <div class="rounded-xl bg-amber-100 border-2 border-amber-300 px-8 py-10 text-lg font-bold">輸出</div>
  </div>
</div>

---
layout: center
class: text-center
---

# Ollama 部署及規格

<div class="text-sm opacity-60 mt-4">以 NVIDIA GB10（DGX Spark）為例</div>

---
layout: default
---

# 統一記憶體架構 vs 傳統 GPU 架構

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="rounded-2xl border-2 p-5">
    <div class="text-center font-bold mb-4 text-gray-500">傳統 GPU 架構</div>
    <div class="flex flex-col items-center gap-2">
      <div class="flex gap-2">
        <div class="rounded-xl bg-blue-50 border-2 border-blue-300 px-4 py-3 text-center text-xs font-bold">CPU</div>
        <div class="rounded-xl bg-blue-50 border-2 border-blue-300 px-4 py-3 text-center text-xs font-bold">系統 RAM</div>
      </div>
      <div class="text-[10px] text-gray-400">PCIe（頻寬有限、需搬資料）</div>
      <div class="text-xl text-gray-400">↕</div>
      <div class="flex gap-2">
        <div class="rounded-xl bg-amber-50 border-2 border-amber-300 px-4 py-3 text-center text-xs font-bold">GPU</div>
        <div class="rounded-xl bg-amber-50 border-2 border-amber-300 px-4 py-3 text-center text-xs font-bold">VRAM<br/>（獨立、有上限）</div>
      </div>
    </div>
    <div class="text-xs text-gray-500 text-center mt-4">模型超過 VRAM 容量時，需要切分／卸載到系統 RAM</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-5">
    <div class="text-center font-bold mb-4 text-emerald-700">統一記憶體架構（GB10）</div>
    <div class="flex flex-col items-center gap-2">
      <div class="flex gap-2">
        <div class="rounded-xl bg-white border-2 border-emerald-400 px-4 py-3 text-center text-xs font-bold">CPU<br/>Grace</div>
        <div class="rounded-xl bg-white border-2 border-emerald-400 px-4 py-3 text-center text-xs font-bold">GPU<br/>Blackwell</div>
      </div>
      <div class="text-[10px] text-emerald-600 font-bold">NVLink-C2C（同一位址空間）</div>
      <div class="text-xl text-emerald-500">↕</div>
      <div class="rounded-xl bg-white border-2 border-emerald-400 px-8 py-3 text-center text-xs font-bold">共用記憶體池　128GB</div>
    </div>
    <div class="text-xs text-emerald-700 text-center mt-4">CPU／GPU 共用同一塊記憶體，不需要搬資料</div>
  </div>
</div>

---
layout: default
---

# GB10：NVIDIA DGX Spark

<div class="grid grid-cols-3 gap-4 mt-10">
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-database class="w-7 h-7 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-sm mb-1">統一記憶體</div>
    <div class="text-xs text-gray-500">128GB LPDDR5x</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-cpu class="w-7 h-7 mx-auto mb-2 text-emerald-500" />
    <div class="font-bold text-sm mb-1">CPU</div>
    <div class="text-xs text-gray-500">20 核 Grace（Arm）</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-zap class="w-7 h-7 mx-auto mb-2 text-amber-500" />
    <div class="font-bold text-sm mb-1">GPU</div>
    <div class="text-xs text-gray-500">Blackwell 架構</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-link class="w-7 h-7 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-sm mb-1">互連</div>
    <div class="text-xs text-gray-500">NVLink-C2C</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-gauge class="w-7 h-7 mx-auto mb-2 text-emerald-500" />
    <div class="font-bold text-sm mb-1">算力</div>
    <div class="text-xs text-gray-500">最高 1 petaFLOP（FP4）</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-plug class="w-7 h-7 mx-auto mb-2 text-amber-500" />
    <div class="font-bold text-sm mb-1">功耗</div>
    <div class="text-xs text-gray-500">TDP 140W</div>
  </div>
</div>

<div class="text-center text-xs text-gray-400 mt-6">＊官方規格數字，實測效能會依軟體／驅動版本而有落差</div>

---
layout: default
---

# 為什麼統一記憶體對地端 LLM 很重要

<div class="mt-10 space-y-5">
  <div class="flex items-center gap-4">
    <div class="w-32 text-xs font-bold text-gray-500 shrink-0">消費級 GPU</div>
    <div class="flex-1 h-6 bg-gray-100 rounded-full overflow-hidden"><div class="w-[15%] h-6 bg-gray-400 rounded-full"></div></div>
    <div class="w-40 text-xs text-gray-500 shrink-0">24～32GB VRAM 上限</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-32 text-xs font-bold text-emerald-600 shrink-0">GB10 單台</div>
    <div class="flex-1 h-6 bg-gray-100 rounded-full overflow-hidden"><div class="w-[65%] h-6 bg-emerald-400 rounded-full"></div></div>
    <div class="w-40 text-xs text-gray-500 shrink-0">推論可達 ~200B／微調 ~70B</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-32 text-xs font-bold text-amber-600 shrink-0">GB10 兩台聯網</div>
    <div class="flex-1 h-6 bg-gray-100 rounded-full overflow-hidden"><div class="w-full h-6 bg-amber-400 rounded-full"></div></div>
    <div class="w-40 text-xs text-gray-500 shrink-0">可達 ~405B 等級</div>
  </div>
</div>

<div class="mt-10 rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-4 text-sm text-emerald-800 text-center">
關鍵不是「算力比較快」，而是「裝得下比較大的模型」——不用把模型切開放在 GPU／CPU 兩邊
</div>

---
layout: default
---

# 傳統 GPU vs GB10 對照表

<table class="w-full mt-10 text-sm border-collapse">
  <thead>
    <tr class="border-b-2">
      <th class="text-left py-2 px-3"></th>
      <th class="text-left py-2 px-3 text-gray-500">傳統獨立 GPU</th>
      <th class="text-left py-2 px-3 text-emerald-600">GB10（統一記憶體）</th>
    </tr>
  </thead>
  <tbody class="text-gray-600">
    <tr class="border-b"><td class="py-2 px-3 font-bold">記憶體配置</td><td class="py-2 px-3">CPU／GPU 各自獨立</td><td class="py-2 px-3">CPU／GPU 共用一塊</td></tr>
    <tr class="border-b"><td class="py-2 px-3 font-bold">資料搬移</td><td class="py-2 px-3">需經 PCIe 複製</td><td class="py-2 px-3">同一位址空間，免複製</td></tr>
    <tr class="border-b"><td class="py-2 px-3 font-bold">容量上限</td><td class="py-2 px-3">通常 24～32GB</td><td class="py-2 px-3">128GB</td></tr>
    <tr class="border-b"><td class="py-2 px-3 font-bold">適合場景</td><td class="py-2 px-3">中小模型、追求速度</td><td class="py-2 px-3">大模型、追求裝得下</td></tr>
  </tbody>
</table>

---
layout: default
---

# Ollama 在這類設備上部署的重點

<div class="mt-10 space-y-3 text-sm">
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-terminal class="w-5 h-5 text-blue-500 shrink-0" /><span>Ollama 原生支援 Arm／Linux，GB10 上安裝方式與一般機器相同</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-layers class="w-5 h-5 text-emerald-500 shrink-0" /><span>記憶體空間充裕，不必為了塞進顯卡而被迫用最激進的量化</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-gauge class="w-5 h-5 text-amber-500 shrink-0" /><span>仍可視情況搭配量化（GGUF／AWQ），換取更快的推論速度</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-flask-conical class="w-5 h-5 text-blue-500 shrink-0" /><span>建議先從小模型測試流程，確認可行後再放大模型規模</span></div>
</div>

---
layout: center
class: text-center
---

# AI 模型安全控管

<div class="text-sm opacity-60 mt-4">以 litellm 為例：API Key、分流</div>

---
layout: default
---

# 為什麼需要模型安全控管？

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-key class="w-8 h-8 mx-auto mb-3 text-blue-500" />
    <div class="font-bold mb-2">金鑰外洩風險</div>
    <div class="text-xs text-gray-500">每個 App 都拿到真正的 API Key，一旦外洩難以追查</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-dollar-sign class="w-8 h-8 mx-auto mb-3 text-emerald-500" />
    <div class="font-bold mb-2">無法統一控管成本</div>
    <div class="text-xs text-gray-500">用量分散在各處，很難知道誰用了多少</div>
  </div>
  <div class="rounded-2xl border-2 p-6 text-center">
    <lucide-network class="w-8 h-8 mx-auto mb-3 text-amber-500" />
    <div class="font-bold mb-2">各自串接難維護</div>
    <div class="text-xs text-gray-500">每個 App 各自接不同模型 API，改動時到處要改</div>
  </div>
</div>

---
layout: default
---

# litellm 是什麼？

<div class="flex items-center justify-center gap-6 mt-14">
  <div class="flex flex-col gap-2">
    <div class="rounded-lg border px-3 py-2 text-xs text-center">App A</div>
    <div class="rounded-lg border px-3 py-2 text-xs text-center">App B</div>
    <div class="rounded-lg border px-3 py-2 text-xs text-center">App C</div>
  </div>
  <div class="text-xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 px-6 py-10 text-center font-bold text-blue-700">litellm</div>
  <div class="text-xl text-gray-400">→</div>
  <div class="flex flex-col gap-2">
    <div class="rounded-lg border px-3 py-2 text-xs text-center">OpenAI</div>
    <div class="rounded-lg border px-3 py-2 text-xs text-center">Anthropic</div>
    <div class="rounded-lg border px-3 py-2 text-xs text-center">地端 Ollama</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">統一的 OpenAI 相容介面，App 不用管背後接的是哪一家模型</div>

---
layout: default
---

# API Key 管理

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="rounded-2xl border-2 p-6">
    <div class="font-bold text-gray-500 mb-3 text-center">沒有 litellm</div>
    <div class="text-sm text-gray-600 text-center">每個 App 都拿到真正的 API Key</div>
    <div class="text-xs text-gray-400 text-center mt-3">外洩風險高、難以撤銷或更換</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6">
    <div class="font-bold text-emerald-700 mb-3 text-center">有了 litellm</div>
    <div class="text-sm text-gray-600 text-center">App 只拿到 litellm 發的虛擬 Key</div>
    <div class="text-xs text-emerald-600 text-center mt-3">真正的金鑰只存在 litellm 後端，可隨時撤換</div>
  </div>
</div>

---
layout: default
---

# 分流

<div class="mt-10 space-y-3 text-sm">
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-lock class="w-5 h-5 text-blue-500 shrink-0" /><span><b>依敏感度分流：</b>含機密內容的請求導向地端模型，一般查詢導向雲端</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-dollar-sign class="w-5 h-5 text-emerald-500 shrink-0" /><span><b>依成本分流：</b>簡單任務導向便宜的小模型，複雜任務才用大模型</span></div>
  <div class="rounded-xl border p-4 flex items-center gap-3"><lucide-repeat class="w-5 h-5 text-amber-500 shrink-0" /><span><b>容錯備援：</b>主要供應商異常時，自動切換到備援模型</span></div>
</div>

---
layout: default
---

# 每一次呼叫都有紀錄

<div class="rounded-2xl border-2 overflow-hidden mt-8">
  <div class="bg-gray-50 border-b px-4 py-2 flex gap-4 text-xs">
    <span class="text-blue-600 font-bold border-b-2 border-blue-600 pb-1">Request Logs</span>
    <span class="text-gray-400">Audit Logs</span>
    <span class="text-gray-400">Deleted Keys</span>
  </div>
  <table class="w-full text-xs">
    <thead>
      <tr class="border-b bg-gray-50 text-gray-400">
        <th class="text-left py-2 px-3 font-normal">Time</th>
        <th class="text-left py-2 px-3 font-normal">Status</th>
        <th class="text-left py-2 px-3 font-normal">Team</th>
        <th class="text-left py-2 px-3 font-normal">Key Name</th>
        <th class="text-left py-2 px-3 font-normal">Model</th>
        <th class="text-left py-2 px-3 font-normal">Tokens</th>
        <th class="text-left py-2 px-3 font-normal">Cost</th>
      </tr>
    </thead>
    <tbody class="text-gray-600">
      <tr class="border-b"><td class="py-2 px-3">09:00:11</td><td class="py-2 px-3"><span class="bg-emerald-100 text-emerald-700 rounded-full px-2 py-0.5 text-[10px]">Success</span></td><td class="py-2 px-3">經理</td><td class="py-2 px-3">小明</td><td class="py-2 px-3">vertex_ai/claude…</td><td class="py-2 px-3">101,618</td><td class="py-2 px-3">$0.0373</td></tr>
      <tr class="border-b"><td class="py-2 px-3">08:57:20</td><td class="py-2 px-3"><span class="bg-emerald-100 text-emerald-700 rounded-full px-2 py-0.5 text-[10px]">Success</span></td><td class="py-2 px-3">主管</td><td class="py-2 px-3">小香</td><td class="py-2 px-3">vertex_ai/claude…</td><td class="py-2 px-3">9</td><td class="py-2 px-3">$0.0000</td></tr>
      <tr class="border-b"><td class="py-2 px-3">08:56:55</td><td class="py-2 px-3"><span class="bg-emerald-100 text-emerald-700 rounded-full px-2 py-0.5 text-[10px]">Success</span></td><td class="py-2 px-3">主管</td><td class="py-2 px-3">技安</td><td class="py-2 px-3">vertex_ai/claude…</td><td class="py-2 px-3">9</td><td class="py-2 px-3">$0.0000</td></tr>
      <tr class="border-b"><td class="py-2 px-3">08:50:12</td><td class="py-2 px-3"><span class="bg-emerald-100 text-emerald-700 rounded-full px-2 py-0.5 text-[10px]">Success</span></td><td class="py-2 px-3">經理</td><td class="py-2 px-3">胖虎</td><td class="py-2 px-3">vertex_ai/claude…</td><td class="py-2 px-3">9</td><td class="py-2 px-3">$0.0000</td></tr>
      <tr><td class="py-2 px-3">08:45:03</td><td class="py-2 px-3"><span class="bg-emerald-100 text-emerald-700 rounded-full px-2 py-0.5 text-[10px]">Success</span></td><td class="py-2 px-3">經理</td><td class="py-2 px-3">小夫</td><td class="py-2 px-3">vertex_ai/claude…</td><td class="py-2 px-3">9</td><td class="py-2 px-3">$0.0000</td></tr>
    </tbody>
  </table>
</div>

<div class="text-center text-sm text-gray-500 mt-6">誰、用哪把 Key、叫了哪個模型、花多少錢——litellm 全部記錄下來</div>

---
layout: default
---

# litellm 後台可控管的範圍

<div class="grid grid-cols-5 gap-3 mt-12">
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-key class="w-7 h-7 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-xs mb-1">金鑰與存取</div>
    <div class="text-[10px] text-gray-500">Virtual Keys／Teams</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-wallet class="w-7 h-7 mx-auto mb-2 text-emerald-500" />
    <div class="font-bold text-xs mb-1">預算控管</div>
    <div class="text-[10px] text-gray-500">Budgets</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-activity class="w-7 h-7 mx-auto mb-2 text-amber-500" />
    <div class="font-bold text-xs mb-1">用量追蹤</div>
    <div class="text-[10px] text-gray-500">Usage／Logs</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-shield class="w-7 h-7 mx-auto mb-2 text-blue-500" />
    <div class="font-bold text-xs mb-1">護欄與政策</div>
    <div class="text-[10px] text-gray-500">Guardrails／Policies</div>
  </div>
  <div class="rounded-2xl border-2 p-4 text-center">
    <lucide-wrench class="w-7 h-7 mx-auto mb-2 text-emerald-500" />
    <div class="font-bold text-xs mb-1">工具治理</div>
    <div class="text-[10px] text-gray-500">MCP Servers／Skills</div>
  </div>
</div>

<div class="text-center text-xs text-gray-400 mt-8">＊示意畫面，實際介面依 litellm 版本而異</div>

---
layout: center
class: text-center
---

# 外掛程式

<div class="text-sm opacity-60 mt-4">MCP 讀取文本、文字 OCR 萃取內容</div>

---
layout: default
---

# 工具怎麼接上 Agent？

<div class="flex items-center justify-center gap-6 mt-16">
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 px-6 py-10 text-center font-bold">Agent</div>
  <div class="flex flex-col items-center gap-1">
    <div class="text-[10px] text-gray-400 font-bold">MCP</div>
    <div class="text-2xl text-gray-300">⇄</div>
  </div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 px-6 py-10 text-center font-bold text-emerald-700">外掛程式<br/><span class="text-xs font-normal">（工具）</span></div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">複習：外掛程式就是透過 MCP 包裝好、Agent 可以直接呼叫的工具</div>

---
layout: default
---

# MCP 讀取文本

<div class="flex items-center justify-center gap-6 mt-16">
  <div class="rounded-2xl border-2 p-6 text-center w-40">
    <lucide-file-text class="w-8 h-8 mx-auto mb-2 text-gray-400" />
    <div class="text-xs font-bold">DOCX／<br/>文字檔</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-blue-300 bg-blue-50 px-6 py-6 text-center">
    <lucide-plug class="w-8 h-8 mx-auto mb-2 text-blue-600" />
    <div class="text-sm font-bold text-blue-700">MCP 工具</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 px-6 py-6 text-center w-40">
    <lucide-bot class="w-8 h-8 mx-auto mb-2 text-emerald-600" />
    <div class="text-xs font-bold text-emerald-700">Agent<br/>直接存取</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">Agent 不用手動貼上文件內容，直接透過工具讀取</div>

---
layout: default
---

# 文字 OCR 萃取內容

<div class="flex items-center justify-center gap-6 mt-16">
  <div class="rounded-2xl border-2 p-6 text-center w-40">
    <lucide-image class="w-8 h-8 mx-auto mb-2 text-gray-400" />
    <div class="text-xs font-bold">PDF／PNG<br/>掃描檔</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-amber-300 bg-amber-50 px-6 py-6 text-center">
    <lucide-scan class="w-8 h-8 mx-auto mb-2 text-amber-600" />
    <div class="text-sm font-bold text-amber-700">OCR 工具</div>
  </div>
  <div class="text-2xl text-gray-400">→</div>
  <div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 px-6 py-6 text-center w-40">
    <lucide-file-text class="w-8 h-8 mx-auto mb-2 text-emerald-600" />
    <div class="text-xs font-bold text-emerald-700">純文字<br/>內容</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">包裝成 MCP 工具後，Agent 可以直接呼叫，不用另外寫程式串接</div>

---
layout: default
---

# 這兩個工具，就是後面實做的基礎

<div class="rounded-2xl border-2 border-emerald-300 bg-emerald-50 p-6 mt-10">
  <div class="font-bold text-emerald-700 text-center mb-4">請假代理人 Skill</div>
  <div class="flex items-center justify-center gap-4">
    <div class="rounded-xl bg-white border px-4 py-3 text-center text-xs font-bold">MCP<br/>讀取文本</div>
    <div class="text-xl text-emerald-500">+</div>
    <div class="rounded-xl bg-white border px-4 py-3 text-center text-xs font-bold">文字 OCR<br/>萃取內容</div>
    <div class="text-xl text-emerald-500">=</div>
    <div class="rounded-xl bg-emerald-100 border-2 border-emerald-400 px-4 py-3 text-center text-xs font-bold">PDF／PNG／DOCX<br/>→ 抓取人事時地物</div>
  </div>
</div>

<div class="text-center text-sm text-gray-500 mt-10">→ 接下來就要動手把這些概念組合成真正能跑的 Agent</div>
