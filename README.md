

# SQL Music Store Agent

An AI-powered SQL Agent that converts natural language questions into SQL queries, validates them, executes them on a SQLite database, and returns results.

---

## Overview

This project demonstrates a modular SQL Agent that:

* Converts natural language questions to SQL
* Validates queries to prevent unsafe operations
* Executes queries on SQLite
* Formats results neatly

LLM-ready design—works with OpenAI, Gemini, or other providers.

---

## Project Structure

```
music_agent/
│
├── main.py
├── agent.py
├── database.py
├── prompts.py
│
└── tools/
    ├── schema_tool.py
    ├── sql_tool.py
    ├── validation_tool.py
    └── formatter_tool.py
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sivavashini/SQL-Music-Store-Agent.git
cd SQL-Music-Store-Agent
```

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## API Key Setup (LLM Integration)

Add your API key as an environment variable.

**Windows (PowerShell):**

```powershell
setx API_KEY "your_api_key_here"
```

**Mac/Linux:**

```bash
export API_KEY="your_api_key_here"
```

In your code:

```python
import os
api_key = os.getenv("API_KEY")
```

Do not commit your API key. Keep `.env` in `.gitignore`.

---

## Running the Project

```bash
python main.py
```

Example:

```
Ask your question: Show all artists
```

---

## Safety Features

* Blocks destructive SQL commands (`DROP`, `DELETE`, `UPDATE`)
* Modular validation layer
* Clear separation of generation, execution, and formatting

---

## Example

**Input:**

```
Show all albums
```

**Output:**

```
(1, 'Album Name', 'Artist Name')
```

---

## Key Highlights

* Modular Agent Architecture
* LLM-Ready Design
* SQLite Backend
* Query Validation Layer
* Easy to Extend


## License

For educational and demonstration purposes.

---

## .gitignore Recommendations

```
.env
__pycache__/
*.pyc
```



If you want, I can **make an ultra-condensed “one-page resume-ready” version** that fits perfectly for GitHub submission or portfolio display. Do you want me to do that?
