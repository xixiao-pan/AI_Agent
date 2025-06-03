import os
import pytest
from app.services.llmExecutor import LLMExecutor

@pytest.mark.skipif(os.getenv("OPENAI_API_KEY") is None, reason="OPENAI_API_KEY not set")
def test_llm_executor_with_image():
    llm = LLMExecutor(model_name="gpt-4o")

    prompt = (
        "Describe this logo in detail: its main color and shape, any text it contains, "
        "its style (e.g., modern, minimalist), and any unique visual elements."
    )

    image_path = "static/test03.png"  # 确保这个路径的图片存在
    result = llm.execute(prompt, image_path=image_path)

    print("\nLLM Response:\n", result)

    # 这里只断言非空，具体断言可以根据返回内容加
    assert result and isinstance(result, str)