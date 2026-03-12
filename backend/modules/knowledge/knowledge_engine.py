class KnowledgeEngine:

    def __init__(self):
        pass

    def collect_knowledge(self, prompt_data):

        topic = prompt_data["topic"]

        knowledge = {
            "topic": topic,
            "facts": [
                f"{topic} is an important concept",
                f"{topic} has many real world applications",
                f"{topic} is widely studied in modern technology"
            ],
            "sources": [
                "wikipedia",
                "web",
                "general knowledge"
            ]
        }

        return knowledge
