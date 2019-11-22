from agents.agent import Agent
from constants import states


class MonteCarlo(Agent):
    def __init__(self):
        super().__init__()

    def init_pi(self):
        for state in states:
            self.pi[state] = 0

    def init_q(self):
        for state in states:
            self.q[(state, 0)] = (0.0, 0)  # average, count
            self.q[(state, 1)] = (0.0, 0)

    def update_states(self, visited):
        reward = self.env.get_reward()
        changed = set()
        for state, action in visited:
            if (state, action) not in changed:
                changed.add((state, action))
                average, count = self.q[(state, action)]
                self.q[(state, action)] = (
                    (average * count + reward) / (count + 1),
                    count + 1
                )

                if self.q[(state, 0)][0] > self.q[(state, 1)][0]:
                    self.pi[state] = 0
                else:
                    self.pi[state] = 1
