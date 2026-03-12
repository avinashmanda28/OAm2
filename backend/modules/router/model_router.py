class ModelRouter:

    def __init__(self):

        self.models = {
            "prompt": "llama",
            "script": "mixtral",
            "knowledge": "mistral",
            "style": "gemma",
            "emotion": "llama"
        }

    def get_model(self, task):

        model = self.models.get(task)

        return {
            "task": task,
            "model_selected": model
        }

    def register_model(self, task, model_name):

        self.models[task] = model_name

        return {
            "registered": task,
            "model": model_name
        }

    def list_models(self):

        return {
            "models": self.models
      }
