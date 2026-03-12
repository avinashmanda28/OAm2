import os


class CaptionGenerator:

    def __init__(self):

        self.output_folder = "backend/temp/captions"

        os.makedirs(self.output_folder, exist_ok=True)

    def generate_captions(self, script_data):

        sections = script_data["script"]

        captions = []

        for i, section in enumerate(sections, start=1):

            filename = f"{self.output_folder}/scene_{i}.srt"

            with open(filename, "w") as f:

                f.write("1\n")
                f.write("00:00:00,000 --> 00:00:05,000\n")
                f.write(section["text"])

            captions.append({
                "scene_id": i,
                "caption_file": filename
            })

        return {
            "captions": captions
        }
