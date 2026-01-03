from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import calculator_tool, datetime_tool, weather_tool

SYSTEM_PROMPT = """
You are an AI assistant.

You can answer questions using your own knowledge.
You have access to ONLY TREE tools called Calculator, CurrentDateTime and Weather.

Use the calculator_tool ONLY when the user asks a mathematical question
that requires a numeric calculation (including trigonometry questions). Always resolve mathematical questions with this tool.

Use the datetime_tool tool ONLY when the user asks questions about the current time or date.

Use the weather_tool tool ONLY when only when the user asks questions about the weather/temperature in a particular city.

If the question is not a mathematical expressions or current date/time question or a weather question
DO NOT use any tool and answer directly.
"""

def create_agent():
    llm = ChatOpenAI(
        model= "gpt-3.5-turbo",
        temperature= 0
    )

    TOOLS = [calculator_tool,datetime_tool,weather_tool]
    
    agent = initialize_agent(
        tools= TOOLS,
        llm= llm,
        agent= AgentType.OPENAI_FUNCTIONS,
        verbose= True,
        agent_kwargs= {
            "system_message": SYSTEM_PROMPT
        }
    )

    return agent
