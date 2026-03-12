class MemoryEngine:

    def __init__(self):

        self.memory_store = []

    def store_video_record(self, workflow):

        record = {
            "prompt": workflow.get("prompt_analysis"),
            "style": workflow.get("style"),
            "quality": workflow.get("quality_scores"),
            "improvements": workflow.get("suggested_improvements")
        }

        self.memory_store.append(record)

        return {
            "stored_records": len(self.memory_store)
        }

    def retrieve_similar(self, prompt_data):

        topic = prompt_data.get("topic")

        matches = []

        for record in self.memory_store:

            if record["prompt"].get("topic") == topic:
                matches.append(record)

        return {
            "matches_found": len(matches),
            "records": matches
      }
