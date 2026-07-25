"""
工作坊共用 MCP Server。

提供兩個工具給學員的 Agent 呼叫：
- read_document：讀取 DOCX／純文字檔內容
- ocr_image：對 PNG／JPG／PDF 掃描檔做 OCR，回傳純文字

這個 server 由講師端統一部署（Docker），學員不需要在自己電腦上安裝
tesseract 或 poppler，只要把 MCP_SERVER_URL 指到這裡即可。
"""

import base64
import io

import pytesseract
from docx import Document
from mcp.server.fastmcp import FastMCP
from pdf2image import convert_from_bytes
from PIL import Image

# host/port/streamable_http_path 要在建構子傳（**settings），FastMCP.run()
# 本身不吃這幾個參數 -- 這幾個剛好也是預設值，寫出來只是為了明確、不依賴預設
mcp = FastMCP(
    name="workshop-tools",
    host="0.0.0.0",
    port=8000,
    streamable_http_path="/mcp",
)


@mcp.tool()
def read_document(file_base64: str) -> str:
    """讀取 DOCX 或純文字檔案的內容。

    Args:
        file_base64: 檔案內容的 Base64 編碼字串（.docx 或 .txt）

    Returns:
        檔案的純文字內容
    """
    raw = base64.b64decode(file_base64)

    try:
        doc = Document(io.BytesIO(raw))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception:
        # 不是合法的 docx，當作純文字處理
        return raw.decode("utf-8", errors="replace")


@mcp.tool()
def ocr_image(file_base64: str, filename: str = "image.png") -> str:
    """對圖片或 PDF 掃描檔做 OCR，回傳辨識出的文字。

    支援 PNG、JPG、PDF（PDF 會逐頁 OCR 後合併）。

    Args:
        file_base64: 圖片或 PDF 檔案內容的 Base64 編碼字串
        filename: 原始檔名，用來判斷副檔名（.pdf 會走 PDF 流程）

    Returns:
        OCR 辨識出的文字內容
    """
    raw = base64.b64decode(file_base64)

    if filename.lower().endswith(".pdf"):
        pages = convert_from_bytes(raw)
        texts = [pytesseract.image_to_string(page, lang="chi_tra+eng") for page in pages]
        return "\n\n".join(texts)

    image = Image.open(io.BytesIO(raw))
    return pytesseract.image_to_string(image, lang="chi_tra+eng")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
