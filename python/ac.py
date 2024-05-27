# percept is a list of size 2 where the first element is the current temperature and the second element is a Boolean indicating if the AC is on (true = AC on, and false = AC off)

class SimpleACReflexAgent(object):

    def __init__(self, min_threshold, max_threshold):
        self.min_threshold = min_threshold  # defining the min threshold
        self.max_threshold = max_threshold  # defining the max threshold

    def select_action(self, precept):
        if bool(precept[1]) is False:
            if precept[0] <= self.min_threshold:
                return "TurnOn"
        if bool(precept[1]) is True:
            if precept[0] >= self.max_threshold:
                return "TurnOff"

        return None


class SimpleACEnvironment(object):

    def __init__(self, ac_agent, starting_temp=28):
        self.ac_agent = ac_agent
        self.temperature = starting_temp
        self.num_agent_actions = 0
        self.is_ac_on = False

    def tick(self):
        UsedAc = [self.temperature, self.is_ac_on]
        ac = self.ac_agent.select_action(UsedAc)
        if ac == "TurnOn":
            self.is_ac_on = True
            self.num_agent_actions = self.num_agent_actions + 1

        if ac == "TurnOff":
            self.is_ac_on = False
            self.num_agent_actions = self.num_agent_actions + 1

        if self.is_ac_on is True:
            self.temperature = self.temperature + 1
        if self.is_ac_on is False:
            self.temperature = self.temperature - 1

        return

    def simulate(self, num_timesteps):
        for _ in range(num_timesteps):
            self.tick()