class StyleConsistencyEngine:

    def __init__(self):

        self.style_profile = {
            "color_palette": "cinematic",
            "lighting": "soft studio lighting",
            "visual_style": "modern youtube documentary",
            "camera_style": "dynamic"
        }

    def enforce_style(self, visuals):

        styled_visuals = []

        for v in visuals:

            visual = v.copy()

            visual["style"] = self.style_profile

            styled_visuals.append(visual)

        return styled_visuals

    def get_style_profile(self):

        return self.style_profile

    def update_style(self, new_style):

        self.style_profile.update(new_style)
