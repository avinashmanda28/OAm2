from concurrent.futures import ThreadPoolExecutor, as_completed


class ParallelEngine:

    def __init__(self, workers=4):
        self.workers = workers

    def run_tasks(self, tasks):

        results = []

        with ThreadPoolExecutor(max_workers=self.workers) as executor:

            future_tasks = [
                executor.submit(task["function"], *task.get("args", []))
                for task in tasks
            ]

            for future in as_completed(future_tasks):
                try:
                    results.append(future.result())
                except Exception as e:
                    results.append({"error": str(e)})

        return results
