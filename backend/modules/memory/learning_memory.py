class LearningMemory:

    def __init__(self):

        self.video_history = []

    def store_video_data(self, data):

        self.video_history.append(data)

    def get_history(self):

        return self.video_history

    def analyze_patterns(self):

        if len(self.video_history) == 0:
            return None

        topics = {}

        for video in self.video_history:

            topic = video.get("topic")

            if topic not in topics:
                topics[topic] = 0

            topics[topic] += 1

        return {
            "topic_frequency": topics
        }

    def best_topics(self):

        patterns = self.analyze_patterns()

        if patterns is None:
            return None

        topics = patterns["topic_frequency"]

        sorted_topics = sorted(
            topics.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_topics
