class CollaborationEngine:

    def __init__(self):

        self.agents = {}

    def register_agent(self, name, agent):

        self.agents[name] = agent

    def list_agents(self):

        return list(self.agents.keys())

    def execute_pipeline(self, pipeline, data):

        current_data = data

        for step in pipeline:

            agent = self.agents.get(step)

            if agent is None:
                continue

            if hasattr(agent, "process"):
                current_data = agent.process(current_data)

        return current_data
