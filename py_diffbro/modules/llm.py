"""
This module contains the functions that interact with the OpenAI API.
"""

from dotenv import load_dotenv
import os
from typing import Any, Dict
import openai

# load .env file
load_dotenv()

# get openai api key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# ------------------ helpers ------------------


def safe_get(data, dot_chained_keys):
    """
    {'a': {'b': [{'c': 1}]}}
    safe_get(data, 'a.b.0.c') -> 1
    """
    keys = dot_chained_keys.split(".")
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data


def response_parser(response: Dict[str, Any]):
    return safe_get(response, "choices.0.message.content")


def make_client(gpt_api_key: str):
    return openai


# ------------------ content generators ------------------


def prompt(prompt: str, model: str = "gpt-4") -> str:
    openai_client = openai

    print(f"Firing off prompt")

    response = openai_client.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response_parser(response)
