SYSTEM_MESSAGE = """
You are a SQL expert.
Only generate SQL query.
Do not explain.
Do not add extra text.
"""

def build_prompt(question, schema):

    prompt = f"""
Database Schema:
{schema}

User Question:
{question}

Generate only SQL query.
"""

    return prompt
