class WorkflowEngine:

    def __init__(self):

        self.workflow_rules = {
            "research_enabled": True,
            "visual_generation": True,
            "voice_generation": True,
            "editing_enabled": True
        }

    def decide_workflow(self, prompt_data):

        topic = prompt_data.get("topic", "").lower()

        workflow = self.workflow_rules.copy()

        if "quick" in topic:
            workflow["research_enabled"] = False

        if "podcast" in topic:
            workflow["visual_generation"] = False

        return workflow

    def summarize_workflow(self, workflow):

        enabled_modules = [
            key for key, value in workflow.items() if value
        ]

        return {
            "enabled_modules": enabled_modules,
            "total_enabled": len(enabled_modules)
        }
