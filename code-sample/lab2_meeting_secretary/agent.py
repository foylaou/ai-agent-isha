"""
實做二：會議秘書

這份骨架已經幫你接好：
- 一個本機工具 load_file_as_base64（讀本機檔案、轉成 base64，MCP 工具要吃這個格式）
- 遠端 MCP 工具 read_document（講師部署，讀 DOCX／文字檔）

你的任務只有一個：把下面 instruction 的 TODO 部分描述清楚，
讓 Agent 知道怎麼把會議內容整理成正式的會議通知。

建議做法：把 ../skills/meeting-secretary.SKILL.md 整份丟給你的 AI 編輯器，
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
    """讀取本機檔案，回傳 base64 編碼字串，給 read_document 使用。

    Args:
        path: 本機檔案路徑，例如 sample_data/會議記錄-範例.txt

    Returns:
        檔案內容的 base64 編碼字串
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


workshop_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_SERVER_URL),
    tool_filter=["read_document"],
)

# TODO(學員)：
# 參考 ../skills/meeting-secretary.SKILL.md，把下面補成完整的 instruction。
# 至少要涵蓋：
#   1. 使用者可能直接貼文字，也可能給檔案路徑（這時才需要
#      load_file_as_base64 + read_document）
#   2. 要擷取哪些欄位（主題、時間、地點、與會人員、決議、待辦事項）
#   3. 欄位缺漏時要反問使用者，不要編造時間或地點
#   4. 輸出格式要求（正式會議通知的排版）
INSTRUCTION = """
TODO: 描述會議秘書該做的事情。
"""

root_agent = Agent(
    name="meeting_secretary",
    model="gemini-2.5-flash",
    instruction=INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
)
