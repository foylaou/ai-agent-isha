# 參考解答（講師驗證用，不要發給學員）

跟 `lab1_leave_agent/`、`lab2_meeting_secretary/` 是同一份骨架，唯一差別是
`INSTRUCTION` 已經照 `../skills/*.SKILL.md` 補完。用來驗證整條基礎設施
（MCP server + LiteLLM Proxy）是不是真的打通，不是給學員看的「正確答案」。

工作坊當天發教材給學員之前，記得把整個 `_solutions/` 資料夾拿掉。

## 執行

沿用同一份共用 `.env`（跟 `lab1_leave_agent/`、`lab2_meeting_secretary/`
共用同一組 `LITELLM_API_BASE`／`LITELLM_API_KEY`／`MCP_SERVER_URL`），
在 `code-sample/` 底下：

```bash
adk web _solutions
```

瀏覽器選 `leave_agent_solution`，測：

```
幫我處理 ../lab1_leave_agent/sample_data/請假單-範例.png
```

預期輸出的 JSON：姓名「小明」、部門「IT」、職位「前端工程師」、
請假類型「病假」、請假期間 1140730–1140805 共 7 天、原因「車禍手術」。

選 `meeting_secretary_solution`，測：

```
幫我處理 ../lab2_meeting_secretary/sample_data/會議記錄-範例.txt
```

預期輸出一份包含時間 7/30 14:00–15:00、地點 3 樓會議室、
與會人員小明、小華的會議通知。

## 兩邊都能正常跑，代表：

- MCP server 的 `ocr_image`／`read_document` 都能被遠端呼叫成功
- LiteLLM Proxy 能正確路由到 `gemma4:26b`（地端）跟
  `claude-sonnet-4-6`（雲端）兩個模型
- 整條「本機檔案 → base64 → MCP 工具 → LLM 整理 → 結構化輸出」的鏈路沒問題

代表可以放心把 `lab1_leave_agent/`、`lab2_meeting_secretary/`、`skills/`
這幾個資料夾（不含 `_solutions/`）發給學員了。
