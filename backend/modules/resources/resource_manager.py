import os
import psutil


class ResourceManager:

    def __init__(self):

        self.max_cpu_usage = 90
        self.max_memory_usage = 90

    def get_system_stats(self):

        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        return {
            "cpu_usage": cpu,
            "memory_usage": memory
        }

    def is_safe(self):

        stats = self.get_system_stats()

        if stats["cpu_usage"] > self.max_cpu_usage:
            return False

        if stats["memory_usage"] > self.max_memory_usage:
            return False

        return True

    def wait_for_resources(self):

        stats = self.get_system_stats()

        if not self.is_safe():

            return {
                "status": "waiting",
                "stats": stats
            }

        return {
            "status": "ready",
            "stats": stats
        }
