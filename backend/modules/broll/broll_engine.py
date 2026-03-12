class BRollEngine:

    def __init__(self):
        pass

    def generate_broll(self, scene_data):

        scenes = scene_data["scenes"]

        broll_list = []

        for scene in scenes:

            title = scene["title"]

            broll_prompt = f"supplementary visuals related to {title}"

            broll_list.append({
                "scene_id": scene["scene_id"],
                "broll_prompt": broll_prompt
            })

        return {
            "broll": broll_list
        }
