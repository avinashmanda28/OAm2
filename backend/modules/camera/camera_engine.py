class CameraEngine:

    def __init__(self):

        self.camera_styles = [
            "static",
            "slow_zoom_in",
            "slow_zoom_out",
            "pan_left",
            "pan_right",
            "orbit",
            "cinematic_push"
        ]


    def assign_camera(self, scenes):

        camera_scenes = []

        for index, scene in enumerate(scenes):

            camera = self.camera_styles[index % len(self.camera_styles)]

            scene_data = {
                "scene": scene,
                "camera_motion": camera
            }

            camera_scenes.append(scene_data)

        return camera_scenes


    def get_camera_for_scene(self, scene_index):

        return self.camera_styles[scene_index % len(self.camera_styles)]
