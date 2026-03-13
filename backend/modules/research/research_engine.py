class ResearchEngine:

    def __init__(self):

        self.sample_facts = [
            "Technology adoption is accelerating globally.",
            "AI investment is growing rapidly.",
            "Automation is transforming industries.",
            "Digital transformation is reshaping businesses."
        ]

    def research_topic(self, prompt_data):

        topic = prompt_data.get("topic", "technology")

        facts = self.sample_facts

        return {
            "topic": topic,
            "facts": facts
        }

    def expand_script(self, script, research_data):

        facts = research_data.get("facts", [])

        expanded_script = script + "\n\nAdditional Insights:\n"

        for fact in facts:
            expanded_script += "- " + fact + "\n"

        return expanded_script
