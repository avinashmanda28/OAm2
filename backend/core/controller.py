from backend.modules.prompt.prompt_interpreter import PromptInterpreter


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()

    def process_prompt(self, prompt: str):

        prompt_data = self.prompt_interpreter.interpret(prompt)

        workflow = {
            "prompt_analysis": prompt_data,
            "pipeline": [
                "video_planner",
                "script_generator",
                "scene_splitter",
                "media_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
