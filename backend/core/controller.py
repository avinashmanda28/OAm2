class Controller:

    def __init__(self):
        self.name = "OAm² Controller"

    def process_prompt(self, prompt: str):

        workflow = {
            "prompt": prompt,
            "steps": [
                "prompt_interpreter",
                "video_planner",
                "script_generator",
                "scene_splitter",
                "visual_generator",
                "voice_generator",
                "scene_composer",
                "video_composer",
                "renderer"
            ]
        }

        return workflow
