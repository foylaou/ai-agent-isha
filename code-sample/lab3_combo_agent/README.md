# 實做三：請假 → 交接會議秘書（把 lab1、lab2 串起來）

**目標**：用 ADK 的 `SequentialAgent` 把 lab1、lab2 的邏輯接成一條
pipeline——請假單擷取完，自動生成一份交接會議通知。對應投影片
「Sequential Agent」。

## 這份骨架幫你做好了什麼

- **Step 1（`leave_step`）**：跟 `lab1_leave_agent` 完全一樣的請假單
  擷取邏輯，已經寫好，不用再改一次；多了 `output_key="leave_info"`，
  執行完會自動把結果 JSON 寫進 session state。
- **Step 2（`meeting_step`）**：接好模型、`output_key="meeting_notice"`，
  但 `INSTRUCTION` 還是 TODO。
- `root_agent = SequentialAgent(sub_agents=[leave_step, meeting_step])`：
  依序執行兩步，中間的資料透過 state 自動傳遞，你不用手動接管線。

## 你要做的事

`agent.py` 裡 `MEETING_STEP_INSTRUCTION` 只有一行 TODO。打開你的 AI
編輯器，把 `../skills/leave-to-meeting-combo.SKILL.md` 整份餵給它，
請它照著規格幫你把這段 instruction 補完——重點是要教會 Step 2「怎麼讀
`{leave_info}` 這個從 Step 1 傳過來的變數」，而不是重新擷取一次請假單。

## 設定與執行

沿用同一份共用 `.env`（跟 `lab1_leave_agent/`、`lab2_meeting_secretary/`
共用同一組 `LITELLM_API_BASE`／`LITELLM_API_KEY`／`MCP_SERVER_URL`），
在 `code-sample/` 底下：

```bash
pip install -r lab3_combo_agent/requirements.txt
adk web .
```

瀏覽器選 `leave_to_meeting_combo`，測：

```
幫我處理 lab1_leave_agent/sample_data/請假單-範例.png
```

Step 1 跑完會直接接著跑 Step 2，這時 Step 2 應該會反問你交接窗口、
會議時間地點（因為 `{leave_info}` 裡沒有這些資訊）。回答後應該會得到
一份完整的交接會議通知。

## 驗收標準

- Step 1 的輸出（`leave_info`）要跟 lab1 一樣正確：姓名「小明」、
  部門「IT」、病假、1140730–1140805 共 7 天、原因「車禍手術」
- Step 2 沒有重新呼叫 `ocr_image`／`read_document`，而是直接讀
  `{leave_info}`
- Step 2 對缺漏的交接窗口／會議時間地點有反問，不是自己編造
- 最終的會議通知包含請假期間與原因，且格式符合
  `leave-to-meeting-combo.SKILL.md` 的規格

## 進階挑戰（選做）

- 用 `ParallelAgent` 改寫：如果請假單裡本來就有指定代理人欄位，讓
  Step 2 跟一個查詢代理人行事曆的步驟平行跑，比較跟 Sequential 的差異
- 幫 Step 2 加一個「反問」的迴圈上限，避免使用者一直不給資訊時無限
  反問下去（對應投影片 LoopAgent 的 exit 機制概念）
