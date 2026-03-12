class VideoPlanner:

    def __init__(self):
        pass

    def create_plan(self, prompt_data):

        topic = prompt_data["topic"]
        style = prompt_data["style"]
        length = prompt_data["target_length"]

        plan = {
            "topic": topic,
            "style": style,
            "length": length,
            "structure": [
                {
                    "section": "Hook",
                    "description": f"Strong opening about {topic}"
                },
                {
                    "section": "Introduction",
                    "description": f"Introduce the topic {topic}"
                },
                {
                    "section": "Main Explanation",
                    "description": f"Explain the core concept of {topic}"
                },
                {
                    "section": "Examples",
                    "description": f"Give real world examples of {topic}"
                },
                {
                    "section": "Conclusion",
                    "description": f"Summarize the topic {topic}"
                }
            ]
        }

        return plan
