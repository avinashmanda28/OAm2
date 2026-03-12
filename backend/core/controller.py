from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter
from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator
from backend.modules.voice.voice_generator import VoiceGenerator


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()
        self.voice_generator = VoiceGenerator()

    def process_prompt(self, prompt: str):

        # Prompt interpretation
        prompt_data = self.prompt_interpreter.interpret(prompt)

        # Video structure
        video_plan = self.video_planner.create_plan(prompt_data)

        # Script generation
        script = self.script_generator.generate_script(video_plan)

        # Scene creation
        scenes = self.scene_splitter.split_scenes(script)

        # Visual prompts
        visuals = self.visual_generator.generate_visuals(scenes)

        # Voice generation
        voice_tracks = self.voice_generator.generate_voice(scenes)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "scenes": scenes,
            "visual_prompts": visuals,
            "voice_tracks": voice_tracks,
            "pipeline": [
                "image_generation",
                "editing_engine",
                "render_engine"
            ]
        }

        return workflow
