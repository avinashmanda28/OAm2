from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter
from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator
from backend.modules.voice.voice_generator import VoiceGenerator
from backend.modules.image.image_generator import ImageGenerator


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()
        self.voice_generator = VoiceGenerator()
        self.image_generator = ImageGenerator()

    def process_prompt(self, prompt: str):

        # Prompt interpretation
        prompt_data = self.prompt_interpreter.interpret(prompt)

        # Video planning
        video_plan = self.video_planner.create_plan(prompt_data)

        # Script generation
        script = self.script_generator.generate_script(video_plan)

        # Scene splitting
        scenes = self.scene_splitter.split_scenes(script)

        # Visual prompts
        visuals = self.visual_generator.generate_visuals(scenes)

        # Voice tracks
        voice_tracks = self.voice_generator.generate_voice(scenes)

        # Image generation
        images = self.image_generator.generate_images(visuals)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "scenes": scenes,
            "visual_prompts": visuals,
            "voice_tracks": voice_tracks,
            "images": images,
            "pipeline": [
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
