class StrategyEngine:

    def __init__(self):

        self.upload_frequency = "3 videos per week"

    def build_strategy(self, ideas):

        idea_list = ideas.get("generated_ideas", [])

        calendar = []

        for i, idea in enumerate(idea_list):

            entry = {
                "week": 1,
                "video_number": i + 1,
                "title": idea
            }

            calendar.append(entry)

        return {
            "upload_frequency": self.upload_frequency,
            "content_calendar": calendar
        }

    def recommend_growth_plan(self):

        return {
            "growth_strategy": [
                "Post consistently",
                "Focus on trending topics",
                "Use strong hooks in first 5 seconds",
                "Optimize thumbnails and titles",
                "Build series-based content"
            ]
              }
