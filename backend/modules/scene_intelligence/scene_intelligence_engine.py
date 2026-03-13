class SceneIntelligenceEngine:

    def __init__(self):
        pass

    def analyze_scenes(self, scenes):

        analyzed_scenes = []

        for index, scene in enumerate(scenes):

            scene_data = {
                "scene_id": index,
                "content": scene,
                "duration": self.estimate_duration(scene),
                "complexity": self.estimate_complexity(scene),
                "visual_density": self.estimate_visual_density(scene),
                "transition": self.choose_transition(index)
            }

            analyzed_scenes.append(scene_data)

        return analyzed_scenes


    def estimate_duration(self, scene):

        words = len(scene.split())

        duration = max(4, min(12, words // 3))

        return duration


    def estimate_complexity(self, scene):

        words = len(scene.split())

        if words < 10:
            return "low"

        if words < 25:
            return "medium"

        return "high"


    def estimate_visual_density(self, scene):

        words = len(scene.split())

        if words < 15:
            return "light"

        if words < 30:
            return "medium"

        return "heavy"


    def choose_transition(self, index):

        transitions = [
            "cut",
            "fade",
            "zoom",
            "slide"
        ]

        return transitions[index % len(transitions)]
