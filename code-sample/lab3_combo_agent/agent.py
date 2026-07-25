"""
實做三：請假 → 交接會議秘書（把 lab1、lab2 用 SequentialAgent 串連起來）

對應投影片「Sequential Agent」：把兩個 Skill 接成一條 pipeline，
上一步的輸出透過 output_key 存進 session state，下一步的 instruction
直接用 {state_key} 讀出來，不用自己手動傳遞。

Step 1（leave_step）：跟 lab1 完全一樣的請假單擷取邏輯，已經幫你寫好，
不用再改一次。
Step 2（meeting_step）：這才是新的部分，要你把 instruction 補完——
根據 Step 1 存進 state 的 {leave_info}，生成一份「請假交接會議通知」。

建議做法：把 ../skills/leave-to-meeting-combo.SKILL.md 丟給你的 AI
編輯器，請它幫你把 meeting_step 的 INSTRUCTION 補完。
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

# .env 放在 code-sample/ 底下，三個 lab 共用（LiteLLM 的 key、MCP 位址）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

MCP_SERVER_URL = os.environ["MCP_SERVER_URL"]  # 例如 http://<講師給的位址>:8000/mcp

# LiteLLM 走 openai-compatible 路徑時，base URL 一定要含 /v1（openai SDK
# 不會自己補），這裡自動補上，不用依賴 .env 填得剛好對
LITELLM_API_BASE = os.environ["LITELLM_API_BASE"].rstrip("/")
if not LITELLM_API_BASE.endswith("/v1"):
    LITELLM_API_BASE += "/v1"


def _model(default_name: str) -> LiteLlm:
    """建立一個指向講師 LiteLLM Proxy 的模型，預設模型可用 .env 的 MODEL_NAME 覆蓋。"""
    model_name = os.environ.get("MODEL_NAME", default_name)
    return LiteLlm(
        model=f"openai/{model_name}",
        api_base=LITELLM_API_BASE,
        api_key=os.environ["LITELLM_API_KEY"],
    )


def load_file_as_base64(path: str) -> str:
    """讀取本機檔案，回傳 base64 編碼字串，給 ocr_image／read_document 使用。

    Args:
        path: 本機檔案路徑，例如 ../lab1_leave_agent/sample_data/請假單-範例.png

    Returns:
        檔案內容的 base64 編碼字串
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


workshop_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_SERVER_URL),
    tool_filter=["ocr_image", "read_document"],
)

# Step 1：跟 lab1_leave_agent 完全一樣的邏輯，多了 output_key="leave_info"，
# 執行完會自動把最終回覆（那段 JSON 字串）寫進 session state 給 Step 2 讀。
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

# TODO(學員)：
# 參考 ../skills/leave-to-meeting-combo.SKILL.md，把下面補成完整的
# instruction。至少要涵蓋：
#   1. {leave_info} 是 Step 1 存進 state 的 JSON 字串（請假人、部門、
#      請假期間、原因），直接讀就好，不用再呼叫任何工具
#   2. 誰負責交接、會議時間地點——這些 {leave_info} 沒有的資訊要反問
#      使用者，不可以自己編造
#   3. 輸出格式比照 ../skills/meeting-secretary.SKILL.md 的會議通知格式，
#      但主題要是「<姓名> 請假交接會議」（注意：instruction 裡示意用的
#      空格要用 <角括號>，不要用 {花括號}——ADK 會把 {word} 當成 session
#      state 變數去查，查不到會直接 KeyError）
MEETING_STEP_INSTRUCTION = """
TODO: 根據 {leave_info} 生成一份請假交接會議通知。
"""

meeting_step = Agent(
    name="meeting_step",
    model=_model("claude-sonnet-4-6"),
    instruction=MEETING_STEP_INSTRUCTION,
    output_key="meeting_notice",
)

root_agent = SequentialAgent(
    name="leave_to_meeting_combo",
    sub_agents=[leave_step, meeting_step],
    description="請假單擷取（Step 1）→ 自動生成交接會議通知（Step 2）",
)
