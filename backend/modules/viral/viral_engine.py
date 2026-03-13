import random


class ViralEngine:

    def __init__(self):

        self.virality_factors = [
            "Strong hook",
            "High curiosity topic",
            "Visual storytelling",
            "Fast pacing",
            "Emotional engagement"
        ]

    def predict_viral_score(self, script, thumbnail):

        base_score = random.randint(60, 90)

        return {
            "viral_score": base_score,
            "ctr_prediction": "High",
            "engagement_level": "Strong"
        }

    def viral_improvements(self):

        return {
            "improvement_tips": [
                "Add stronger opening hook",
                "Increase visual transitions",
                "Use more curiosity-driven storytelling",
                "Improve thumbnail contrast",
                "Use emotional triggers"
            ]
        }
