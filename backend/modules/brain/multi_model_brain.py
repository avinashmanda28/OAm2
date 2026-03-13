class MultiModelBrain:

    def __init__(self):

        self.models = {
            "script": "llama",
            "research": "mistral",
            "ideas": "deepseek",
            "seo": "mistral",
            "visual": "llama"
        }

    def select_model(self, task):

        if task in self.models:
            return self.models[task]

        return "llama"

    def update_model(self, task, model):

        self.models[task] = model

    def get_model_map(self):

        return self.models
