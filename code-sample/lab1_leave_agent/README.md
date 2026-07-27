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
（Cursor／Copilot／Claude Code 都可以），把下面這段 prompt 複製貼給它：

```
請幫我完成 lab1_leave_agent/agent.py 裡 leave_agent 的 INSTRUCTION。

規格請看 skills/leave-agent.SKILL.md，裡面有完整的 Instructions、
輸出格式、Examples，照著那份規格把 INSTRUCTION 補完。

要求：
- 只修改 INSTRUCTION 這個變數的內容，不要動其他程式碼（工具、模型
  設定都已經接好了）
- instruction 裡不要用花括號 {像這樣} 當示意用的空格——ADK 會把
  instruction 裡任何 {word} 當成必須存在的 session state 變數去查，
  查不到會直接丟 KeyError 讓 Agent 掛掉。範例格式裡要留空格請用
  <角括號>
- 完成後跑 python3 -m py_compile lab1_leave_agent/agent.py 確認語法
  沒問題
```

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

## 更多測試情境

上面那張圖只測到 `ocr_image` 這條路。再測下面兩個，確認
`read_document` 那條路跟「缺漏欄位」的處理也對：

```
幫我處理 lab1_leave_agent/sample_data/請假單-範例2.txt
```

這是純文字檔（走 `read_document`，不是 OCR），欄位齊全，預期：姓名
「小華」、部門「業務部」、職位「業務專員」、事假、114/08/15–114/08/15
共 1 天、原因「家中有事」。

```
幫我處理 lab1_leave_agent/sample_data/請假單-範例3-缺欄位.txt
```

這份故意沒寫職位、沒寫請假原因。預期姓名「小美」、部門「財務部」、
特休、114/09/01–114/09/03 共 3 天，**職位跟請假原因要是 `null`**，
不能自己編一個出來——這是驗證 SKILL.md「缺漏欄位不要編造」那條規則
最直接的測試。

## 進階挑戰（選做）

- 讓 Agent 在欄位缺漏時主動反問使用者，而不是直接留 `null`
- 支援一次處理多張請假單，回傳 JSON 陣列
- 在 `.env` 加 `MODEL_NAME=claude-sonnet-4-6`，跟預設的地端小模型比較
  結果品質與速度差異
