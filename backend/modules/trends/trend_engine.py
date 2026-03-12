import random


class TrendEngine:

    def __init__(self):

        self.trends = [
            "Artificial Intelligence",
            "Space Exploration",
            "Future Technology",
            "Quantum Computing",
            "Climate Innovation",
            "AI Agents",
            "Digital Economy"
        ]

    def get_trending_topics(self):

        selected = random.sample(self.trends, 3)

        return {
            "trending_topics": selected
        }

    def recommend_topic(self):

        topic = random.choice(self.trends)

        return {
            "recommended_topic": topic
        }
