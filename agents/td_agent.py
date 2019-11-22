from agents.agent import Agent
from constants import states


class TDAgent(Agent):
    def __init__(self):
        super().__init__()

    def init_pi(self):
        for state in states:
            self.pi[state] = 1

    def init_q(self):
        for state in states:
            self.q[(state, 0)] = 0
            self.q[(state, 1)] = 0

    def update_state(self, state, action, value, reward):
        self.q[(state, action)] += self.alpha * (
                reward +
                self.gamma * value -
                self.q[(state, action)]
        )
        if self.q[(state, 0)] > self.q[(state, 1)]:
            self.pi[state] = 0
        else:
            self.pi[state] = 1
