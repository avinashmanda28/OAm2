class DataCollector:

    def __init__(self):

        self.sources = [
            "wikipedia",
            "news",
            "scientific_articles",
            "public_datasets"
        ]

    def collect_data(self, prompt_data):

        topic = prompt_data.get("topic", "general")

        collected_data = {
            "topic": topic,
            "sources_used": self.sources,
            "facts": [
                f"Basic information about {topic}",
                f"Historical context of {topic}",
                f"Recent developments related to {topic}"
            ]
        }

        return collected_data

    def list_sources(self):

        return self.sources
