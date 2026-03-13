class SoundEngine:

    def __init__(self):

        self.sound_library = {
            "intro": "intro_impact",
            "transition": "whoosh",
            "highlight": "digital_ping",
            "ending": "cinematic_hit"
        }

    def assign_sounds(self, scenes):

        sound_scenes = []

        for i, scene in enumerate(scenes):

            if i == 0:
                sound = self.sound_library["intro"]

            elif i == len(scenes) - 1:
                sound = self.sound_library["ending"]

            else:
                sound = self.sound_library["transition"]

            sound_scenes.append({
                "scene": scene,
                "sound_effect": sound
            })

        return sound_scenes
