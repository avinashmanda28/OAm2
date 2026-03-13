import queue
import threading
import time


class TaskQueue:

    def __init__(self, workers=2):

        self.task_queue = queue.Queue()
        self.workers = workers
        self.active_workers = []
        self.running = True

        self.start_workers()

    def start_workers(self):

        for _ in range(self.workers):
            worker = threading.Thread(target=self.worker_loop)
            worker.daemon = True
            worker.start()
            self.active_workers.append(worker)

    def worker_loop(self):

        while self.running:

            try:
                task = self.task_queue.get(timeout=1)

                func = task["function"]
                args = task.get("args", [])

                func(*args)

                self.task_queue.task_done()

            except queue.Empty:
                time.sleep(0.1)

    def add_task(self, function, args=None):

        if args is None:
            args = []

        self.task_queue.put({
            "function": function,
            "args": args
        })

    def pending_tasks(self):

        return self.task_queue.qsize()

    def stop(self):

        self.running = False
