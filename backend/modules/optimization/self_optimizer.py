class SelfOptimizer:

    def __init__(self):
        self.optimization_history = []

    def analyze_video(self, video_data):

        script = video_data.get("script", "")
        topic = video_data.get("topic", "")

        recommendations = []

        if len(script) < 500:
            recommendations.append("Script length too short, expand explanations")

        if "hook" not in script.lower():
            recommendations.append("Add stronger hook in the beginning")

        if len(topic) < 3:
            recommendations.append("Topic may be too vague")

        result = {
            "topic": topic,
            "recommendations": recommendations
        }

        self.optimization_history.append(result)

        return result

    def get_history(self):
        return self.optimization_history
