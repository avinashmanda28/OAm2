class VisualConsistencyEngine:

    def __init__(self):

        self.style_profile = {
            "color_palette": "cinematic",
            "lighting": "dramatic",
            "camera_style": "smooth",
            "character_style": "consistent"
        }

    def enforce_style(self, visuals):

        consistent_visuals = []

        for v in visuals:

            visual = {
                "prompt": v,
                "style": self.style_profile
            }

            consistent_visuals.append(visual)

        return consistent_visuals

    def update_style(self, style_dict):

        for k, v in style_dict.items():
            self.style_profile[k] = v

    def get_style_profile(self):

        return self.style_profile
