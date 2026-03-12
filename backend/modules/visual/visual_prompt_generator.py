class VisualPromptGenerator:

    def __init__(self):
        pass

    def generate_visuals(self, scene_data):

        topic = scene_data["topic"]
        scenes = scene_data["scenes"]

        visual_prompts = []

        for scene in scenes:

            narration = scene["narration"]

            visual_prompt = (
                f"cinematic visual representation of {topic}, "
                f"scene about {scene['title']}, "
                f"detailed environment, dramatic lighting, "
                f"high quality film composition"
            )

            visual_prompts.append({
                "scene_id": scene["scene_id"],
                "title": scene["title"],
                "narration": narration,
                "visual_prompt": visual_prompt
            })

        return {
            "topic": topic,
            "visual_scenes": visual_prompts
      }
