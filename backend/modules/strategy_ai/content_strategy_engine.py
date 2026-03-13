class ContentStrategyEngine:

    def __init__(self):

        self.history = []

    def record_video(self, video_data):

        self.history.append(video_data)

    def analyze_history(self):

        if len(self.history) == 0:

            return {
                "best_topics": [],
                "recommendation": "collect more data"
            }

        topics = [v.get("topic") for v in self.history if "topic" in v]

        topic_frequency = {}

        for t in topics:

            topic_frequency[t] = topic_frequency.get(t, 0) + 1

        best_topics = sorted(
            topic_frequency,
            key=topic_frequency.get,
            reverse=True
        )

        return {
            "best_topics": best_topics[:5],
            "recommendation": "focus on top performing niches"
        }

    def suggest_next_video(self):

        analysis = self.analyze_history()

        if len(analysis["best_topics"]) == 0:

            return "Create a trending topic video"

        return f"Create another video about {analysis['best_topics'][0]}"
