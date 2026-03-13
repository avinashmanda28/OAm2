class ChapterEngine:

    def __init__(self):
        pass


    def generate_chapters(self, scenes):

        chapters = []

        current_time = 0

        for i, scene in enumerate(scenes):

            title = scene.get("title", f"Scene {i+1}")

            timestamp = self.seconds_to_timestamp(current_time)

            chapters.append({
                "timestamp": timestamp,
                "title": title
            })

            # assume average scene length
            current_time += 30

        return chapters


    def seconds_to_timestamp(self, seconds):

        minutes = seconds // 60
        seconds = seconds % 60

        return f"{int(minutes):02d}:{int(seconds):02d}"
