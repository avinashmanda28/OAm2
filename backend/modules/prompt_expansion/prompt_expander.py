class PromptExpansionEngine:

    def __init__(self):
        pass

    def expand_prompt(self, prompt):

        expansion = {
            "topic": prompt,
            "hooks": [
                f"Why {prompt} will change everything",
                f"The shocking truth about {prompt}"
            ],
            "subtopics": [
                f"Introduction to {prompt}",
                f"How {prompt} works",
                f"Real world examples of {prompt}",
                f"Future impact of {prompt}"
            ],
            "visual_ideas": [
                "animated explanation",
                "diagram visualization",
                "cinematic storytelling"
            ],
            "story_structure": [
                "hook",
                "problem",
                "explanation",
                "examples",
                "future",
                "conclusion"
            ]
        }

        return expansion
