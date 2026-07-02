import os

from dotenv import load_dotenv
from openai import OpenAI

API_KEY_ENV = "OPENROUTER_API_KEY"
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/free"


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
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
