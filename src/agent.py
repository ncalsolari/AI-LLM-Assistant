from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools import calculator_tool, datetime_tool, weather_tool

SYSTEM_PROMPT = """
You are an AI assistant.

You can answer questions using your own knowledge.
You have access to ONLY THREE tools called Calculator, CurrentDateTime and Weather.

Use the calculator_tool ONLY when the user asks a mathematical question
that requires a numeric calculation (including trigonometry questions).

Use the datetime_tool ONLY when the user asks questions about the current time or date.

Use the weather_tool ONLY when the user asks questions about the weather/temperature in a particular city.

If the question is not related to math, date/time, or weather,
DO NOT use any tool and answer directly.
"""

def create_agent():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    tools = [
        calculator_tool,
        datetime_tool,
        weather_tool
    ]

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_openai_functions_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return agent_executor