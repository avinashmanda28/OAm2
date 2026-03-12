import threading


class TaskQueue:

    def __init__(self):

        self.tasks = []

    def add_task(self, func, *args):

        thread = threading.Thread(target=func, args=args)

        self.tasks.append(thread)

        return {
            "task_added": func.__name__
        }

    def run_all(self):

        for task in self.tasks:
            task.start()

        for task in self.tasks:
            task.join()

        return {
            "tasks_completed": len(self.tasks)
        }

    def clear_tasks(self):

        self.tasks = []

        return {
            "status": "queue_cleared"
      }
