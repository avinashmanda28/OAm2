import random


class ThumbnailEngine:

    def __init__(self):

        self.thumbnails = []

    def generate_thumbnail(self, scenes):

        if not scenes:
            return None

        selected_scene = random.choice(scenes)

        thumbnail = {
            "selected_scene": selected_scene,
            "confidence_score": round(random.uniform(0.7, 0.95), 2),
            "style": "high_contrast"
        }

        self.thumbnails.append(thumbnail)

        return thumbnail

    def list_thumbnails(self):

        return self.thumbnails
