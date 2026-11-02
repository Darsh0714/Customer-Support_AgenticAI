# Local Customer Support AI-Agent

An autonomous customer support and operational routing agent built using LangChain and local Large Language Models (LLMs) via Ollama. The system acts as a decision-making engine that analyzes natural language input, determines the user's intent, and executes corresponding programmatic tools (Python functions) to complete tasks without third-party API costs or data privacy exposure.

## Features

* **Autonomous Tool Selection:** Uses a local Llama3 instance to parse text and map user intentions directly to specific back-end scripts.
* **Deterministic Execution:** Eliminates conversational overhead by forcing structured output keys, ensuring reliable code execution.
* **Functional Extensibility:** Designed with modular, decoupled tools that mimic real database checks and financial calculations.
* **Data-Secure Environment:** Runs entirely on local hardware using Ollama, guaranteeing that sensitive business queries do not leave the host infrastructure.
* **Streamlit Interface:** Provides a clean interface displaying the step-by-step reasoning logs and execution outputs.

## Tech Stack

* **Framework:** LangChain
* **LLM Engine:** Ollama (Llama3 Model)
* **Frontend:** Streamlit
* **Language:** Python

## System Architecture

```text
[User Input: Natural Language]
            │
            ▼
[Prompt Template Formatting]
            │
            ▼
[Local LLM Inference via Ollama]
            │
            ▼
[Decision Parsing: Structural Key Output]
            │
            ├───> CHECK_BALANCE ───> [Python Tool A: Database Simulation]
            ├───> CALCULATE_REFUND ─> [Python Tool B: Math Computation Engine]
            └───> GENERAL_REPLY ───> [Text Fallback Mode]
```


## How It Works

1. **Intent Analysis:** The user enters a request (e.g., "Check the balance for account darshini").
2. **Classification & Mapping:** The prompt constraints guide the local model to skip conversational filler and output a structured instruction key like `CHECK_BALANCE: darshini`.
3. **Programmatic Execution:** Python conditional handlers catch the key, isolate the required parameter token, and run the designated script function.
4. **Output Rendering:** The web application displays both the underlying structural decision string and the final executed functional output.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd local-ai-task-agent
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install streamlit langchain langchain-ollama
```

### 4. Serve the Local Model
Ensure Ollama is installed on your machine and host services are active:
```bash
ollama pull llama3
ollama serve
```

### 5. Run the Application
```bash
streamlit run app.py
```

## Future Roadmap

* **Dynamic Tool Binding:** Upgrading to LangChain Structured Tool architectures to manage arguments automatically.
* **Database Integration:** Replacing mock dictionaries with direct SQLAlchemy relational database connections.
* **Memory Management:** Incorporating conversation history tracking to manage multi-turn tool calling.

## Author

* **Darshini R** - Data Scientist & AI Engineer
