from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()

    def process_prompt(self, prompt: str):

        prompt_data = self.prompt_interpreter.interpret(prompt)

        video_plan = self.video_planner.create_plan(prompt_data)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "pipeline": [
                "script_generator",
                "scene_splitter",
                "media_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
