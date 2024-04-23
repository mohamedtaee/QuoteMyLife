import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def prompt_fine_tune_model(model, messages):
    client = OpenAI()

    completion = client.chat.completions.create(model=model, messages=messages)

    return completion.choices[0].message


if __name__ == "__main__":
    model = "ft:gpt-3.5-turbo-1106:personal::92VNg4lL"

    messages = [
        {
            "role": "system",
            "content": "You are a famous quote API that returns famous quotes in JSON based on user input.",
        },
        {"role": "user", "content": "Give me a quote about having a good day"},
    ]

    response = prompt_fine_tune_model(model, messages)

    content = response.content

    if content:
        json_content = json.loads(content)
        print("Quote:", json_content.get("quote", "No quote found"))
        print("Source:", json_content.get("source", "No source found"))

    else:
        print("No content found in response")
