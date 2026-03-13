class AgentMarketplace:

    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):

        self.agents[name] = agent

    def get_agent(self, name):

        if name in self.agents:
            return self.agents[name]

        return None

    def list_agents(self):

        return list(self.agents.keys())

    def remove_agent(self, name):

        if name in self.agents:
            del self.agents[name]
