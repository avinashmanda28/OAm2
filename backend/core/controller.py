from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter
from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()

    def process_prompt(self, prompt: str):

        # Step 1
        prompt_data = self.prompt_interpreter.interpret(prompt)

        # Step 2
        video_plan = self.video_planner.create_plan(prompt_data)

        # Step 3
        script = self.script_generator.generate_script(video_plan)

        # Step 4
        scenes = self.scene_splitter.split_scenes(script)

        # Step 5
        visuals = self.visual_generator.generate_visuals(scenes)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "scenes": scenes,
            "visual_prompts": visuals,
            "pipeline": [
                "image_generation",
                "voice_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
