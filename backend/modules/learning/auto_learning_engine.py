class AutoLearningEngine:

    def __init__(self):

        self.video_history = []


    def record_video(self, video_data):

        self.video_history.append(video_data)


    def analyze_patterns(self):

        topics = []

        for video in self.video_history:

            if "topic" in video:
                topics.append(video["topic"])

        return {
            "videos_analyzed": len(self.video_history),
            "topics": topics
        }
