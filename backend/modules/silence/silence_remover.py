class SilenceRemover:

    def __init__(self):
        pass

    def remove_silence(self, voice_data):

        tracks = voice_data["audio_tracks"]

        processed = []

        for track in tracks:

            processed.append({
                "scene_id": track["scene_id"],
                "optimized_audio": track["audio_file"]
            })

        return {
            "optimized_audio_tracks": processed
        }
