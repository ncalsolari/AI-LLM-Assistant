from dotenv import load_dotenv
from agent import create_agent

load_dotenv()

def main():
    agent = create_agent()

    print("Assistant started (type 'exit' to close)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Goodbye!")
            break

        print("Agent: ", end="", flush=True)
        response = agent.invoke({"input": user_input})
        print(response["output"])
        print()

if __name__ == "__main__":
    main()
