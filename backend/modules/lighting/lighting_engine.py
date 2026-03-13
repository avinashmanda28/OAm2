class LightingEngine:

    def __init__(self):

        self.lighting_styles = [
            "soft_studio",
            "cinematic_dramatic",
            "natural_daylight",
            "warm_documentary",
            "high_contrast",
            "rim_light",
            "ambient_soft"
        ]


    def assign_lighting(self, scenes):

        lighting_scenes = []

        for index, scene in enumerate(scenes):

            lighting = self.lighting_styles[index % len(self.lighting_styles)]

            scene_data = {
                "scene": scene,
                "lighting": lighting
            }

            lighting_scenes.append(scene_data)

        return lighting_scenes


    def get_lighting(self, scene_index):

        return self.lighting_styles[scene_index % len(self.lighting_styles)]
