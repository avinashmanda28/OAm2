import os

def generate_voice(script):

    os.makedirs("backend/temp/audio", exist_ok=True)

    tracks = []

    for i, scene in enumerate(script):

        path = f"backend/temp/audio/scene_{i}.wav"

        with open(path, "w") as f:
            f.write(scene["text"])

        tracks.append({
            "scene_id": i,
            "audio_file": path
        })

    return tracks
