import random


class VideoAnalytics:

    def __init__(self):

        self.metrics = {}

    def analyze_video(self, workflow):

        hook_score = random.uniform(6, 9)
        emotion_score = random.uniform(6, 9)
        pacing_score = random.uniform(6, 9)

        retention_score = (hook_score + emotion_score + pacing_score) / 3

        viral_probability = retention_score / 10

        analytics = {
            "hook_score": round(hook_score, 2),
            "emotion_score": round(emotion_score, 2),
            "pacing_score": round(pacing_score, 2),
            "retention_score": round(retention_score, 2),
            "viral_probability": round(viral_probability, 2)
        }

        self.metrics = analytics

        return analytics

    def get_metrics(self):

        return self.metrics
