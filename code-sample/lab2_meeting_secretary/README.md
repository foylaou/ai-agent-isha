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
把 `../skills/meeting-secretary.SKILL.md` 整份餵給它，請它照著規格
把 `INSTRUCTION` 補完。

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

## 進階挑戰（選做，對應投影片 A2A 段落）

- 加一個「行事曆 Agent」，會議秘書先問它某個時段是否有空，沒空的話
  改問使用者要不要換時間，體驗 Agent 對 Agent 的溝通（A2A）
