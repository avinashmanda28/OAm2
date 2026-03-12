import random


class SEOEngine:

    def __init__(self):

        self.templates = [
            "The Truth About {topic}",
            "What Nobody Tells You About {topic}",
            "The Hidden Secrets of {topic}",
            "The Future of {topic}",
            "Everything You Need to Know About {topic}"
        ]

    def generate_metadata(self, prompt_data, script):

        topic = prompt_data.get("topic", "technology")

        title_template = random.choice(self.templates)

        title = title_template.format(topic=topic)

        description = f"""
This video explains {topic} in a clear and engaging way.

In this video you will learn:
- key concepts about {topic}
- why it matters today
- important insights and examples

Subscribe for more educational content.
"""

        tags = [
            topic,
            f"{topic} explained",
            f"{topic} tutorial",
            "education",
            "documentary"
        ]

        metadata = {
            "title": title,
            "description": description.strip(),
            "tags": tags
        }

        return metadata
