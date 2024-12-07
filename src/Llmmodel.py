import openai

from dotenv import load_dotenv

import Env
Env.envset()

import aisuite as ai
client = ai.Client()

#models = ["openai:gpt-4o"]
models = [ "huggingface:HuggingFaceTB/SmolLM2-1.7B-Instruct", "groq:gemma-7b-it"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
        )
    print(response.choices[0].message.content)
