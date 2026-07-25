---
name: leave-agent
description: 讀取請假單（PDF／PNG 掃描檔或 DOCX），擷取人事時地物並輸出成結構化 JSON
---

# 請假代理人 Skill

## Instructions（操作步驟）

1. 判斷使用者提供的請假單是圖片／PDF 掃描檔，還是 DOCX／文字檔
   - 圖片或 PDF → 呼叫 MCP 工具 `ocr_image`，取得 OCR 純文字
   - DOCX 或純文字 → 呼叫 MCP 工具 `read_document`，取得純文字
2. 從純文字中擷取以下欄位：姓名、部門、職位、請假類型、請假起訖日期、
   請假天數、請假原因
3. 缺漏的欄位一律填 `null`，不要自己編造內容
4. 用下方「輸出格式」把結果整理成 JSON 字串回覆使用者

## 輸出格式

```json
{
  "姓名": "string | null",
  "部門": "string | null",
  "職位": "string | null",
  "請假類型": "string | null",
  "請假時間": {
    "起": "YYYMMDD | null",
    "迄": "YYYMMDD | null",
    "共": "string | null"
  },
  "請假原因": "string | null"
}
```

## Examples（範例）

輸入（OCR 後的純文字，來自 `sample_data/請假單-範例.png`）：

```
請假條
姓名：小明　部門：IT　職位：前端工程師　日期：7/30
請假類型：☑病假
請假時間：自 114 年 7 月 30 日 — 114 年 8 月 5 日　共 7 天
請假原因：車禍手術
```

預期輸出：

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
