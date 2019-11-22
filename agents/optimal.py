from agents.agent import Agent
from constants import optimal_hit_states


class OptimalAgent(Agent):

    def __init__(self):
        super().__init__()

    def init_pi(self):
        for state in optimal_hit_states:
            self.pi[state] = 1