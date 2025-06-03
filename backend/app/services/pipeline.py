from backend.app.services.intentDetector import IntentDetector
from backend.app.services.featureExtractor import LogoFeatureExtractor
from backend.app.services.taskPlanner import TaskPlanner
from backend.app.services.llmExecutor import LLMExecutor

class AgentPipeline:
    def __init__(self):
        self.intent_detector = IntentDetector()
        self.logo_extractor = LogoFeatureExtractor()
        self.task_planner = TaskPlanner()
        self.llm = LLMExecutor(api_key="test_api_key")

    def handle_input(self, user_input, user_db):
        intent = self.intent_detector.detect(user_input)

        if intent == "generate_logo":
            features = self.logo_extractor.extract(user_input)
            memory = ...  # 读取历史 logo
            prompt = self.task_planner.plan(user_input, memory, ..., ...)
            result = self.llm.execute(prompt)
            ...