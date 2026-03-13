class AudienceEngine:

    def __init__(self):

        self.audience_types = [
            "Tech Enthusiasts",
            "Students",
            "Professionals",
            "Curiosity Learners",
            "Entrepreneurs"
        ]

    def analyze_audience(self, script):

        length = len(script)

        if length > 500:
            retention = "High"
        else:
            retention = "Medium"

        return {
            "audience_type": self.audience_types[0],
            "predicted_retention": retention,
            "engagement_driver": "Curiosity"
        }

    def recommend_improvements(self):

        return {
            "audience_tips": [
                "Use strong hooks in first 5 seconds",
                "Use visual explanations",
                "Maintain fast pacing",
                "Use storytelling structure"
            ]
        }
