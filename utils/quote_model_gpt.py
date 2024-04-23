import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_FINE_TUNE_MODEL = os.getenv("OPENAI_FINE_TUNE_MODEL")


def prompt_fine_tune_model(messages, model=OPENAI_FINE_TUNE_MODEL):
    client = OpenAI()

    if not model:
        raise ValueError("Model is required")

    completion = client.chat.completions.create(model=model, messages=messages)

    print(completion)

    return completion.choices[0].message


def submit_user_prompt(prompt):
    messages = [
        {
            "role": "system",
            "content": "You are a famous quote API that returns famous quotes in JSON based on user input.",
        },
        {"role": "user", "content": str(prompt)},
    ]

    response = prompt_fine_tune_model(model=OPENAI_FINE_TUNE_MODEL, messages=messages)

    content = response.content

    if content:
        json_content = json.loads(content)
        print("Quote:", json_content.get("quote", "No quote found"))
        print("Source:", json_content.get("source", "No source found"))

        string_response = f"{json_content.get('quote', 'No quote found')} - {json_content.get('source', 'No source found')}"

        return string_response

    else:
        print("No content found in response")
        return "No content found in response"
