import os


class VideoRenderer:

    def __init__(self):

        self.output_folder = "backend/output"

        os.makedirs(self.output_folder, exist_ok=True)

    def render_video(self, editor_output):

        final_video_path = f"{self.output_folder}/video_output.txt"

        timeline = editor_output["final_video"]

        with open(final_video_path, "w") as f:

            f.write("Rendered Video\n\n")
            f.write(f"Source Timeline: {timeline}\n")

        return {
            "rendered_video": final_video_path
        }
