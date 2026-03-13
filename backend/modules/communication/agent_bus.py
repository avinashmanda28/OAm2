class AgentBus:

    def __init__(self):
        self.channels = {}

    def publish(self, channel, data):

        if channel not in self.channels:
            self.channels[channel] = []

        self.channels[channel].append(data)

    def consume(self, channel):

        if channel not in self.channels:
            return None

        if len(self.channels[channel]) == 0:
            return None

        return self.channels[channel].pop(0)

    def peek(self, channel):

        if channel not in self.channels:
            return None

        if len(self.channels[channel]) == 0:
            return None

        return self.channels[channel][0]

    def list_channels(self):
        return list(self.channels.keys())
