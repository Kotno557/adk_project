from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


root_agent = Agent(
    name="base_agent",
    model=LiteLlm(
        model="ollama/qwen2.5vl:7b",
        api_base="http://140.116.8.202:30192", # 如果要用本機的話不用加這個
    ),
    description=(
        "Agent to answer questions about the anything."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about anything."
    ),
)