class ContextEngine:

    def __init__(self):

        self.context_memory = {}

    def update_context(self, key, value):

        self.context_memory[key] = value

    def get_context(self, key):

        return self.context_memory.get(key, None)

    def clear_context(self):

        self.context_memory = {}
