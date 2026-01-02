from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import calculator_tool, datetime_tool

SYSTEM_PROMPT = """
You are an AI assistant.

You can answer questions using your own knowledge.
You have access to ONLY TWO tools called Calculator and CurrentDateTime.

Use the Calculator tool ONLY when the user asks a mathematical question
that requires a numeric calculation.

Use the CurrentDateTime tool ONLYwhen the user asks questions about the current time or date.

If the question is not a mathematical expressions or current date/time question
DO NOT use any tool and answer directly.
"""

def create_agent():
    llm = ChatOpenAI(
        model= "gpt-3.5-turbo",
        temperature= 0
    )

    TOOLS = [calculator_tool,datetime_tool]
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
