class AgentSupervisor:

    def __init__(self):

        self.agent_status = {}

    def register_agent(self, name):

        self.agent_status[name] = "running"

        return {
            "registered_agent": name
        }

    def report_failure(self, name):

        self.agent_status[name] = "failed"

        return {
            "failed_agent": name
        }

    def restart_agent(self, name):

        if name in self.agent_status:

            self.agent_status[name] = "running"

            return {
                "restarted_agent": name
            }

        return {
            "error": "agent_not_found"
        }

    def get_status(self):

        return {
            "agents": self.agent_status
          }
