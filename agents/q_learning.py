from agents.td_agent import TDAgent


class QLearning(TDAgent):
    """
    Q-learning (off-policy TD control)
    """

    def __init__(self):
        super().__init__()
        self.epsilon = 0.05
        self.alpha = 0.001
        self.gamma = 0.99

    def update(self, state, action, next_state, reward):
        q_next_max_value = max(self.q[(next_state, 0)], self.q[(next_state, 1)]) \
            if next_state is not None else 0

        self.update_state(state, action, q_next_max_value, reward)

    def run_episode(self):
        self.env.deal_dealer()
        self.env.deal_player()

        while not self.env.is_end():
            state, action = self.step()
            next_state = self.env.get_state() if not self.env.is_end() \
                else None
            reward = 0 if next_state else self.env.get_reward()
            self.update(state, action, next_state, reward)
