class AIDirector:

    def __init__(self):

        self.structure_template = [
            "HOOK",
            "INTRO",
            "CONTEXT",
            "MAIN_EXPLANATION",
            "VISUAL_SECTION",
            "EXAMPLE",
            "CLIMAX",
            "CONCLUSION"
        ]

    def design_story_flow(self, script):

        scenes = []

        sections = script.split("\n")

        for i, section in enumerate(sections):

            part = self.structure_template[i % len(self.structure_template)]

            scenes.append({
                "type": part,
                "content": section
            })

        return scenes

    def analyze_pacing(self, scenes):

        pacing = []

        for s in scenes:

            if s["type"] == "HOOK":
                pacing.append("fast")

            elif s["type"] == "CLIMAX":
                pacing.append("intense")

            else:
                pacing.append("normal")

        return pacing

    def direct_video(self, script):

        scenes = self.design_story_flow(script)

        pacing = self.analyze_pacing(scenes)

        return {
            "directed_scenes": scenes,
            "pacing_plan": pacing
        }
