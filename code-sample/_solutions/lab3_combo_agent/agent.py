"""
實做三：請假 → 交接會議秘書 —— 完整參考解答（講師驗證用，不要給學員看）

跟 ../../lab3_combo_agent/agent.py 是同一份骨架，差別只有 Step 2
（meeting_step）的 INSTRUCTION 已經照
../../skills/leave-to-meeting-combo.SKILL.md 補完。
"""

import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams,
)
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

# 這裡在 code-sample/_solutions/lab3_combo_agent/，.env 在 code-sample/
# 底下，所以要往上三層（跟學員版的 agent.py 往上兩層不一樣，因為多了
# _solutions/ 這層）
load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]

LITELLM_API_BASE = os.environ["LITELLM_API_BASE"].rstrip("/")
if not LITELLM_API_BASE.endswith("/v1"):
    LITELLM_API_BASE += "/v1"


def _model(default_name: str) -> LiteLlm:
    model_name = os.environ.get("MODEL_NAME", default_name)
    return LiteLlm(
        model=f"openai/{model_name}",
        api_base=LITELLM_API_BASE,
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

LEAVE_STEP_INSTRUCTION = """
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

leave_step = Agent(
    name="leave_step",
    model=_model("gemma4:26b"),
    instruction=LEAVE_STEP_INSTRUCTION,
    tools=[load_file_as_base64, workshop_tools],
    output_key="leave_info",
)

MEETING_STEP_INSTRUCTION = """
你是「請假交接會議秘書」，任務是根據上一步驟的請假擷取結果，生成一份
請假交接會議通知。

# 你會拿到的資料
{leave_info}

這是上一步驟（請假代理人）存進 state 的 JSON 字串，包含姓名、部門、
職位、請假類型、請假時間、請假原因。直接讀這段內容，不要呼叫任何工具、
不要重新擷取一次請假單。

# 操作步驟
1. 從 {leave_info} 讀出請假人姓名、請假期間、請假原因。
2. 交接窗口是誰、交接會議的時間地點，這些資訊不在 {leave_info} 裡，
   一定要反問使用者，不可以自己編造。
3. 拿到使用者回覆後，用下面的格式生成正式的會議通知。

# 輸出格式
（下面 <角括號> 是要你自己填的內容，不是變數，照格式輸出文字就好）

【會議通知】<姓名> 請假交接會議

時間：<日期> <開始時間>–<結束時間>
地點：<地點>
與會人員：<請假人>、<交接窗口>

交接事項：
- 請假期間：<leave_info 裡的請假時間>
- 請假原因：<leave_info 裡的請假原因>
- <其他交接重點>
"""

meeting_step = Agent(
    name="meeting_step",
    model=_model("claude-sonnet-4-6"),
    instruction=MEETING_STEP_INSTRUCTION,
    output_key="meeting_notice",
)

root_agent = SequentialAgent(
    name="leave_to_meeting_combo_solution",
    sub_agents=[leave_step, meeting_step],
    description="請假單擷取（Step 1）→ 自動生成交接會議通知（Step 2）",
)
