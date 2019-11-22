import random

from agents.monte_carlo import MonteCarlo


class MonteCarloES(MonteCarlo):
    """
    Monte Carlo ES (Exploring Starts)
    """

    def __init__(self):
        super().__init__()

    def policy(self, state):
        return self.pi[state]

    def run_episode(self):
        self.env.deal_dealer()

        # random first state and action
        self.env.sum_player = random.randint(12, 21)
        self.env.usable_ace_player = random.choice([False, True])

        state, action = self.env.get_state(), random.randint(0, 1)
        visited = [(state, action)]
        if visited[-1][1] == 0:
            self.env.stick()
        else:
            self.env.hit()

        while not self.env.is_end():
            state, action = self.step()
            visited.append((state, action))

        self.update_states(visited)
