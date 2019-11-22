import random
from abc import abstractmethod

from constants import states, optimal_hit_states
from environment import Environment


class Agent:
    """
    0 - stick
    1 - hit
    """

    @abstractmethod
    def init_pi(self):
        pass

    @abstractmethod
    def init_q(self):
        pass

    def __init__(self):
        self.epsilon = 0.05
        self.env = Environment()

        self.pi = dict()  # policy
        self.init_pi()

        self.q = dict()  # approximate state-action value
        self.init_q()

    def diff_optimal(self, step):
        distance = 0
        for state in states:
            if self.pi[state] == 1 and state not in optimal_hit_states:
                distance += 1
            if self.pi[state] == 0 and state in optimal_hit_states:
                distance += 1
        print(f'After {step} episodes distance from optimal policy {distance}.')

    def policy(self, state):
        action = self.pi[state]
        if random.choices((False, True),
                          weights=(1 - self.epsilon, self.epsilon))[0]:
            action = (action + 1) % 2
        return action

    def step(self):
        current_state = self.env.get_state()
        action = self.policy(current_state)
        if action == 0:
            self.env.stick()
        else:
            self.env.hit()
        return current_state, action

    @abstractmethod
    def run_episode(self):
        pass

    def train(self):
        episodes = 35000000
        for i in range(episodes):
            if i % 100000 == 0:
                self.diff_optimal(i)

            self.run_episode()
            self.env = Environment()
