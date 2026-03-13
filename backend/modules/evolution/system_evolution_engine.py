class SystemEvolutionEngine:

    def __init__(self):

        self.evolution_log = []


    def evaluate_system(self, system_state):

        report = {
            "status": "stable",
            "recommendation": "no changes required"
        }

        if system_state.get("errors", 0) > 5:

            report["status"] = "unstable"
            report["recommendation"] = "optimize modules"

        self.evolution_log.append(report)

        return report


    def get_evolution_history(self):

        return self.evolution_log
