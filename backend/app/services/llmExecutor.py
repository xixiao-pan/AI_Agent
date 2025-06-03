import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)

class LLMExecutor:

    def __init__(self, model_name="gpt-3.5-turbo"):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("Missing OPENAI_API_KEY in environment variables")
        self.model = model_name

    def execute(self, prompt: str) -> str:
        response = client.chat.completions.create(model=self.model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=512)
        return response.choices[0].message.content