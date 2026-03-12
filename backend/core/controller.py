from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()

    def process_prompt(self, prompt: str):

        # Step 1
        prompt_data = self.prompt_interpreter.interpret(prompt)

        # Step 2
        video_plan = self.video_planner.create_plan(prompt_data)

        # Step 3
        script = self.script_generator.generate_script(video_plan)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "pipeline": [
                "scene_splitter",
                "media_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
