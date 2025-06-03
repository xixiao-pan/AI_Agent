class TaskPlanner:
    def __init__(self):
        pass

    def plan(self, query: str, memory: dict, history: list, preferences: dict) -> str:
        # Compose prompt or task type
        return f"请为以下需求生成一个 logo：{query}。用户偏好是：{preferences}"