import os


class VoiceGenerator:

    def __init__(self):

        self.output_folder = "backend/temp/audio"

        os.makedirs(self.output_folder, exist_ok=True)

    def generate_voice(self, scene_data):

        scenes = scene_data["scenes"]

        audio_files = []

        for scene in scenes:

            scene_id = scene["scene_id"]

            filename = f"{self.output_folder}/scene_{scene_id}.txt"

            # placeholder for voice (later will be real TTS)
            with open(filename, "w") as f:
                f.write(scene["narration"])

            audio_files.append({
                "scene_id": scene_id,
                "audio_file": filename
            })

        return {
            "audio_tracks": audio_files
        }
