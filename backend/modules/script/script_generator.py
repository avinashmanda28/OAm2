class ScriptGenerator:

    def __init__(self):
        pass

    def generate_script(self, video_plan):

        topic = video_plan["topic"]

        script = []

        for section in video_plan["structure"]:

            section_name = section["section"]
            description = section["description"]

            text = f"{section_name}: {description}. In this part of the video we explore {topic} in detail."

            script.append({
                "section": section_name,
                "text": text
            })

        return {
            "topic": topic,
            "script": script
        }
