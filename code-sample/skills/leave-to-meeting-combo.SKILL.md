---
name: leave-to-meeting-combo
description: 用 SequentialAgent 把「請假代理人」與「會議秘書」串成一條 pipeline，請假單擷取完自動生成交接會議通知
---

# 請假 → 交接會議秘書 Combo

對應投影片「Sequential Agent」：多個 Skill 可以串成一條 pipeline，
上一步的輸出透過 `output_key` 存進 session state，下一步的 instruction
直接用 `{state_key}` 讀出來。

這份 Skill 只講 **Step 2（meeting_step）** 要做的事——Step 1
（`leave_step`）就是 `leave-agent.SKILL.md` 那套擷取邏輯，已經幫你接好。

## Instructions（Step 2 操作步驟）

1. `{leave_info}` 是 Step 1 存進 state 的 JSON 字串（姓名、部門、
   請假類型、請假時間、請假原因），直接讀就好，不用呼叫任何工具。
2. 交接窗口是誰、交接會議的時間地點——這些 `{leave_info}` 裡沒有的
   資訊要反問使用者，不可以自己編造。
3. 用下面「輸出格式」生成一份請假交接會議通知。

## 輸出格式

⚠️ 寫進 `instruction` 字串時，格式範本裡的空格不要用 `{像這樣}` 的花括號
——ADK 會把 `instruction` 裡任何 `{word}` 當成 session state 變數去查，
查不到就直接丟 `KeyError` 讓整個 Agent 掛掉。只有 `{leave_info}` 是
真的要讀 state，其他示意用的空格請用 `<角括號>`，例如：

```
【會議通知】<姓名> 請假交接會議

時間：<日期> <開始時間>–<結束時間>
地點：<地點>
與會人員：<請假人>、<交接窗口>

交接事項：
- 請假期間：<leave_info 裡的請假時間>
- 請假原因：<leave_info 裡的請假原因>
- <其他交接重點>
```

## Examples（範例）

輸入（`{leave_info}`，來自 Step 1 處理 `lab1_leave_agent/sample_data/請假單-範例.png` 的結果）：

```json
{
  "姓名": "小明",
  "部門": "IT",
  "職位": "前端工程師",
  "請假類型": "病假",
  "請假時間": { "起": "1140730", "迄": "1140805", "共": "7 天" },
  "請假原因": "車禍手術"
}
```

使用者接著說：「交接窗口是小華，會議約 7/29 下午 3 點，在 3 樓會議室」

預期輸出：

```
【會議通知】小明 請假交接會議

時間：7/29 15:00–16:00
地點：3 樓會議室
與會人員：小明、小華

交接事項：
- 請假期間：114/07/30–114/08/05（共 7 天）
- 請假原因：車禍手術
- 請小華於請假期間代理 IT 部門前端相關工作
```
