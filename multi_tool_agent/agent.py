from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


root_agent = Agent(
    name="base_agent",
    model=LiteLlm(
        model="ollama/qwen2.5vl:7b",
        api_base="http://140.116.8.202:30192", # 如果要用本機的話不用加這個
    ),
    instruction=(
        "You are an expert web automation agent. "
        "You can navigate to web pages, take screenshots, fill forms, and click elements. "
        "When asked to interact with a web page, use the appropriate browser tools. "
        "If you don't know something, you can always google it using the browser tools"
    ),
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "@playwright/mcp@latest",
                        "--vision",
                    ],
                ),
                timeout=60, # mcp，有需要可以在加長
            )
        )
    ]
)

