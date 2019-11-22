import argparse

from agents.monte_carlo_es import MonteCarloES
from agents.on_policy_first_visit_mc_control import OnPolicyFirstVisitMCControl
from agents.q_learning import QLearning
from agents.sarsa import Sarsa


def parse_args():
    """
    Parse arguments from command line input
    """
    parser = argparse.ArgumentParser(description='Learning parameters')
    parser.add_argument('--agent', type=str, default='monte_carlo_es',
                        help='The agent among monte_carlo_es, '
                             'on_policy_first_visit_mc_control, '
                             'q_learning, sarsa.',
                        choices=['monte_carlo_es',
                                 'on_policy_first_visit_mc_control',
                                 'q_learning',
                                 'sarsa'])
    args, unknown = parser.parse_known_args()
    return args


def main():
    # Parse arguments
    args = parse_args()

    # Select the agent to train
    if args.agent == 'monte_carlo_es':
        agent = MonteCarloES()
    elif args.agent == 'on_policy_first_visit_mc_control':
        agent = OnPolicyFirstVisitMCControl()
    elif args.agent == 'q_learning':
        agent = QLearning()
    elif args.agent == 'sarsa':
        agent = Sarsa()

    agent.train()


if __name__ == '__main__':
    main()
