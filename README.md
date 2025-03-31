# LLM Code Interpreter

A powerful code interpreter system that combines multiple LangChain agents to handle both Python code execution and CSV data analysis. This project demonstrates the integration of different AI agents working together to provide comprehensive data analysis and code execution capabilities.

## Features

- **Python Code Execution Agent**: Executes Python code based on natural language instructions
- **CSV Data Analysis Agent**: Analyzes and queries CSV data using pandas
- **Grand Agent**: Orchestrates the interaction between different specialized agents
- **QR Code Generation**: Built-in capability to generate QR codes
- **Episode Data Analysis**: Specialized analysis of episode information from CSV files

## Project Structure

```
code-interpreter/
├── agents/
│   ├── python_execute_agent.py  # Handles Python code execution
│   ├── csv_agent.py            # Manages CSV data analysis
│   └── grand_agent.py          # Orchestrates agent interactions
├── static/
│   └── episode_info.csv        # Sample data for analysis
├── main.py                     # Main application entry point
└── README.md                   # This file
```

## Prerequisites

- Python 3.x
- OpenAI API key
- Required Python packages (see requirements.txt)

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env copy` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=
   LANGCHAIN_API_KEY=
   LANGCHAIN_TRACING_V2=
   LANGCHAIN_PROJECT=
   PINECONE_API_KEY=
   PINECONE_INDEX_NAME=
   ```

## Usage

Run the main script:

```bash
python main.py
```

The system can handle various types of queries:

1. CSV Data Analysis:

   ```python
   "which season has the most episodes?"
   ```

2. Code Generation and Execution:
   ```python
   "Generate and save in current working directory 1 qrcode that point to `https://github.com/KoKocik1`"
   ```

## Security Notice

This project uses agents that can execute arbitrary Python code. For security reasons:

- Code execution is opt-in and requires explicit permission
- The system should be run in a controlled environment
- Users should be aware of the security implications of executing arbitrary code

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
