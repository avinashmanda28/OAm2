# OAm² MASTER CONTROLLER
# Main brain of the AI video factory


# -----------------------------
# IMPORT ALL MODULES
# -----------------------------

from backend.modules.prompt.prompt_interpreter import PromptInterpreter
from backend.modules.prompt_expansion.prompt_expander import PromptExpansionEngine
from backend.modules.planner.video_planner import VideoPlanner
from backend.modules.script.script_generator import ScriptGenerator
from backend.modules.story.story_engine import StoryEngine
from backend.modules.scene.scene_splitter import SceneSplitter

from backend.modules.visual.visual_prompt_generator import VisualPromptGenerator
from backend.modules.image.image_generator import ImageGenerator
from backend.modules.voice.voice_generator import VoiceGenerator

from backend.modules.caption.caption_generator import CaptionGenerator
from backend.modules.smart_edit.smart_editor import SmartEditor
from backend.modules.broll.broll_engine import BRollEngine
from backend.modules.silence.silence_remover import SilenceRemover
from backend.modules.hook.hook_detector import HookDetector

from backend.modules.scene_intelligence.scene_intelligence_engine import SceneIntelligenceEngine
from backend.modules.camera.camera_engine import CameraEngine
from backend.modules.lighting.lighting_engine import LightingEngine
from backend.modules.style_transfer.style_transfer_engine import StyleTransferEngine

from backend.modules.sound.sound_engine import SoundEngine
from backend.modules.music.music_engine import MusicEngine
from backend.modules.narrative.narrative_engine import NarrativeEngine

from backend.modules.context.context_engine import ContextEngine
from backend.modules.retrieval.retrieval_engine import RetrievalEngine

from backend.modules.timing.timing_engine import TimingEngine
from backend.modules.render_opt.render_optimizer import RenderOptimizer
from backend.modules.compute.gpu_scheduler import GPUScheduler

from backend.modules.error_prediction.error_prediction_engine import ErrorPredictionEngine
from backend.modules.batch.batch_engine import BatchEngine

from backend.modules.learning.auto_learning_engine import AutoLearningEngine
from backend.modules.evolution.system_evolution_engine import SystemEvolutionEngine

from backend.modules.visual_memory.visual_memory_engine import VisualMemoryEngine

from backend.modules.assets.asset_manager import AssetManager
from backend.modules.quality.quality_engine import QualityEngine
from backend.modules.thumbnail.thumbnail_engine import ThumbnailEngine
from backend.modules.seo.seo_engine import SEOEngine

from backend.modules.trends.trend_engine import TrendEngine
from backend.modules.ideas.idea_engine import IdeaEngine
from backend.modules.strategy.strategy_engine import StrategyEngine
from backend.modules.analytics.video_analytics import VideoAnalytics

from backend.modules.healing.self_healing import SelfHealingSystem


# -----------------------------
# CONTROLLER CLASS
# -----------------------------

class Controller:

    def __init__(self):

        # Prompt engines
        self.prompt_interpreter = PromptInterpreter()
        self.prompt_expander = PromptExpansionEngine()

        # Planning engines
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.story_engine = StoryEngine()

        # Scene engines
        self.scene_splitter = SceneSplitter()
        self.scene_intelligence = SceneIntelligenceEngine()

        # Visual engines
        self.visual_generator = VisualPromptGenerator()
        self.image_generator = ImageGenerator()
        self.visual_memory = VisualMemoryEngine()

        # Camera & lighting
        self.camera_engine = CameraEngine()
        self.lighting_engine = LightingEngine()
        self.style_engine = StyleTransferEngine()

        # Audio engines
        self.voice_generator = VoiceGenerator()
        self.sound_engine = SoundEngine()
        self.music_engine = MusicEngine()

        # Editing engines
        self.caption_generator = CaptionGenerator()
        self.smart_editor = SmartEditor()
        self.broll_engine = BRollEngine()
        self.silence_remover = SilenceRemover()
        self.hook_detector = HookDetector()

        # Intelligence engines
        self.narrative_engine = NarrativeEngine()
        self.context_engine = ContextEngine()
        self.retrieval_engine = RetrievalEngine()

        # Performance engines
        self.timing_engine = TimingEngine()
        self.render_optimizer = RenderOptimizer()
        self.gpu_scheduler = GPUScheduler()

        # Reliability engines
        self.error_predictor = ErrorPredictionEngine()
        self.self_healing = SelfHealingSystem()

        # Batch processing
        self.batch_engine = BatchEngine()

        # Learning engines
        self.auto_learning = AutoLearningEngine()
        self.system_evolution = SystemEvolutionEngine()

        # Assets
        self.asset_manager = AssetManager()

        # Optimization engines
        self.quality_engine = QualityEngine()
        self.thumbnail_engine = ThumbnailEngine()
        self.seo_engine = SEOEngine()

        # Intelligence systems
        self.trend_engine = TrendEngine()
        self.idea_engine = IdeaEngine()
        self.strategy_engine = StrategyEngine()
        self.analytics_engine = VideoAnalytics()


    # ------------------------------------------------
    # MAIN VIDEO CREATION PIPELINE
    # ------------------------------------------------

    def create_video(self, prompt):

        try:

            # 1 Prompt interpretation
            prompt_data = self.prompt_interpreter.interpret(prompt)

            # 2 Prompt expansion
            expanded_prompt = self.prompt_expander.expand_prompt(prompt)

            # 3 Trend analysis
            trends = self.trend_engine.get_trending_topics()

            ideas = self.idea_engine.generate_ideas(trends)

            strategy = self.strategy_engine.build_strategy(ideas)

            # 4 Knowledge retrieval
            knowledge = self.retrieval_engine.retrieve_knowledge(prompt)

            # 5 Video planning
            video_plan = self.video_planner.create_plan(prompt_data)

            # 6 Script generation
            script = self.script_generator.generate_script(video_plan)

            script = self.narrative_engine.improve_story(script)

            # 7 Scene creation
            scenes = self.scene_splitter.split_scenes(script)

            scenes = self.scene_intelligence.analyze_scenes(scenes)

            # 8 Camera & lighting
            scenes = self.camera_engine.assign_camera(scenes)

            scenes = self.lighting_engine.assign_lighting(scenes)

            # 9 Visual generation
            visuals = self.visual_generator.generate_visuals(scenes)

            visuals = self.style_engine.apply_style(visuals)

            # 10 Image generation
            images = self.image_generator.generate_images(visuals)

            # Store visuals
            for img in images:
                self.visual_memory.store_visual("scene_asset", img)

            # 11 Voice
            voice_tracks = self.voice_generator.generate_voice(scenes)

            # 12 Audio design
            sound = self.sound_engine.assign_sounds(scenes)

            music = self.music_engine.choose_music(prompt)

            # 13 Editing
            captions = self.caption_generator.generate_captions(script)

            edited = self.smart_editor.edit_video(images)

            edited = self.silence_remover.remove_silence(edited)

            edited = self.broll_engine.add_broll(edited)

            # 14 Timing
            timed_scenes = self.timing_engine.optimize_timing(scenes)

            # 15 Render optimization
            render_settings = self.render_optimizer.optimize(timed_scenes)

            # 16 Thumbnail
            thumbnail = self.thumbnail_engine.generate_thumbnail(scenes)

            # 17 SEO
            seo = self.seo_engine.generate_metadata(prompt, script)

            # 18 Quality check
            quality = self.quality_engine.evaluate_video(edited)

            # 19 Analytics
            analytics = self.analytics_engine.analyze_video({
                "script": script,
                "scenes": scenes
            })

            # 20 Learning
            self.auto_learning.record_video({
                "topic": prompt
            })

            learning_data = self.auto_learning.analyze_patterns()

            # 21 System evolution
            evolution = self.system_evolution.evaluate_system({
                "errors": 0
            })

            return {

                "prompt": prompt,
                "expanded_prompt": expanded_prompt,
                "knowledge": knowledge,
                "trends": trends,
                "ideas": ideas,
                "strategy": strategy,
                "script": script,
                "scenes": scenes,
                "images": images,
                "voice": voice_tracks,
                "music": music,
                "captions": captions,
                "thumbnail": thumbnail,
                "seo": seo,
                "quality": quality,
                "analytics": analytics,
                "learning": learning_data,
                "evolution": evolution

            }

        except Exception as e:

            self.self_healing.check_system_health()

            return {
                "error": str(e)
            }
