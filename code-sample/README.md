# 實做教材：Google ADK + MCP

對應簡報 Part 2「使用 AI」的兩個實做。目標不是叫你手刻 OCR，而是練習
**用 AI 編輯器（vibe coding）把 Agent 的 instruction 寫完整，並學會怎麼
接上別人架好的 MCP 工具**。

## 架構

```
講師端：mcp-server/（Docker，已部署好，當天給你網址）
  ├─ ocr_image      對圖片／PDF 掃描檔做 OCR
  └─ read_document   讀 DOCX／文字檔內容

你要寫的：
  lab1_leave_agent/       請假代理人：擷取請假單人事時地物
  lab2_meeting_secretary/ 會議秘書：開會內容 → 生成會議通知
```

兩個實做的 `agent.py` 都已經把 MCP 工具接好了，唯一要做的是把
`INSTRUCTION` 裡的 TODO 描述清楚——這就是「Skill」：把一次性的 prompt
變成有名字、有規則、可重複呼叫的東西（詳見簡報「從 Prompt 到 Skill」）。

## 事前準備

1. Python 3.10+
2. VS Code（建議用本機版，不要用線上版，才能跟 AI 編輯器整合順暢）
3. `pip install google-adk`
4. 一組 [Gemini API Key](https://aistudio.google.com/apikey)
5. 講師當天公布的 MCP server 網址

## 資料夾

| 路徑 | 內容 |
|---|---|
| `skills/` | 兩個 Skill 的規格文件（SKILL.md），寫 instruction 前先讀這個，或直接餵給 AI 編輯器 |
| `lab1_leave_agent/` | 實做一：請假代理人 |
| `lab2_meeting_secretary/` | 實做二：會議秘書 |

## 建議流程

1. 打開 `skills/leave-agent.SKILL.md`，看懂要擷取哪些欄位、輸出長怎樣
2. 打開 `lab1_leave_agent/agent.py`，把 SKILL.md 內容連同這個檔案一起
   丟給 AI 編輯器，請它幫你把 `INSTRUCTION` 補完
3. `adk web .`，實際測試、跟 AI 一起除錯
4. 完成後照同樣流程做 `lab2_meeting_secretary/`
5. 有餘力的話挑戰兩邊 README 裡的「進階挑戰」
