# 實做二：會議秘書

**目標**：學員把開會內容（文字或檔案）交給 Agent，自動整理成人事時地物
清楚的正式會議通知。

## 這份骨架幫你做好了什麼

- 本機工具 `load_file_as_base64`：讀本機檔案轉 base64
- 已經接好講師部署的遠端 MCP 工具：`read_document`
- 已經接好講師部署的 LiteLLM Proxy（預設用中大型模型
  `claude-sonnet-4-6`，這個任務要組織語言、掌握語境，需要能力較強的模型）
- `skills/meeting-secretary.SKILL.md`：完整規格（欄位、輸出格式、範例）

## 你要做的事

`agent.py` 裡的 `INSTRUCTION` 目前只有一行 TODO。打開你的 AI 編輯器，
把下面這段 prompt 複製貼給它：

```
請幫我完成 lab2_meeting_secretary/agent.py 裡 meeting_secretary 的
INSTRUCTION。

規格請看 skills/meeting-secretary.SKILL.md，裡面有完整的
Instructions、輸出格式、Examples，照著那份規格把 INSTRUCTION 補完。

要求：
- 只修改 INSTRUCTION 這個變數的內容，不要動其他程式碼（工具、模型
  設定都已經接好了）
- instruction 裡不要用花括號 {像這樣} 當示意用的空格——ADK 會把
  instruction 裡任何 {word} 當成必須存在的 session state 變數去查，
  查不到會直接丟 KeyError 讓 Agent 掛掉。範例格式裡要留空格請用
  <角括號>
- 缺漏的關鍵欄位（時間、地點）要設計成反問使用者，不要自己編造
- 完成後跑 python3 -m py_compile lab2_meeting_secretary/agent.py
  確認語法沒問題
```

## 設定與執行

在 `code-sample/` 底下（跟這個資料夾同一層）：

```bash
pip install -r lab2_meeting_secretary/requirements.txt

# 如果還沒設定過共用的 .env（見上層 README「事前準備」）：
cp .env.example .env
# 編輯 .env：LITELLM_API_BASE／LITELLM_API_KEY／MCP_SERVER_URL 用講師當天公布的值

adk web .
```

瀏覽器打開 ADK 的網頁介面後，選擇 `meeting_secretary`，可以直接貼文字：

```
7/30 下午 2 點到 3 點，在 3 樓會議室，跟小明、小華討論下一季文件生成專案。
決定先做請假單 OCR，小明負責串 MCP 工具，小華負責寫 Agent instruction，
下週三前要有 demo。
```

或請它讀檔案：

```
幫我處理 lab2_meeting_secretary/sample_data/會議記錄-範例.txt
```

## 驗收標準

輸出要包含：主題、時間（7/30 14:00–15:00）、地點（3 樓會議室）、
與會人員（小明、小華）、決議事項、以及帶負責人的待辦事項清單。

## 更多測試情境

上面那個範例時間地點都齊全，Agent 不用反問就能生成。再測這個：

```
幫我處理 lab2_meeting_secretary/sample_data/會議記錄-範例2-缺資訊.txt
```

這份內容故意沒提到時間、地點。**預期 Agent 要反問你**（例如「請問會議
時間跟地點是？」），而不是自己編一個時間地點出來就直接生成通知——這是
驗證 SKILL.md「關鍵欄位缺漏要反問，不要編造」那條規則最直接的測試。
回答後應該才會拿到完整的會議通知。

## 進階挑戰（選做，對應投影片 A2A 段落）

- 加一個「行事曆 Agent」，會議秘書先問它某個時段是否有空，沒空的話
  改問使用者要不要換時間，體驗 Agent 對 Agent 的溝通（A2A）
