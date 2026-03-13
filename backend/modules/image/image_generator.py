import os

def generate_images(prompts):

    os.makedirs("backend/temp/images", exist_ok=True)

    images = []

    for i, prompt in enumerate(prompts):

        path = f"backend/temp/images/scene_{i}.png"

        # placeholder generation
        with open(path, "w") as f:
            f.write(prompt)

        images.append({
            "scene_id": i,
            "image_file": path
        })

    return images
