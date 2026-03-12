import os


class SceneComposer:

    def __init__(self):

        self.output_folder = "backend/temp/scenes"

        os.makedirs(self.output_folder, exist_ok=True)

    def compose_scenes(self, image_data, voice_data):

        images = image_data["images"]
        voices = voice_data["audio_tracks"]

        scenes = []

        for img, voice in zip(images, voices):

            scene_id = img["scene_id"]

            filename = f"{self.output_folder}/scene_{scene_id}.txt"

            # placeholder scene file
            with open(filename, "w") as f:

                f.write(f"Scene {scene_id}\n")
                f.write(f"Image: {img['image_file']}\n")
                f.write(f"Audio: {voice['audio_file']}\n")

            scenes.append({
                "scene_id": scene_id,
                "scene_file": filename
            })

        return {
            "scene_videos": scenes
              }
