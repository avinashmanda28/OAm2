from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()

    def process_prompt(self, prompt: str):

        # Step 1: interpret prompt
        prompt_data = self.prompt_interpreter.interpret(prompt)

        # Step 2: create video plan
        video_plan = self.video_planner.create_plan(prompt_data)

        # Step 3: generate script
        script = self.script_generator.generate_script(video_plan)

        # Step 4: create scenes
        scenes = self.scene_splitter.split_scenes(script)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "scenes": scenes,
            "pipeline": [
                "media_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
