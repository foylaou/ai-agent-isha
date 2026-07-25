"""
實做一：請假代理人 —— 完整參考解答（講師驗證用，不要給學員看）

跟 ../../lab1_leave_agent/agent.py 是同一份骨架，差別只有 INSTRUCTION
已經照 ../../skills/leave-agent.SKILL.md 補完，用來驗證 MCP server／
LiteLLM Proxy 整條線是否真的打通。
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

# 這裡在 code-sample/_solutions/lab1_leave_agent/，.env 在 code-sample/ 底下，
# 所以要往上三層（跟學員版的 agent.py 往上兩層不一樣，因為多了 _solutions/ 這層）
load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]

MODEL_NAME = os.environ.get("MODEL_NAME", "gemma4:26b")

model = LiteLlm(
    model=f"litellm_proxy/{MODEL_NAME}",
    api_base=os.environ["LITELLM_API_BASE"],
    api_key=os.environ["LITELLM_API_KEY"],
)


def load_file_as_base64(path: str) -> str:
    """讀取本機檔案，回傳 base64 編碼字串，給 ocr_image／read_document 使用。

    Args:
        path: 本機檔案路徑，例如 ../../lab1_leave_agent/sample_data/請假單-範例.png

    Returns:
        檔案內容的 base64 編碼字串
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


workshop_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_SERVER_URL),
    tool_filter=["ocr_image", "read_document"],
)

INSTRUCTION = """
你是「請假代理人」，任務是讀取請假單並擷取結構化資訊，回傳 JSON。

# 你有的工具
- load_file_as_base64(path)：讀本機檔案，轉成 base64 字串
- ocr_image(file_base64, filename)：對圖片／PDF 掃描檔做 OCR，回傳純文字
- read_document(file_base64)：讀 DOCX／純文字檔案，回傳純文字

# 操作步驟
1. 使用者給你一個檔案路徑時，先呼叫 load_file_as_base64 取得 base64 內容。
2. 依副檔名決定下一步：
   - .png / .jpg / .jpeg / .pdf → 呼叫 ocr_image(file_base64=..., filename=原始檔名)
   - .docx / .txt → 呼叫 read_document(file_base64=...)
3. 從拿到的純文字中擷取以下欄位：姓名、部門、職位、請假類型、
   請假起訖日期（轉成 YYYMMDD 格式的民國年）、請假天數、請假原因。
4. 任何欄位如果在文字裡找不到，一律填 null，不可以自己編造內容。
5. 只回傳下面格式的 JSON 字串，不要加其他說明文字或 markdown code fence。

# 輸出格式
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
"""

root_agent = Agent(
    name="leave_agent_solution",
    model=model,
    instruction=INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
)
