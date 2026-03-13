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
from backend.modules.data.data_collector import DataCollector
from backend.modules.research.research_engine import ResearchEngine

from backend.modules.thumbnail.thumbnail_engine import ThumbnailEngine
from backend.modules.seo.seo_engine import SEOEngine
from backend.modules.trends.trend_engine import TrendEngine
from backend.modules.ideas.idea_engine import IdeaEngine
from backend.modules.strategy.strategy_engine import StrategyEngine
from backend.modules.audience.audience_engine import AudienceEngine
from backend.modules.viral.viral_engine import ViralEngine

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
from backend.modules.analytics.video_analytics import VideoAnalytics

from backend.modules.workflow.workflow_engine import WorkflowEngine

from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer

from backend.modules.publisher.publisher_engine import PublisherEngine


class Controller:

    def __init__(self):

        # Core systems
        self.supervisor = AgentSupervisor()
        self.analytics = VideoAnalytics()
        self.healing = SelfHealingSystem()

        # Workflow engine
        self.workflow_engine = WorkflowEngine()

        # Intelligence engines
        self.trend_engine = TrendEngine()
        self.idea_engine = IdeaEngine()
        self.strategy_engine = StrategyEngine()
        self.audience_engine = AudienceEngine()
        self.viral_engine = ViralEngine()

        # Research systems
        self.data_collector = DataCollector()
        self.knowledge_engine = KnowledgeEngine()
        self.research_engine = ResearchEngine()

        # Planning engines
        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.story_engine = StoryEngine()

        # Creative engines
        self.emotion_engine = EmotionEngine()
        self.style_engine = StyleEngine()
        self.motion_engine = MotionEngine()

        # Scene generation
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()

        # Media generation
        self.image_generator = ImageGenerator()
        self.voice_generator = VoiceGenerator()

        # Editing systems
        self.caption_generator = CaptionGenerator()
        self.smart_editor = SmartEditor()
        self.broll_engine = BRollEngine()
        self.silence_remover = SilenceRemover()
        self.hook_detector = HookDetector()

        # Composition
        self.scene_composer = SceneComposer()
        self.video_editor = VideoEditor()
        self.video_renderer = VideoRenderer()

        # Optimization
        self.thumbnail_engine = ThumbnailEngine()
        self.seo_engine = SEOEngine()
        self.quality_engine = QualityEngine()
        self.improvement_engine = ImprovementEngine()

        # Infrastructure
        self.assets = AssetManager()
        self.memory_engine = MemoryEngine()
        self.orchestrator = OrchestratorEngine()
        self.plugins = PluginManager()
        self.router = ModelRouter()
        self.queue = TaskQueue()

        # Publishing
        self.publisher_engine = PublisherEngine()

    def safe_run(self, name, func, *args):

        try:
            self.supervisor.register_agent(name)
            return func(*args)

        except Exception:
            self.supervisor.report_failure(name)
            self.supervisor.restart_agent(name)
            return None

    def process_prompt(self, prompt: str):

        try:

            # Prompt interpretation
            prompt_data = self.safe_run(
                "prompt_interpreter",
                self.prompt_interpreter.interpret,
                prompt
            )

            # Decide workflow dynamically
            workflow_plan = self.workflow_engine.decide_workflow(prompt_data)

            # Trend detection
            trending_topics = self.trend_engine.get_trending_topics()

            # Idea generation
            ideas = self.idea_engine.generate_ideas(trending_topics)

            # Strategy generation
            strategy = self.strategy_engine.build_strategy(ideas)

            # Research topic
            research_details = self.research_engine.research_topic(prompt_data)

            # Data collection
            research_data = self.safe_run(
                "data_collector",
                self.data_collector.collect_data,
                prompt_data
            )

            # Video planning
            video_plan = self.safe_run(
                "video_planner",
                self.video_planner.create_plan,
                prompt_data
            )

            # Script generation
            script = self.safe_run(
                "script_generator",
                self.script_generator.generate_script,
                video_plan
            )

            # Expand script using research
            script = self.research_engine.expand_script(script, research_details)

            # Audience analysis
            audience_analysis = self.audience_engine.analyze_audience(script)

            # Scene splitting
            scenes = self.safe_run(
                "scene_splitter",
                self.scene_splitter.split_scenes,
                script
            )

            # Visual prompts
            visuals = self.safe_run(
                "visual_generator",
                self.visual_generator.generate_visuals,
                scenes
            )

            # Image generation
            images = self.safe_run(
                "image_generator",
                self.image_generator.generate_images,
                visuals
            )

            # Voice generation
            voice_tracks = self.safe_run(
                "voice_generator",
                self.voice_generator.generate_voice,
                scenes
            )

            # Compose scenes
            composed_scenes = self.safe_run(
                "scene_composer",
                self.scene_composer.compose_scenes,
                images,
                voice_tracks
            )

            # Assemble video
            timeline = self.safe_run(
                "video_editor",
                self.video_editor.assemble_video,
                composed_scenes
            )

            # Render video
            rendered_video = self.safe_run(
                "video_renderer",
                self.video_renderer.render_video,
                timeline
            )

            # Thumbnail
            thumbnail = self.thumbnail_engine.generate_thumbnail(scenes)

            # SEO metadata
            metadata = self.seo_engine.generate_metadata(prompt_data, script)

            # Viral prediction
            viral_prediction = self.viral_engine.predict_viral_score(script, thumbnail)

            # Multi-platform export
            platform_exports = self.publisher_engine.prepare_platform_exports(rendered_video)

            # Quality evaluation
            quality = self.safe_run(
                "quality_engine",
                self.quality_engine.evaluate_video,
                rendered_video
            )

            # Improvements
            improvements = self.safe_run(
                "improvement_engine",
                self.improvement_engine.analyze_improvements,
                quality
            )

            # Analytics
            analytics = self.analytics.analyze_video({
                "script": script,
                "scenes": scenes
            })

            # Workflow summary
            workflow_summary = self.workflow_engine.summarize_workflow(workflow_plan)

            # System health
            health = self.healing.check_system_health()

            # Cleanup assets
            self.assets.cleanup_assets()

            result = {
                "workflow_plan": workflow_plan,
                "workflow_summary": workflow_summary,
                "trending_topics": trending_topics,
                "ideas": ideas,
                "strategy": strategy,
                "prompt_analysis": prompt_data,
                "research_details": research_details,
                "research_data": research_data,
                "video_plan": video_plan,
                "script": script,
                "audience_analysis": audience_analysis,
                "scenes": scenes,
                "thumbnail": thumbnail,
                "seo_metadata": metadata,
                "viral_prediction": viral_prediction,
                "rendered_video": rendered_video,
                "platform_exports": platform_exports,
                "quality_scores": quality,
                "analytics": analytics,
                "suggested_improvements": improvements,
                "agent_status": self.supervisor.get_status(),
                "system_health": health
            }

            # Save to memory
            self.memory_engine.store_video_record(result)

            return result

        except Exception as e:

            return {
                "error": str(e),
                "system_health": self.healing.check_system_health()
            }
