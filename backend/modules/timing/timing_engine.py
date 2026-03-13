class TimingEngine:

    def __init__(self):
        pass

    def optimize_timing(self, scenes):

        optimized = []

        for scene in scenes:

            scene_data = {
                "scene": scene,
                "recommended_duration": self.calculate_duration(scene)
            }

            optimized.append(scene_data)

        return optimized


    def calculate_duration(self, scene):

        words = len(scene.split())

        duration = max(4, min(15, words // 2))

        return duration
