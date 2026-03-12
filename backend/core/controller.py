from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.scene.scene_splitter import SceneSplitter
from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator
from backend.modules.voice.voice_generator import VoiceGenerator
from backend.modules.image.image_generator import ImageGenerator
from backend.modules.caption.caption_generator import CaptionGenerator
from backend.modules.smart_edit.smart_editor import SmartEditor
from backend.modules.broll.broll_engine import BRollEngine
from backend.modules.silence.silence_remover import SilenceRemover
from backend.modules.hook.hook_detector import HookDetector
from backend.modules.healing.self_healing import SelfHealingSystem
from backend.modules.knowledge.knowledge_engine import KnowledgeEngine
from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer


class Controller:

    def __init__(self):

        self.healing = SelfHealingSystem()

        self.prompt_interpreter = PromptInterpreter()
        self.knowledge_engine = KnowledgeEngine()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()
        self.voice_generator = VoiceGenerator()
        self.image_generator = ImageGenerator()
        self.caption_generator = CaptionGenerator()
        self.smart_editor = SmartEditor()
        self.broll_engine = BRollEngine()
        self.silence_remover = SilenceRemover()
        self.hook_detector = HookDetector()
        self.scene_composer = SceneComposer()
        self.video_editor = VideoEditor()
        self.video_renderer = VideoRenderer()

    def process_prompt(self, prompt: str):

        try:

            prompt_data = self.prompt_interpreter.interpret(prompt)
            self.healing.monitor_module("prompt_interpreter", "ok")

            knowledge = self.knowledge_engine.collect_knowledge(prompt_data)
            self.healing.monitor_module("knowledge_engine", "ok")

            video_plan = self.video_planner.create_plan(prompt_data)

            script = self.script_generator.generate_script(video_plan)

            hook = self.hook_detector.detect_hook(script)

            captions = self.caption_generator.generate_captions(script)

            scenes = self.scene_splitter.split_scenes(script)

            editing = self.smart_editor.analyze_editing(script, scenes)

            broll = self.broll_engine.generate_broll(scenes)

            visuals = self.visual_generator.generate_visuals(scenes)

            voice_tracks = self.voice_generator.generate_voice(scenes)

            optimized_audio = self.silence_remover.remove_silence(voice_tracks)

            images = self.image_generator.generate_images(visuals)

            composed_scenes = self.scene_composer.compose_scenes(images, voice_tracks)

            timeline = self.video_editor.assemble_video(composed_scenes)

            rendered_video = self.video_renderer.render_video(timeline)

            health = self.healing.check_system_health()

            workflow = {
                "prompt_analysis": prompt_data,
                "knowledge": knowledge,
                "video_plan": video_plan,
                "hook": hook,
                "script": script,
                "captions": captions,
                "scenes": scenes,
                "editing_plan": editing,
                "broll": broll,
                "visual_prompts": visuals,
                "voice_tracks": voice_tracks,
                "optimized_audio": optimized_audio,
                "images": images,
                "scene_videos": composed_scenes,
                "timeline": timeline,
                "rendered_video": rendered_video,
                "system_health": health
            }

            return workflow

        except Exception as e:

            return {
                "error": str(e),
                "system_health": self.healing.check_system_health()
        }
