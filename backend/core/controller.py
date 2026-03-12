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
from backend.modules.router.model_router import ModelRouter
from backend.modules.queue.task_queue import TaskQueue
from backend.modules.supervisor.agent_supervisor import AgentSupervisor
from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer


class Controller:

    def __init__(self):

        self.supervisor = AgentSupervisor()

        self.healing = SelfHealingSystem()
        self.assets = AssetManager()
        self.quality_engine = QualityEngine()
        self.improvement_engine = ImprovementEngine()
        self.memory_engine = MemoryEngine()
        self.orchestrator = OrchestratorEngine()
        self.plugins = PluginManager()
        self.router = ModelRouter()
        self.queue = TaskQueue()

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

    def safe_run(self, name, func, *args):

        try:

            self.supervisor.register_agent(name)

            result = func(*args)

            return result

        except Exception:

            self.supervisor.report_failure(name)

            self.supervisor.restart_agent(name)

            return None

    def process_prompt(self, prompt: str):

        try:

            prompt_data = self.safe_run(
                "prompt_interpreter",
                self.prompt_interpreter.interpret,
                prompt
            )

            style = self.safe_run(
                "style_engine",
                self.style_engine.determine_style,
                prompt_data
            )

            knowledge = self.safe_run(
                "knowledge_engine",
                self.knowledge_engine.collect_knowledge,
                prompt_data
            )

            video_plan = self.safe_run(
                "video_planner",
                self.video_planner.create_plan,
                prompt_data
            )

            script = self.safe_run(
                "script_generator",
                self.script_generator.generate_script,
                video_plan
            )

            scenes = self.safe_run(
                "scene_splitter",
                self.scene_splitter.split_scenes,
                script
            )

            visuals = self.safe_run(
                "visual_generator",
                self.visual_generator.generate_visuals,
                scenes
            )

            voice_tracks = self.safe_run(
                "voice_generator",
                self.voice_generator.generate_voice,
                scenes
            )

            images = self.safe_run(
                "image_generator",
                self.image_generator.generate_images,
                visuals
            )

            composed_scenes = self.safe_run(
                "scene_composer",
                self.scene_composer.compose_scenes,
                images,
                voice_tracks
            )

            timeline = self.safe_run(
                "video_editor",
                self.video_editor.assemble_video,
                composed_scenes
            )

            rendered_video = self.safe_run(
                "video_renderer",
                self.video_renderer.render_video,
                timeline
            )

            quality = self.safe_run(
                "quality_engine",
                self.quality_engine.evaluate_video,
                rendered_video
            )

            improvements = self.safe_run(
                "improvement_engine",
                self.improvement_engine.analyze_improvements,
                quality
            )

            health = self.healing.check_system_health()

            self.assets.cleanup_assets()

            workflow = {
                "prompt_analysis": prompt_data,
                "style": style,
                "knowledge": knowledge,
                "video_plan": video_plan,
                "script": script,
                "scenes": scenes,
                "rendered_video": rendered_video,
                "quality_scores": quality,
                "suggested_improvements": improvements,
                "agent_status": self.supervisor.get_status(),
                "system_health": health
            }

            self.memory_engine.store_video_record(workflow)

            return workflow

        except Exception as e:

            return {
                "error": str(e),
                "system_health": self.healing.check_system_health()
}
