from langchain.tools import Tool
from datetime import datetime


def calculator(expression: str) -> str:
    """
    Used to resolve mathematical expressions.
    Input example: '128 * 46'
    """
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception:
        return "Erro ao calcular a expressão"


calculator_tool = Tool(
    name= "Calculator",
    func= calculator,
    description= (
        "Use this tool to solve mathematical expressions. The input must be a valid expression, e.g., '128 * 46'."
    ),
)


def current_datetime(date: str = "") -> str:
    """
    Returns the current date and time.
    """

    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


datetime_tool = Tool(
    name="CurrentDateTime",
    func=current_datetime,
    description=(
        "Use this tool for any question related to the current date or time,including today, yesterday, tomorrow, or the current day of the week."
    ),
)





