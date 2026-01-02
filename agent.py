from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import calculator_tool

SYSTEM_PROMPT = """
You are an AI assistant.

You can answer questions using your own knowledge.
You have access to ONLY ONE tool called Calculator.

Use the Calculator tool ONLY when the user asks a mathematical question
that requires a numeric calculation.

If the question is not a mathematical expressions
DO NOT use any tool and answer directly.
"""

def create_agent():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    agent = initialize_agent(
        tools=[calculator_tool],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        agent_kwargs={
            "system_message": SYSTEM_PROMPT
        }
    )

    return agent
