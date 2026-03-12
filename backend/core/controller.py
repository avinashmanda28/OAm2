from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter
from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator
from backend.modules.voice.voice_generator import VoiceGenerator
from backend.modules.image.image_generator import ImageGenerator
from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer


class Controller:

    def __init__(self):

        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()
        self.voice_generator = VoiceGenerator()
        self.image_generator = ImageGenerator()
        self.scene_composer = SceneComposer()
        self.video_editor = VideoEditor()
        self.video_renderer = VideoRenderer()

    def process_prompt(self, prompt: str):

        prompt_data = self.prompt_interpreter.interpret(prompt)

        video_plan = self.video_planner.create_plan(prompt_data)

        script = self.script_generator.generate_script(video_plan)

        scenes = self.scene_splitter.split_scenes(script)

        visuals = self.visual_generator.generate_visuals(scenes)

        voice_tracks = self.voice_generator.generate_voice(scenes)

        images = self.image_generator.generate_images(visuals)

        composed_scenes = self.scene_composer.compose_scenes(images, voice_tracks)

        final_video = self.video_editor.assemble_video(composed_scenes)

        rendered_video = self.video_renderer.render_video(final_video)

        workflow = {
            "prompt_analysis": prompt_data,
            "video_plan": video_plan,
            "script": script,
            "scenes": scenes,
            "visual_prompts": visuals,
            "voice_tracks": voice_tracks,
            "images": images,
            "scene_videos": composed_scenes,
            "timeline": final_video,
            "rendered_video": rendered_video
        }

        return workflow
