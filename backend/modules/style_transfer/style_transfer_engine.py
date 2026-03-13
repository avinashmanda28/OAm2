class StyleTransferEngine:

    def __init__(self):

        self.available_styles = [
            "cinematic",
            "documentary",
            "futuristic",
            "minimal_explainer",
            "realistic",
            "anime_cinematic"
        ]


    def apply_style(self, visuals, style="cinematic"):

        styled_visuals = []

        for visual in visuals:

            visual_data = {
                "visual": visual,
                "style": style
            }

            styled_visuals.append(visual_data)

        return styled_visuals


    def choose_style(self, prompt):

        prompt = prompt.lower()

        if "ai" in prompt or "future" in prompt:
            return "futuristic"

        if "explain" in prompt:
            return "minimal_explainer"

        if "story" in prompt:
            return "cinematic"

        return "documentary"
