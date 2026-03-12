class EmotionEngine:

    def __init__(self):
        pass

    def analyze_emotions(self, script_data):

        sections = script_data["script"]

        emotions = []

        for section in sections:

            emotions.append({
                "scene_id": section["scene_id"],
                "emotion": "neutral"
            })

        return {
            "scene_emotions": emotions
        }
