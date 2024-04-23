import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from utils.mongo_db import MongoDB

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_FINE_TUNE_MODEL = os.getenv("OPENAI_FINE_TUNE_MODEL")


def prompt_fine_tune_model(messages, model=OPENAI_FINE_TUNE_MODEL):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        if not model:
            raise ValueError("Model is required")

        completion = client.chat.completions.create(model=model, messages=messages)

        mongo = MongoDB()
        mongo.store_openai_response(completion.model_dump())

        return completion.choices[0].message

    except Exception as e:
        return e


def submit_user_prompt(prompt):
    messages = [
        {
            "role": "system",
            "content": "You are a famous quote API that returns famous quotes in JSON based on user input.",
        },
        {"role": "user", "content": str(prompt)},
    ]

    response = prompt_fine_tune_model(model=OPENAI_FINE_TUNE_MODEL, messages=messages)

    if isinstance(response, Exception):
        print("Error or No content found in response:", response)
        return "No content found in response"

    try:
        content = response.content
        if content:
            json_content = json.loads(content)
            quote = json_content.get("quote", "No quote found")
            source = json_content.get("source", "No source found")

            string_response = f"{quote} - {source}"
            return string_response
        else:
            return f"No quote found: {response}"

    except json.JSONDecodeError:
        print("Failed to decode JSON from response")
        return "Failed to decode JSON from response"
