class HookDetector:

    def __init__(self):
        pass

    def detect_hook(self, script_data):

        sections = script_data["script"]

        hook_line = sections[0]["text"]

        return {
            "detected_hook": hook_line
        }
