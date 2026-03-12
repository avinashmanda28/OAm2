import re


class PromptInterpreter:

    def __init__(self):
        self.supported_platforms = [
            "youtube",
            "tiktok",
            "instagram",
            "shorts"
        ]

    def interpret(self, prompt: str):

        result = {
            "topic": None,
            "style": "educational",
            "tone": "neutral",
            "target_length": "8 minutes",
            "platform": "youtube"
        }

        prompt_lower = prompt.lower()

        # Detect platform
        for platform in self.supported_platforms:
            if platform in prompt_lower:
                result["platform"] = platform

        # Detect length
        length_match = re.search(r"(\d+)\s*(minute|min)", prompt_lower)
        if length_match:
            result["target_length"] = f"{length_match.group(1)} minutes"

        # Detect style
        if "story" in prompt_lower:
            result["style"] = "storytelling"

        if "documentary" in prompt_lower:
            result["style"] = "documentary"

        if "tutorial" in prompt_lower:
            result["style"] = "tutorial"

        # Detect tone
        if "funny" in prompt_lower:
            result["tone"] = "entertaining"

        if "serious" in prompt_lower:
            result["tone"] = "serious"

        if "simple" in prompt_lower:
            result["tone"] = "simple"

        # Topic detection (basic fallback)
        topic_words = prompt.split(" ")
        if len(topic_words) > 2:
            result["topic"] = " ".join(topic_words[:4])
        else:
            result["topic"] = prompt

        return result
