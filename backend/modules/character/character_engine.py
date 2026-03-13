class CharacterEngine:

    def __init__(self):

        self.characters = {}

    def create_character(self, name, description):

        character = {
            "name": name,
            "description": description,
            "visual_style": "consistent",
            "voice_style": "natural"
        }

        self.characters[name] = character

        return character

    def get_character(self, name):

        if name in self.characters:
            return self.characters[name]

        return None

    def list_characters(self):

        return list(self.characters.keys())

    def assign_character_to_scene(self, scenes, character_name):

        character = self.get_character(character_name)

        if not character:
            return scenes

        updated_scenes = []

        for s in scenes:

            scene = s.copy()

            scene["character"] = character

            updated_scenes.append(scene)

        return updated_scenes
