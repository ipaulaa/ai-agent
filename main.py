import os

from dotenv import load_dotenv
from openai import OpenAI

API_KEY_ENV = "OPENROUTER_API_KEY"
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/free"


def print_response_details(prompt, response):
    print(f"User prompt: {prompt}")

    if response.usage is None:
        raise RuntimeError(
            "Missing token usage information. The API request may have failed."
        )
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

    print("Response:", response.choices[0].message.content, sep="\n")


def main():

    load_dotenv()
    api_key = os.environ.get(API_KEY_ENV)
    if api_key is None:
        raise RuntimeError(f"Missing required environment variable: {API_KEY_ENV}")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=api_key,
    )

    messages = [
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ]

    completion = client.chat.completions.create(model=MODEL, messages=messages)
    print_response_details(messages[0]["content"], completion)


if __name__ == "__main__":
    main()
