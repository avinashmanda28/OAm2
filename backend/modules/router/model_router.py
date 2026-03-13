class ModelRouter:

    def __init__(self):

        self.models = {
            "script": ["llama3", "mistral", "fallback_llm"],
            "planning": ["mistral", "llama3", "fallback_llm"],
            "image": ["stable_diffusion", "sd_light", "fallback_image"],
            "voice": ["xtts", "coqui", "fallback_voice"]
        }

    def choose_model(self, task):

        if task not in self.models:
            return None

        return self.models[task][0]

    def get_fallback(self, task, attempt):

        try:
            return self.models[task][attempt]
        except:
            return None

    def route_task(self, task):

        model = self.choose_model(task)

        return {
            "task": task,
            "selected_model": model
        }

    def get_pipeline(self):

        return {
            "script": self.models["script"],
            "planning": self.models["planning"],
            "image": self.models["image"],
            "voice": self.models["voice"]
        }
