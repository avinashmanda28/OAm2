class MotionEngine:

    def __init__(self):
        pass

    def generate_motion_plan(self, scenes):

        motion_plan = []

        for scene in scenes["scenes"]:

            motion_plan.append({
                "scene_id": scene["scene_id"],
                "camera_motion": "slow_zoom",
                "parallax": True
            })

        return {
            "motion_plan": motion_plan
        }
