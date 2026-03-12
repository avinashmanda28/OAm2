from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.story.story_engine import StoryEngine
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
from backend.modules.emotion.emotion_engine import EmotionEngine
from backend.modules.style.style_engine import StyleEngine
from backend.modules.motion.motion_engine import MotionEngine
from backend.modules.assets.asset_manager import AssetManager
from backend.modules.quality.quality_engine import QualityEngine
from backend.modules.improvement.improvement_engine import ImprovementEngine
from backend.modules.memory.memory_engine import MemoryEngine
from backend.modules.orchestrator.orchestrator_engine import OrchestratorEngine
from backend.modules.plugins.plugin_manager import PluginManager
from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer


class Controller:

    def __init__(self):

        self.healing = SelfHealingSystem()
        self.assets = AssetManager()
        self.quality_engine = QualityEngine()
        self.improvement_engine = ImprovementEngine()
        self.memory_engine = MemoryEngine()
        self.orchestrator = OrchestratorEngine()
        self.plugins = PluginManager()

        self.prompt_interpreter = PromptInterpreter()
        self.style_engine = StyleEngine()
        self.knowledge_engine = KnowledgeEngine()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.story_engine = StoryEngine()
        self.emotion_engine = EmotionEngine()
        self.motion_engine = MotionEngine()

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

            self.orchestrator.clear_pipeline()

            prompt_data = self.prompt_interpreter.interpret(prompt)
            self.orchestrator.register_task("prompt_interpreter")

            past_records = self.memory_engine.retrieve_similar(prompt_data)

            style = self.style_engine.determine_style(prompt_data)
            knowledge = self.knowledge_engine.collect_knowledge(prompt_data)

            video_plan = self.video_planner.create_plan(prompt_data)

            script = self.script_generator.generate_script(video_plan)

            story = self.story_engine.optimize_story(script)

            emotions = self.emotion_engine.analyze_emotions(script)

            hook = self.hook_detector.detect_hook(script)

            captions = self.caption_generator.generate_captions(script)

            scenes = self.scene_splitter.split_scenes(script)

            motion = self.motion_engine.generate_motion_plan(scenes)

            editing = self.smart_editor.analyze_editing(script, scenes)

            broll = self.broll_engine.generate_broll(scenes)

            visuals = self.visual_generator.generate_visuals(scenes)

            voice_tracks = self.voice_generator.generate_voice(scenes)

            optimized_audio = self.silence_remover.remove_silence(voice_tracks)

            images = self.image_generator.generate_images(visuals)

            composed_scenes = self.scene_composer.compose_scenes(images, voice_tracks)

            timeline = self.video_editor.assemble_video(composed_scenes)

            rendered_video = self.video_renderer.render_video(timeline)

            quality = self.quality_engine.evaluate_video(rendered_video)

            improvements = self.improvement_engine.analyze_improvements(quality)

            health = self.healing.check_system_health()

            self.assets.cleanup_assets()

            workflow = {
                "prompt_analysis": prompt_data,
                "past_records": past_records,
                "style": style,
                "knowledge": knowledge,
                "video_plan": video_plan,
                "script": script,
                "story": story,
                "emotions": emotions,
                "hook": hook,
                "captions": captions,
                "scenes": scenes,
                "motion": motion,
                "editing_plan": editing,
                "broll": broll,
                "visual_prompts": visuals,
                "voice_tracks": voice_tracks,
                "optimized_audio": optimized_audio,
                "images": images,
                "scene_videos": composed_scenes,
                "timeline": timeline,
                "rendered_video": rendered_video,
                "quality_scores": quality,
                "suggested_improvements": improvements,
                "pipeline": self.orchestrator.get_pipeline(),
                "plugins_loaded": self.plugins.list_plugins(),
                "system_health": health
            }

            self.memory_engine.store_video_record(workflow)

            return workflow

        except Exception as e:

            return {
                "error": str(e),
                "system_health": self.healing.check_system_health()
}
