"""
實做一：請假代理人

這份骨架已經幫你接好：
- 一個本機工具 load_file_as_base64（讀本機檔案、轉成 base64，MCP 工具要吃這個格式）
- 遠端 MCP 工具 ocr_image / read_document（講師部署，跑真正的 OCR）

你的任務只有一個：把下面 instruction 的 TODO 部分描述清楚，
讓 Agent 知道怎麼把請假單內容擷取成結構化 JSON。

建議做法：把 ../skills/leave-agent.SKILL.md 整份丟給你的 AI 編輯器，
請它依照裡面的 Instructions／輸出格式／Examples 幫你把這段 instruction 補完。
"""

import base64
import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams,
)
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

load_dotenv()

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]  # 例如 http://<講師給的位址>:8000/mcp


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
    model="gemini-2.5-flash",
    instruction=INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
)
