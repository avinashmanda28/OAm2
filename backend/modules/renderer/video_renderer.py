import os
import subprocess

class VideoRenderer:

    def __init__(self):
        os.makedirs("backend/output/videos", exist_ok=True)

    def render(self, images, voice=None):

        output_file = "backend/output/videos/final_video.mp4"

        if not images:
            return {"error": "no images provided"}

        # For now we only use the first image
        image_path = images[0]["image_file"]

        cmd = [
            "ffmpeg",
            "-y",
            "-loop", "1",
            "-i", image_path,
            "-t", "5",
            "-vf", "zoompan=z='min(zoom+0.0015,1.5)':d=125",
            "-pix_fmt", "yuv420p",
            output_file
        ]

        subprocess.run(cmd)

        return {
            "video_file": output_file
        }
