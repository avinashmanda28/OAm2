class VisualMemoryEngine:

    def __init__(self):
        self.memory = {}

    def store_visual(self, key, visual_data):

        self.memory[key] = visual_data

    def get_visual(self, key):

        return self.memory.get(key, None)

    def list_visuals(self):

        return list(self.memory.keys())
