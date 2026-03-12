class SceneSplitter:

    def __init__(self):
        pass

    def split_scenes(self, script_data):

        topic = script_data["topic"]
        script_sections = script_data["script"]

        scenes = []

        scene_number = 1

        for section in script_sections:

            scene = {
                "scene_id": scene_number,
                "title": section["section"],
                "narration": section["text"],
                "visual_prompt": f"visual representation of {topic} for {section['section']}"
            }

            scenes.append(scene)

            scene_number += 1

        return {
            "topic": topic,
            "scenes": scenes
        }
