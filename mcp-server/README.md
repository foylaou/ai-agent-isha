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

回 `406 Not Acceptable` + `"Client must accept text/event-stream"` 的 JSON-RPC
錯誤是正常的，代表 server 有在跑，只是這個 GET 沒帶對 header。想看到真正
成功的回應，要用 POST 帶正確 header 打 `initialize`：

```bash
curl -i http://localhost:8000/mcp \
  -H "Accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2026-03-26","capabilities":{},"clientInfo":{"name":"curl-test","version":"0"}}}'
```

回 `200 OK`、`content-type: text/event-stream`，內容帶
`"serverInfo":{"name":"workshop-tools",...}` 才代表真正沒問題。

## 換掉伺服器位址時要注意

- 如果是內網／筆電熱點，記得開對外的 port
- 學員端用的是 `StreamableHTTPConnectionParams`，URL 要包含 `/mcp` 這個 path

## nginx 反向代理

streamable-http 本質是長連線的 `text/event-stream`，nginx 預設的緩衝／逾時
設定會把它悶住（回應卡住不吐、或連線被提早斷掉），所以重點都在「關掉
buffering、拉長 timeout、保留串流相關的 header」：

```nginx
server {
    listen 443 ssl;
    server_name mcp.example.com;

    # ssl_certificate ...;
    # ssl_certificate_key ...;

    location /mcp {
        proxy_pass http://127.0.0.1:8888/mcp;

        proxy_http_version 1.1;
        proxy_set_header Connection "";        # 保持長連線，不要被當一般請求關掉
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_buffering off;                   # 關鍵：SSE 一定要關 buffering
        proxy_cache off;
        proxy_read_timeout 3600s;              # 長對話／慢工具（OCR）要給夠時間
        proxy_send_timeout 3600s;
    }
}
```

代理設好後，用同一組 `Accept: application/json, text/event-stream` 的
`curl -X POST` 打公開網址測一次（見上面「健康檢查」），跟直接打
`10.6.20.11:8888` 的結果應該一樣，才代表 nginx 沒有把串流悶住。
