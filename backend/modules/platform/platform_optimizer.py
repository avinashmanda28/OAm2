class PlatformOptimizer:

    def __init__(self):

        self.platform_profiles = {
            "youtube": {
                "aspect_ratio": "16:9",
                "style": "long_form",
                "recommended_length": "8-15 minutes"
            },
            "shorts": {
                "aspect_ratio": "9:16",
                "style": "fast_paced",
                "recommended_length": "15-60 seconds"
            },
            "tiktok": {
                "aspect_ratio": "9:16",
                "style": "hook_intensive",
                "recommended_length": "15-60 seconds"
            },
            "instagram": {
                "aspect_ratio": "1:1",
                "style": "visual",
                "recommended_length": "30-90 seconds"
            }
        }

    def optimize_for_platform(self, video_data):

        optimized_outputs = {}

        for platform, profile in self.platform_profiles.items():

            optimized_outputs[platform] = {
                "aspect_ratio": profile["aspect_ratio"],
                "style": profile["style"],
                "recommended_length": profile["recommended_length"],
                "video_source": video_data
            }

        return optimized_outputs
