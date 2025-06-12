# app/helpers/openai_helper.py

import openai
import os

# Set your API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(prompt, model="gpt-4"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You're a data assistant helping analyse churn data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=800
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error from OpenAI: {e}"