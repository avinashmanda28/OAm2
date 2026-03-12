class OrchestratorEngine:

    def __init__(self):

        self.tasks = []

    def register_task(self, name, data=None):

        task = {
            "task_name": name,
            "data": data
        }

        self.tasks.append(task)

        return task

    def get_pipeline(self):

        return {
            "tasks": self.tasks,
            "total_tasks": len(self.tasks)
        }

    def clear_pipeline(self):

        self.tasks = []

        return {
            "status": "pipeline_cleared"
        }
