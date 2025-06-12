# chat_with_data.py

import openai
import traceback
import pandas as pd

from openai_helper import call_gpt

def interpret_query(user_query, df):
    """Main interface to process natural language query on churn data."""
    try:
        # Provide system context for GPT
        prompt = f"""
You are a data assistant. A user has asked a question about a DataFrame called 'df' that contains churn analysis data.
You must generate Python code that uses pandas and matplotlib/seaborn to answer the query.
The code should assume 'df' is already loaded. Do not include import statements or df loading.

Here is the question:
\"\"\"{user_query}\"\"\"

Return only the Python code that answers the query.
        """

        # Call GPT (wrapped safely)
        code = call_gpt(prompt)

        # Execute code safely in local scope
        local_vars = {'df': df.copy()}
        exec(code, {}, local_vars)

        # Return the last object (plot or data)
        output = local_vars.get('output', None)
        return output, code

    except Exception as e:
        return f"Error: {str(e)}\n{traceback.format_exc()}", None