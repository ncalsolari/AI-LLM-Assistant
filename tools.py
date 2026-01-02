from langchain.tools import Tool


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
    name="Calculator",
    func=calculator,
    description=(
        "Use this tool to solve mathematical expressions. The input must be a valid expression, e.g., '128 * 46'."
    ),
)
