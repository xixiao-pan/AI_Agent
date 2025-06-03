class IntentDetector:
    def __init__(self, model=None):
        self.llm = model or self.default_model()

    def default_model(self):
        # return spaCy model, regex, or LLM API
        pass

    def detect(self, user_input: str) -> str:
        """
        Returns one of: 'generate_logo', 'faq_question', 'chat'
        """
        # do prediction/classification here
        # Notes: Simply used LLM here. Consider using a smaller and quicker model for classification.
        prompt = f"""Please classify the user's intent into one of the following three categories (respond with one of the keywords below only):
                - generate_logo: if the user wants to generate a logo
                - faq_question: if the user is asking a frequently asked question about the platform or product
                - chat: if it's a casual conversation or does not belong to the above two categories

                The user's input is: "{user_input}"
                Please respond with the intent keyword only:"""
        result = self.llm.execute(prompt).strip().lower()
        return result