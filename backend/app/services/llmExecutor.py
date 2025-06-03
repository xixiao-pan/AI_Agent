import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional, Union

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class LLMExecutor:
    def __init__(self, model_name="gpt-4o"):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("Missing OPENAI_API_KEY in environment variables")
        self.model = model_name

    def _encode_image_to_base64(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def execute(self, prompt: str, image_path: Optional[str] = None) -> str:
        messages = [{"role": "user", "content": []}]
        
        # Add text prompt
        messages[0]["content"].append({
            "type": "text",
            "text": prompt
        })

        # Optionally add image
        if image_path:
            image_base64 = self._encode_image_to_base64(image_path)
            messages[0]["content"].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_base64}"
                }
            })

        # Send request
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )
        return response.choices[0].message.content