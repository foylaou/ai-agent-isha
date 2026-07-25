"""
實做一：請假代理人

這份骨架已經幫你接好：
- 一個本機工具 load_file_as_base64（讀本機檔案、轉成 base64，MCP 工具要吃這個格式）
- 遠端 MCP 工具 ocr_image / read_document（講師部署，跑真正的 OCR）
- 透過講師部署的 LiteLLM Proxy 呼叫模型（統一管理 API Key、記錄呼叫）

你的任務只有一個：把下面 instruction 的 TODO 部分描述清楚，
讓 Agent 知道怎麼把請假單內容擷取成結構化 JSON。

建議做法：把 ../skills/leave-agent.SKILL.md 整份丟給你的 AI 編輯器，
請它依照裡面的 Instructions／輸出格式／Examples 幫你把這段 instruction 補完。
"""

import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams,
)
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

# .env 放在 code-sample/ 底下，兩個 lab 共用（LiteLLM 的 key、MCP 位址）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]  # 例如 http://<講師給的位址>:8000/mcp

# 請假單擷取是簡單、欄位固定的任務，用小型／地端模型就夠（見投影片
# 「以文件生成為例：該選哪一種？」）。想比較雲端模型的話，在 .env 加一行
# MODEL_NAME=claude-sonnet-4-6 覆蓋這個預設值即可。
MODEL_NAME = os.environ.get("MODEL_NAME", "gemma4:26b")

# LiteLLM 走 openai-compatible 路徑時，base URL 一定要含 /v1（openai SDK
# 不會自己補），這裡自動補上，不用依賴 .env 填得剛好對
LITELLM_API_BASE = os.environ["LITELLM_API_BASE"].rstrip("/")
if not LITELLM_API_BASE.endswith("/v1"):
    LITELLM_API_BASE += "/v1"

model = LiteLlm(
    model=f"openai/{MODEL_NAME}",
    api_base=LITELLM_API_BASE,
    api_key=os.environ["LITELLM_API_KEY"],
)


def load_file_as_base64(path: str) -> str:
    """讀取本機檔案，回傳 base64 編碼字串，給 ocr_image／read_document 使用。

    Args:
        path: 本機檔案路徑，例如 sample_data/請假單-範例.png

    Returns:
        檔案內容的 base64 編碼字串
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


workshop_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_SERVER_URL),
    tool_filter=["ocr_image", "read_document"],
)

# TODO(學員)：
# 參考 ../skills/leave-agent.SKILL.md，把下面補成完整的 instruction。
# 至少要涵蓋：
#   1. 拿到檔案路徑後，先呼叫 load_file_as_base64 轉成 base64
#   2. 什麼時候該呼叫 ocr_image、什麼時候該呼叫 read_document
#   3. 要擷取哪些欄位（姓名、部門、職位、請假類型、起訖日期、天數、原因）
#   4. 缺漏欄位怎麼處理（提示：不要編造）
#   5. 輸出格式要求
INSTRUCTION = """
TODO: 描述請假代理人該做的事情。
"""

root_agent = Agent(
    name="leave_agent",
    model=model,
    instruction=INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
)
