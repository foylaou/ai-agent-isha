# 實做一：請假代理人

**目標**：學員讀取一張請假單（PDF／PNG 掃描檔或 DOCX），自動擷取人事時地物，
輸出成結構化 JSON。

## 這份骨架幫你做好了什麼

- 本機工具 `load_file_as_base64`：讀本機檔案轉 base64
- 已經接好講師部署的遠端 MCP 工具：`ocr_image`、`read_document`
- 已經接好講師部署的 LiteLLM Proxy（預設用地端小模型 `gemma4:26b`，
  這個任務欄位固定、夠簡單，不需要大模型）
- `skills/leave-agent.SKILL.md`：完整規格（欄位、輸出格式、範例）

## 你要做的事

`agent.py` 裡的 `INSTRUCTION` 目前只有一行 TODO。打開你的 AI 編輯器
（Cursor／Copilot／Claude Code 都可以），把 `../skills/leave-agent.SKILL.md`
整份餵給它，請它照著規格把 `INSTRUCTION` 補完。

## 設定與執行

在 `code-sample/` 底下（跟這個資料夾同一層）：

```bash
pip install -r lab1_leave_agent/requirements.txt

# 如果還沒設定過共用的 .env（見上層 README「事前準備」）：
cp .env.example .env
# 編輯 .env：LITELLM_API_BASE／LITELLM_API_KEY／MCP_SERVER_URL 用講師當天公布的值

adk web .
```

瀏覽器打開 ADK 的網頁介面後，選擇 `leave_agent`，輸入：

```
幫我處理 lab1_leave_agent/sample_data/請假單-範例.png
```

## 驗收標準

輸出的 JSON 應包含：姓名「小明」、部門「IT」、職位「前端工程師」、
請假類型「病假」、請假期間 114/07/30–114/08/05 共 7 天、原因「車禍手術」。
缺漏欄位要是 `null`，不能是編造的內容。

## 進階挑戰（選做）

- 讓 Agent 在欄位缺漏時主動反問使用者，而不是直接留 `null`
- 支援一次處理多張請假單，回傳 JSON 陣列
- 在 `.env` 加 `MODEL_NAME=claude-sonnet-4-6`，跟預設的地端小模型比較
  結果品質與速度差異
