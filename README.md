# 🤖 Python AI Search Agent

A Python-based AI research agent built using LangChain and OpenRouter.

This project demonstrates how to build an AI agent that can research topics, use external tools, retrieve information, generate structured responses, and save research results.

## 🚀 Features

- 🔍 Web search using DuckDuckGo
- 📚 Information retrieval using Wikipedia
- 🤖 LLM integration through OpenRouter
- 🛠️ Tool-based AI research workflows
- 💾 Save research results to a text file
- 📋 Structured output using Pydantic
- 🔐 Environment variable configuration for API credentials
- 📦 Pinned dependency versions for reproducible installations

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain OpenRouter
- LangChain OpenAI
- LangChain Anthropic
- OpenRouter API
- DuckDuckGo Search
- Wikipedia
- Pydantic
- Python Dotenv

## 📋 Prerequisites

Before getting started, make sure you have:

- Python 3.12 or another compatible Python version
- pip
- Git
- An OpenRouter API key

### Verify Python and Git

Check your Python version:

```bash
python3 --version
```

Check your Git installation:

```bash
git --version
```

## 📥 Installation and Setup

Follow these steps to clone the repository and run the project on a new computer.

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/AMITJHA001/ai_search_agent.git
```

### Step 2: Navigate to the Project Directory

```bash
cd ai_search_agent
```

### Step 3: Create a Python Virtual Environment

A virtual environment keeps this project's dependencies separate from other Python projects.

On Linux or macOS:

```bash
python3 -m venv venv
```

If you are using Ubuntu and encounter an error related to the `venv` module, install it:

```bash
sudo apt update
sudo apt install python3-venv
```

Then create the environment again:

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

**Linux or macOS:**

```bash
source venv/bin/activate
```

**Windows Command Prompt:**

```bat
venv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, your terminal should display `(venv)`.

### Step 5: Upgrade pip

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
```

### Step 6: Install Dependencies

Install the pinned package versions from the lock file:

```bash
python -m pip install -r requirements-lock.txt
```

The lock file records the package versions used in the development environment to help reproduce the setup.

**Important:** The `requirements-lock.txt` file must be committed to GitHub for this command to work after cloning the repository.

If the repository contains only `requirements.txt`, use:

```bash
python -m pip install -r requirements.txt
```

### Step 7: Verify Dependencies

Check whether the installed packages have dependency conflicts:

```bash
python -m pip check
```

Expected output when no dependency conflicts are detected:

```text
No broken requirements found.
```

## 🔑 Environment Configuration

The application uses OpenRouter to access supported language models.

You must configure your API key before running the application.

### Step 1: Create an OpenRouter API Key

Visit:

https://openrouter.ai/

Create an account and generate an API key.

### Step 2: Create a `.env` File

From the project root directory, run:

```bash
touch .env
```

Open the `.env` file and add the following environment variables:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL_NAME=deepseek/deepseek-v4.1-flash
```

Replace `your_openrouter_api_key` with your actual OpenRouter API key.

The model name above is an example. Use a model available through your OpenRouter account and ensure that its name matches the configuration expected by your application.

### Environment Variables

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | API key used to authenticate with OpenRouter |
| `OPENROUTER_MODEL_NAME` | Name of the language model used by the application |

**Security recommendations:**

- Never commit your actual `.env` file to GitHub.
- Never expose your API key in source code or public repositories.
- Ensure `.env` is included in `.gitignore`.
- Share a placeholder configuration file such as `sample.env` instead of your real credentials.

### Example `.gitignore`

Make sure your `.gitignore` includes:

```gitignore
# Python cache
__pycache__/
*.py[cod]

# Virtual environments
venv/
.venv/
test_venv/

# Environment variables and secrets
.env
.env.*

# Keep example environment files
!.env.example
!sample.env

# IDE settings
.vscode/
.idea/

# Logs
*.log
```

## ▶️ Running the Application

Once you have installed the dependencies and configured your environment variables, run:

```bash
python main.py
```

The application should start in your terminal and prompt you to enter a research question.

### Example

```text
What can I help you research?

What are the planets in our solar system?
```

The agent processes your question using its configured language model and available tools.

The exact output depends on the research question, selected model, and tools implemented in the application.

## 🔄 Running the Project Again

After the initial setup, you do not need to create the virtual environment or reinstall dependencies every time.

Whenever you want to run the project again, navigate to the project directory:

```bash
cd ai_search_agent
```

Activate the existing virtual environment:

```bash
source venv/bin/activate
```

Run the application:

```bash
python main.py
```

When you finish working, deactivate the virtual environment:

```bash
deactivate
```

**Note:** The activation command shown above is for Linux and macOS. Use the appropriate activation command for Windows.

## 📁 Project Structure

```text
ai_search_agent/
│
├── main.py                 # Main application entry point
├── tools.py                # Research tools
├── test_save_tool.py       # Tests for the save tool
├── requirements.txt        # Main dependency list
├── requirements-lock.txt   # Pinned environment dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
└── research_output.txt     # Research output, if generated
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main application entry point |
| `tools.py` | Contains the research tools used by the agent |
| `test_save_tool.py` | Tests the save tool |
| `requirements.txt` | Main Python dependency list |
| `requirements-lock.txt` | Pinned package versions for reproducible installations |
| `.env` | Local environment variables and API credentials |
| `.gitignore` | Specifies files Git should ignore |
| `README.md` | Project documentation |
| `research_output.txt` | Stores research results when generated by the application |

The `.env` file must be created locally. It should not be committed to GitHub.

## 🔧 Available Tools

### 1. DuckDuckGo Search

Searches the web for information relevant to the research question.

### 2. Wikipedia Search

Retrieves relevant information from Wikipedia.

### 3. Save Research Results

Saves research results to a text file for future reference.

The output file is generated or updated when the save tool is used.

## 🧪 Running Tests

To run the save tool tests, execute:

```bash
python test_save_tool.py
```

Ensure that your virtual environment is activated and the required dependencies are installed.

## 📦 Dependency Management

This project uses pinned dependency versions to reduce unexpected changes caused by package updates.

### Install Dependencies

```bash
python -m pip install -r requirements-lock.txt
```

### Check Dependency Compatibility

```bash
python -m pip check
```

### Generate the Lock File

If you need to capture the installed package versions from your working environment, run:

```bash
python -m pip freeze > requirements-lock.txt
```

Run this command with the project's virtual environment activated.

**Warning:** This command replaces the existing lock file with all packages installed in the active environment.

Pinned package versions improve reproducibility, but they do not guarantee compatibility across every Python version, operating system, or future external API change.

## 🐛 Troubleshooting

### 1. ModuleNotFoundError

If Python reports that a module is missing, activate your virtual environment and install the dependencies:

```bash
source venv/bin/activate
python -m pip install -r requirements-lock.txt
```

### 2. Missing Environment Variables

If the application cannot find your API key or model name, check that:

- The `.env` file exists in the project root.
- The environment variable names match those used in your Python code.
- The application loads environment variables using `python-dotenv`.
- The `.env` file is loaded before the variables are accessed.

Example:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("OPENROUTER_MODEL_NAME")
```

### 3. OpenRouter API Errors

Check the following:

- Your API key is valid.
- Your OpenRouter account has sufficient credits.
- The selected model is available through OpenRouter.
- Your application loads the environment variables correctly.
- The model name matches the variable expected by your code.

### 4. Dependency Conflicts

Run:

```bash
python -m pip check
```

If conflicts are reported, verify that:

- You activated the correct virtual environment.
- You installed dependencies from the intended requirements file.
- Your Python version is compatible with the pinned packages.

### 5. Virtual Environment Activation Fails

On Linux or macOS:

```bash
source venv/bin/activate
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 6. Python Command Not Found

On Ubuntu or other Linux distributions, try:

```bash
python3 main.py
```

## 🔮 Future Improvements

Potential improvements for this project include:

- Adding more research tools.
- Implementing multi-step agent workflows.
- Improving structured output validation.
- Adding retries and error handling.
- Implementing conversation memory.
- Building a web interface.
- Integrating additional LLM providers.
- Exploring advanced agentic AI architectures.

## 👨‍💻 Author

**Amit Jha**

GitHub: [AMITJHA001](https://github.com/AMITJHA001)

## 📂 Repository

[Python AI Search Agent](https://github.com/AMITJHA001/ai_search_agent)

## 📄 License

This project is intended for learning and experimentation.

Add an appropriate open-source license if you plan to distribute the project for reuse.