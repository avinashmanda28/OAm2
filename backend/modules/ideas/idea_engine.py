import random


class IdeaEngine:

    def __init__(self):

        self.idea_templates = [
            "The Future of {topic}",
            "Why {topic} Will Change Everything",
            "The Hidden Truth About {topic}",
            "What Nobody Tells You About {topic}",
            "How {topic} Is Transforming the World"
        ]

    def generate_ideas(self, trending_topics):

        topics = trending_topics.get("trending_topics", [])

        ideas = []

        for topic in topics:

            template = random.choice(self.idea_templates)

            idea = template.format(topic=topic)

            ideas.append(idea)

        return {
            "generated_ideas": ideas
        }

    def generate_series(self, topic):

        series = [
            f"{topic} Explained",
            f"The History of {topic}",
            f"The Future of {topic}",
            f"{topic} Case Studies"
        ]

        return {
            "series_suggestions": series
                                     }
