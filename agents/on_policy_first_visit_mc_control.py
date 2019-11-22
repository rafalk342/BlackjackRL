from agents.monte_carlo import MonteCarlo


class OnPolicyFirstVisitMCControl(MonteCarlo):
    """
    On-policy first-visit MC control (for epsilon-soft policies)
    """

    def __init__(self):
        super().__init__()

    def run_episode(self):
        self.env.deal_dealer()
        self.env.deal_player()

        visited = []

        while not self.env.is_end():
            state, action = self.step()
            visited.append((state, action))

        self.update_states(visited)
