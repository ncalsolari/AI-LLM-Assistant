from dotenv import load_dotenv
from agent import create_agent
import asyncio
import os

load_dotenv()

async def main():
    

    agent = create_agent()
    os.system('cls' if os.name == 'nt' else 'clear') #clean the CLI
    print("Assistant started (type 'exit' to close)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Goodbye!")
            break

        print("Agent: ", end="", flush=True)
        response = await agent.ainvoke({"input": user_input})
        print(response["output"])
        print()

if __name__ == "__main__":
    asyncio.run(main())
