"""
實做二：會議秘書 —— 完整參考解答（講師驗證用，不要給學員看）

跟 ../../lab2_meeting_secretary/agent.py 是同一份骨架，差別只有
INSTRUCTION 已經照 ../../skills/meeting-secretary.SKILL.md 補完，
用來驗證 MCP server／LiteLLM Proxy 整條線是否真的打通。
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

# 這裡在 code-sample/_solutions/lab2_meeting_secretary/，.env 在 code-sample/
# 底下，所以要往上三層（跟學員版的 agent.py 往上兩層不一樣，因為多了
# _solutions/ 這層）
load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]

MODEL_NAME = os.environ.get("MODEL_NAME", "claude-sonnet-4-6")

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
    """讀取本機檔案，回傳 base64 編碼字串，給 read_document 使用。

    Args:
        path: 本機檔案路徑，例如 ../../lab2_meeting_secretary/sample_data/會議記錄-範例.txt

    Returns:
        檔案內容的 base64 編碼字串
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


workshop_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_SERVER_URL),
    tool_filter=["read_document"],
)

INSTRUCTION = """
你是「會議秘書」，任務是把會議內容整理成正式的會議通知。

# 你有的工具
- load_file_as_base64(path)：讀本機檔案，轉成 base64 字串
- read_document(file_base64)：讀 DOCX／純文字檔案，回傳純文字

# 操作步驟
1. 使用者可能直接貼會議內容文字，也可能給檔案路徑：
   - 直接貼文字 → 不用呼叫任何工具，直接處理
   - 給檔案路徑 → 先呼叫 load_file_as_base64，再呼叫 read_document 取得純文字
2. 從內容中擷取：會議主題、時間、地點、與會人員、決議事項／待辦事項。
3. 如果時間或地點這類關鍵欄位缺漏，要反問使用者，不可以自己編造；
   其他次要欄位缺漏可以留白。
4. 用下面的格式生成一份正式的會議通知文字回覆使用者。

# 輸出格式
（下面 <角括號> 是要你自己填的內容，不是變數，照格式輸出文字就好）

【會議通知】<會議主題>

時間：<日期> <開始時間>–<結束時間>
地點：<地點>
與會人員：<人員清單，以頓號分隔>

討論重點／決議：
- <重點>

待辦事項：
- <待辦事項>（負責人：<姓名>）
"""

root_agent = Agent(
    name="meeting_secretary_solution",
    model=model,
    instruction=INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
)
