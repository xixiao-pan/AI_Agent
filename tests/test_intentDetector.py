import pytest
from app.services.intentDetector import IntentDetector
from app.services.llmExecutor import LLMExecutor

@pytest.fixture
def intent_detector():
    llm = LLMExecutor()
    return IntentDetector(llm)

@pytest.mark.parametrize("text,expected", [
    ("I want to generate a logo for my new business.", "generate_logo"),
    ("What is the price of this service?", "faq_question"),
    ("Hello, how are you?", "chat"),
])
def test_intent_classification(intent_detector, text, expected):
    result = intent_detector.detect(text).strip().lower()
    assert result == expected