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
from backend.modules.memory.learning_memory import LearningMemory

from backend.modules.optimization.self_optimizer import SelfOptimizer
from backend.modules.experiments.experiment_engine import ExperimentEngine
from backend.modules.brain.multi_model_brain import MultiModelBrain
from backend.modules.marketplace.agent_marketplace import AgentMarketplace
from backend.modules.director.ai_director import AIDirector
from backend.modules.consistency.visual_consistency import VisualConsistencyEngine

from backend.modules.orchestrator.orchestrator_engine import OrchestratorEngine
from backend.modules.plugins.plugin_manager import PluginManager
from backend.modules.router.model_router import ModelRouter
from backend.modules.queue.task_queue import TaskQueue
from backend.modules.supervisor.agent_supervisor import AgentSupervisor
from backend.modules.analytics.video_analytics import VideoAnalytics

from backend.modules.workflow.workflow_engine import WorkflowEngine
from backend.modules.parallel.parallel_engine import ParallelEngine
from backend.modules.resources.resource_manager import ResourceManager
from backend.modules.communication.agent_bus import AgentBus

from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer
from backend.modules.publisher.publisher_engine import PublisherEngine


class Controller:

    def __init__(self):

        # Monitoring
        self.supervisor = AgentSupervisor()
        self.analytics = VideoAnalytics()
        self.healing = SelfHealingSystem()

        # Communication
        self.agent_bus = AgentBus()

        # Workflow
        self.workflow_engine = WorkflowEngine()
        self.model_router = ModelRouter()

        # Parallel execution
        self.parallel_engine = ParallelEngine()

        # Resource control
        self.resource_manager = ResourceManager()

        # Queue
        self.queue = TaskQueue()

        # Memory
        self.memory_engine = MemoryEngine()
        self.learning_memory = LearningMemory()

        # Optimization
        self.self_optimizer = SelfOptimizer()
        self.experiment_engine = ExperimentEngine()

        # AI Brain
        self.brain = MultiModelBrain()

        # Marketplace
        self.marketplace = AgentMarketplace()

        # Director
        self.director = AIDirector()

        # Visual consistency
        self.visual_consistency = VisualConsistencyEngine()

        # Intelligence engines
        self.trend_engine = TrendEngine()
        self.idea_engine = IdeaEngine()
        self.strategy_engine = StrategyEngine()
        self.audience_engine = AudienceEngine()
        self.viral_engine = ViralEngine()

        # Research
        self.data_collector = DataCollector()
        self.knowledge_engine = KnowledgeEngine()
        self.research_engine = ResearchEngine()

        # Planning
        self.prompt_interpreter = PromptInterpreter()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.story_engine = StoryEngine()

        # Creative
        self.emotion_engine = EmotionEngine()
        self.style_engine = StyleEngine()
        self.motion_engine = MotionEngine()

        # Scene + visuals
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()

        # Media
        self.image_generator = ImageGenerator()
        self.voice_generator = VoiceGenerator()

        # Editing
        self.caption_generator = CaptionGenerator()
        self.smart_editor = SmartEditor()
        self.broll_engine = BRollEngine()
        self.silence_remover = SilenceRemover()
        self.hook_detector = HookDetector()

        # Composition
        self.scene_composer = SceneComposer()
        self.video_editor = VideoEditor()
        self.video_renderer = VideoRenderer()

        # Optimization engines
        self.thumbnail_engine = ThumbnailEngine()
        self.seo_engine = SEOEngine()
        self.quality_engine = QualityEngine()
        self.improvement_engine = ImprovementEngine()

        # Infrastructure
        self.assets = AssetManager()
        self.orchestrator = OrchestratorEngine()
        self.plugins = PluginManager()

        # Publishing
        self.publisher_engine = PublisherEngine()

        # Register core agents
        self.marketplace.register_agent("script_generator", self.script_generator)
        self.marketplace.register_agent("image_generator", self.image_generator)
        self.marketplace.register_agent("voice_generator", self.voice_generator)
        self.marketplace.register_agent("video_editor", self.video_editor)
        self.marketplace.register_agent("renderer", self.video_renderer)

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

            resource_state = self.resource_manager.wait_for_resources()

            prompt_data = self.safe_run(
                "prompt_interpreter",
                self.prompt_interpreter.interpret,
                prompt
            )

            workflow_plan = self.workflow_engine.decide_workflow(prompt_data)

            trending_topics = self.trend_engine.get_trending_topics()
            ideas = self.idea_engine.generate_ideas(trending_topics)
            strategy = self.strategy_engine.build_strategy(ideas)

            script_model = self.brain.select_model("script")

            research_details = self.research_engine.research_topic(prompt_data)

            research_data = self.safe_run(
                "data_collector",
                self.data_collector.collect_data,
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

            experiment_results = self.experiment_engine.run_experiments(script)
            script = experiment_results["best_script"]

            direction = self.director.direct_video(script)

            script = self.research_engine.expand_script(script, research_details)

            audience_analysis = self.audience_engine.analyze_audience(script)

            scenes = direction["directed_scenes"]

            visuals = self.safe_run(
                "visual_generator",
                self.visual_generator.generate_visuals,
                scenes
            )

            visuals = self.visual_consistency.enforce_style(visuals)

            tasks = [
                {"function": self.image_generator.generate_images, "args": [visuals]},
                {"function": self.voice_generator.generate_voice, "args": [scenes]}
            ]

            results = self.parallel_engine.run_tasks(tasks)

            images = results[0]
            voice_tracks = results[1]

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

            self.queue.add_task(self.video_renderer.render_video, [timeline])

            rendered_video = "queued_render"

            thumbnail = self.thumbnail_engine.generate_thumbnail(scenes)

            metadata = self.seo_engine.generate_metadata(prompt_data, script)

            viral_prediction = self.viral_engine.predict_viral_score(script, thumbnail)

            platform_exports = self.publisher_engine.prepare_platform_exports(rendered_video)

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

            analytics = self.analytics.analyze_video({
                "script": script,
                "scenes": scenes
            })

            self.learning_memory.store_video_data({
                "topic": prompt,
                "script": script
            })

            learning_patterns = self.learning_memory.analyze_patterns()

            optimization_report = self.self_optimizer.analyze_video({
                "topic": prompt,
                "script": script
            })

            workflow_summary = self.workflow_engine.summarize_workflow(workflow_plan)

            system_health = self.healing.check_system_health()

            self.assets.cleanup_assets()

            result = {
                "resource_status": resource_state,
                "workflow_plan": workflow_plan,
                "workflow_summary": workflow_summary,
                "director_plan": direction,
                "visual_style_profile": self.visual_consistency.get_style_profile(),
                "ai_brain_models": self.brain.get_model_map(),
                "experiment_results": experiment_results,
                "learning_patterns": learning_patterns,
                "optimization_report": optimization_report,
                "available_agents": self.marketplace.list_agents(),
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
                "system_health": system_health
            }

            self.memory_engine.store_video_record(result)

            return result

        except Exception as e:

            return {
                "error": str(e),
                "system_health": self.healing.check_system_health()
            }
