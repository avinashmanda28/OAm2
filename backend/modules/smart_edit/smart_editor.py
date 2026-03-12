class SmartEditor:

    def __init__(self):
        pass

    def analyze_editing(self, script_data, scene_data):

        scenes = scene_data["scenes"]

        editing_plan = []

        for scene in scenes:

            title = scene["title"].lower()

            decision = "normal"

            if "hook" in title:
                decision = "zoom_in"

            if "example" in title:
                decision = "highlight"

            editing_plan.append({
                "scene_id": scene["scene_id"],
                "edit_style": decision
            })

        return {
            "editing_plan": editing_plan
        }
