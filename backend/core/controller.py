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
from backend.modules.composer.scene_composer import SceneComposer
from backend.modules.editor.video_editor import VideoEditor
from backend.modules.renderer.video_renderer import VideoRenderer


class Controller:

    def __init__(self):

        # System monitoring
        self.healing = SelfHealingSystem()

        # Core AI modules
        self.prompt_interpreter = PromptInterpreter()
        self.style_engine = StyleEngine()
        self.knowledge_engine = KnowledgeEngine()
        self.video_planner = VideoPlanner()
        self.script_generator = ScriptGenerator()
        self.story_engine = StoryEngine()
        self.emotion_engine = EmotionEngine()

        # Scene modules
        self.scene_splitter = SceneSplitter()
        self.visual_generator = VisualPromptGenerator()

        # Media generation
        self.voice_generator = VoiceGenerator()
        self.image_generator = ImageGenerator()

        # Video intelligence
        self.caption_generator = CaptionGenerator()
        self.smart_editor = SmartEditor()
        self.broll_engine = BRollEngine()
        self.silence_remover = SilenceRemover()
        self.hook_detector = HookDetector()

        # Composition
        self.scene_composer = SceneComposer()
        self.video_editor = VideoEditor()
        self.video_renderer = VideoRenderer()

    def process_prompt(self, prompt: str):

        try:

            # STEP 1 — Prompt Analysis
            prompt_data = self.prompt_interpreter.interpret(prompt)
            self.healing.monitor_module("prompt_interpreter", "ok")

            # STEP 2 — Determine Visual Style
            style = self.style_engine.determine_style(prompt_data)

            # STEP 3 — Collect Knowledge
            knowledge = self.knowledge_engine.collect_knowledge(prompt_data)
            self.healing.monitor_module("knowledge_engine", "ok")

            # STEP 4 — Plan Video Structure
            video_plan = self.video_planner.create_plan(prompt_data)

            # STEP 5 — Generate Script
            script = self.script_generator.generate_script(video_plan)
            self.healing.monitor_module("script_generator", "ok")

            # STEP 6 — Optimize Story
            story = self.story_engine.optimize_story(script)

            # STEP 7 — Emotion Detection
            emotions = self.emotion_engine.analyze_emotions(script)

            # STEP 8 — Detect Hook
            hook = self.hook_detector.detect_hook(script)

            # STEP 9 — Generate Captions
            captions = self.caption_generator.generate_captions(script)

            # STEP 10 — Split Scenes
            scenes = self.scene_splitter.split_scenes(script)

            # STEP 11 — Smart Editing Plan
            editing = self.smart_editor.analyze_editing(script, scenes)

            # STEP 12 — B-Roll Suggestions
            broll = self.broll_engine.generate_broll(scenes)

            # STEP 13 — Generate Visual Prompts
            visuals = self.visual_generator.generate_visuals(scenes)

            # STEP 14 — Generate Voice
            voice_tracks = self.voice_generator.generate_voice(scenes)

            # STEP 15 — Remove Silence
            optimized_audio = self.silence_remover.remove_silence(voice_tracks)

            # STEP 16 — Generate Images
            images = self.image_generator.generate_images(visuals)

            # STEP 17 — Compose Scenes
            composed_scenes = self.scene_composer.compose_scenes(images, voice_tracks)

            # STEP 18 — Assemble Video Timeline
            timeline = self.video_editor.assemble_video(composed_scenes)

            # STEP 19 — Render Final Video
            rendered_video = self.video_renderer.render_video(timeline)

            # STEP 20 — System Health Check
            health = self.healing.check_system_health()

            workflow = {
                "prompt_analysis": prompt_data,
                "style": style,
                "knowledge": knowledge,
                "video_plan": video_plan,
                "script": script,
                "story": story,
                "emotions": emotions,
                "hook": hook,
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
