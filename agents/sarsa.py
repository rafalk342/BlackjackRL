from agents.td_agent import TDAgent


class Sarsa(TDAgent):
    """
    Sarsa (on-policy TD control)
    """

    def __init__(self):
        super().__init__()
        self.epsilon = 1
        self.alpha = 0.5
        self.gamma = 0.99

    def update(self, state, action, next_state, next_action, reward=0):
        q_next_value = self.q[(next_state, next_action)] \
            if next_state is not None else 0

        self.update_state(state, action, q_next_value, reward)

    def run_episode(self):
        self.epsilon = max(self.epsilon * 0.99, 0.05)
        self.alpha = max(self.alpha * 0.99, 0.001)

        self.env.deal_dealer()
        self.env.deal_player()

        state, action = self.step()

        while not self.env.is_end():
            next_state, next_action = self.step()

            self.update(state, action, next_state, next_action)

            state = next_state
            action = next_action

        self.update(state, action, None, None, self.env.get_reward())
