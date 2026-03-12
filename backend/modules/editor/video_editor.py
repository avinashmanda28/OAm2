import os


class VideoEditor:

    def __init__(self):

        self.output_folder = "backend/temp/final"

        os.makedirs(self.output_folder, exist_ok=True)

    def assemble_video(self, scene_data):

        scenes = scene_data["scene_videos"]

        final_file = f"{self.output_folder}/final_video.txt"

        with open(final_file, "w") as f:

            f.write("Final Video Timeline\n\n")

            for scene in scenes:
                f.write(f"Scene {scene['scene_id']} → {scene['scene_file']}\n")

        return {
            "final_video": final_file
        }
