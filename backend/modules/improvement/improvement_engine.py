class ImprovementEngine:

    def __init__(self):
        pass

    def analyze_improvements(self, quality_scores):

        scores = quality_scores["quality_scores"]

        improvements = []

        if scores["hook_score"] < 7:
            improvements.append("improve_hook")

        if scores["story_score"] < 7:
            improvements.append("improve_story")

        if scores["visual_score"] < 7:
            improvements.append("improve_visuals")

        return {
            "suggested_improvements": improvements
        }
