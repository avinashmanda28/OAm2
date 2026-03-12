class SelfHealingSystem:

    def __init__(self):
        self.module_status = {}

    def monitor_module(self, module_name, status):

        self.module_status[module_name] = status

        return {
            "module": module_name,
            "status": status
        }

    def check_system_health(self):

        failed_modules = []

        for module, status in self.module_status.items():

            if status != "ok":
                failed_modules.append(module)

        return {
            "failed_modules": failed_modules,
            "system_status": "healthy" if not failed_modules else "degraded"
        }

    def repair_module(self, module_name):

        return {
            "module": module_name,
            "action": "restart_attempted"
        }
