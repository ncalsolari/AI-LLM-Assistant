# AI Assistant with Tools

## Description

This project implements an AI assistant using an **OpenAI GPT-3.5 model**, integrated with **external tools** via LangChain Agents.  
The agent dynamically decides **when to respond on its own** and **when to trigger a tool**.

The currently available tools are:

1. **Calculator** – solves mathematical expressions.  
2. **CurrentDateTime** – returns the current date and/or time.  
3. **Weather** – queries an external API (Open-Meteo) to return the weather forecast for any city.

---

## Solution Architecture

- **LLM:** OpenAI GPT-3.5 Turbo  
- **Framework:** LangChain (Agents + Tools)  
- **Tools:** Calculator, DateTime, Weather  
- **Interface:** Command Line Interface (CLI)  
- **Agent Type:** `OPENAI_FUNCTIONS`  

---

## Project Structure

The `src` folder contains files organized into three packages: `app`, `agent`, and `tools`:

- `app`: handles the application's input/output logic.  
- `agent`: creates and configures the agent.  
- `tools`: creates and configures the tools that the agent will use.

---

## Setup and Execution

### 1. Configure the `.env`

After cloning the repository, create a `.env` file in the project's root folder with:



```
# OPEAI API Key
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

### 2. Virtual Environment

Create a virtual environment using Python 3.9:

```bash
python3.9 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Execute the `app.py` file:

```bash
python app.py
```
 
Examples of inputs that will use the tools:
```
> What is 128 times 46?
> What day is it today?
> What is the weather forecast in São Paulo?
```

Examples of inputs that will not use the tools:
```
> Who was Albert Einstein?
> What is the speed of light?
> Can dogs eat grapes?
```

---


### Implementation Logic

The program's logic works as illustrated in the diagram below:

![alt text](link "Logical Diagram")

Based on the user's input, the program analyzes whether to use a tool or not. For each tool, the cases in which it should be used were described and exemplified.


### Learnings and Next Steps

During this challenge, the main learning was about integrating LLMs with tools and agents using the LangChain framework, understanding the differences between direct LLM responses and responses with external tools.

It is impressive the potential that this approach has. Equipping LLMs with efficient and established tools (such as weather APIs, pricing APIs, email APIs, etc.) transforms them from simple prediction models into systems capable of decision making and action, opening the way for building robust and automated applications.

It was also important to understand the limitations and challenges of this application. More complex inputs (such as equations involving square roots, logarithms, and exponentiation) or indirect requests (e.g., "what is the log of 6 base 10") may not be interpreted correctly, causing the tool to not be triggered.

With more time, it would be possible to improve these fine-tuning aspects, for example:

-Enhance mathematical expression recognition using more robust regex patterns.

-Restrict functions from the math library more safely.

-Implement new tools (e.g., email sending).

-Add additional features to existing tools (e.g., set alarms based on the current time).

The potential for modifying and expanding AI assistants is enormous, and their application areas are virtually unlimited.