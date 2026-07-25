# 工作坊共用 MCP Server（講師端部署）

提供兩個工具，給學員在「請假代理人」「會議秘書」兩個實做裡透過 MCP 呼叫：

- `read_document`：讀 DOCX／純文字內容
- `ocr_image`：對 PNG／JPG／PDF 掃描檔做 OCR（含繁體中文）

學員不需要在自己電腦裝 tesseract／poppler，只要拿到這個 server 的網址即可。

## 建置與啟動

```bash
docker build -t workshop-mcp-server .
docker run -d --name workshop-mcp -p 8000:8000 --restart unless-stopped workshop-mcp-server
```

啟動後，MCP endpoint 在：

```
http://<伺服器位址>:8000/mcp
```

當天把這個網址（或內網位址）直接告訴學員，讓他們填進自己 `agent.py` 旁的
`.env` 的 `MCP_SERVER_URL`。

## 健康檢查

```bash
curl -i http://localhost:8000/mcp
```

有回應（非連線失敗）就代表 server 正常在跑。

## 換掉伺服器位址時要注意

- 如果是內網／筆電熱點，記得開對外的 port（8000）
- 如果前面有反向代理（nginx／Caddy），要保留 streamable-http 需要的
  `Content-Type: text/event-stream` 與長連線，不要幫它加 buffering
- 學員端用的是 `StreamableHTTPConnectionParams`，URL 要包含 `/mcp` 這個 path
