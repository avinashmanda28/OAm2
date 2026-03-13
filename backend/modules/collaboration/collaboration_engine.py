class CollaborationEngine:

    def __init__(self):

        self.shared_context = {}

    def share_data(self, agent_name, data):

        self.shared_context[agent_name] = data

    def get_shared_data(self):

        return self.shared_context

    def summarize_collaboration(self):

        agents = list(self.shared_context.keys())

        return {
            "active_agents": agents,
            "total_agents": len(agents)
        }
