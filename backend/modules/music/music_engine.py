class MusicEngine:

    def __init__(self):

        self.music_styles = {
            "cinematic": "cinematic_background",
            "tech": "tech_ambient",
            "story": "emotional_piano",
            "education": "light_background"
        }

    def choose_music(self, prompt):

        prompt = prompt.lower()

        if "ai" in prompt or "tech" in prompt:
            return self.music_styles["tech"]

        if "story" in prompt:
            return self.music_styles["story"]

        if "explain" in prompt:
            return self.music_styles["education"]

        return self.music_styles["cinematic"]
