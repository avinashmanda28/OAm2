class PublisherEngine:

    def __init__(self):

        self.platform_formats = {
            "youtube": "16:9",
            "shorts": "9:16",
            "tiktok": "9:16",
            "instagram": "1:1"
        }

    def prepare_platform_exports(self, video_file):

        exports = []

        for platform, ratio in self.platform_formats.items():

            exports.append({
                "platform": platform,
                "aspect_ratio": ratio,
                "video_source": video_file
            })

        return {
            "platform_exports": exports
        }

    def publishing_recommendations(self):

        return {
            "recommendations": [
                "Post Shorts 3-5 times per week",
                "Upload long videos weekly",
                "Use same content repurposed across platforms",
                "Optimize captions for vertical viewing"
            ]
      }
