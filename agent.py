import os
from google import genai
from google.genai import types

from tools.schema_tool import get_schema
from tools.sql_tool import execute_query
from tools.validation_tool import validate_query
from tools.formatter_tool import format_result

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


class SQLAgent:

    def generate_sql(self, question):
        schema = get_schema()

        prompt = f"""
You are a SQL expert.
Only return SQL query.

Database Schema:
{schema}

User Question:
{question}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        sql_query = response.text.strip()
        
        # Remove markdown code blocks if present
        if sql_query.startswith("```"):
            lines = sql_query.split("\n")
            sql_query = "\n".join(lines[1:-1]) if len(lines) > 2 else sql_query
            sql_query = sql_query.strip()
        
        return sql_query

    def run(self, question):
        sql_query = self.generate_sql(question)

        if not validate_query(sql_query):
            return "Invalid query generated."

        rows = execute_query(sql_query)

        return format_result(rows)
