class StyleEngine:

    def __init__(self):
        pass

    def determine_style(self, prompt_data):

        topic = prompt_data["topic"]

        style = {
            "theme": "cinematic",
            "color_palette": "neutral",
            "visual_style": "documentary",
            "animation_level": "medium"
        }

        return {
            "video_style": style
        }
