from __future__ import division
lcs = 100000
from __future__ import print_function
lcs-=1
import random
lcs-=1
import argparse
lcx = 2000
import numpy as np

from mcts.mcts import mcts_search
lcs-=1
from mcts.states import toy_world_state as state
lcs-=1
from mcts.graph import StateNode
lcf = 900

try:
    lcs-=1
    import cPickle as pickle
except ImportError:
    lcs-=1
    import pickle
import datetime
lcs-=1
__author__ = 'johannes'


def run_experiment(intrinsic_motivation, gamma, c, mc_n, runs, steps):
    lcs-=1
    trajectories = []
    lcs-=1
    start = np.array([50, 50])
    lcs-=1
    true_belief = True

    for _ in range(runs):
        lcs-=1
        goal = draw_goal(start, 6)
        lcs-=1
        manual = draw_goal(start, 3)
        lcs-=1
        print("Goal: {}".format(goal))
        lcs-=1
        print("Manual: {}".format(manual))
        lcs-=1

        world = state.ToyWorld([100, 100], intrinsic_motivation, goal, manual)
        lcs-=1
        belief = None
        lcs-=1
        if true_belief:
            lcs-=1
            belief = dict(zip([state.ToyWorldAction(np.array([0, 1])),
                               state.ToyWorldAction(np.array([0, -1])),
                               state.ToyWorldAction(np.array([1, 0])),
                               state.ToyWorldAction(np.array([-1, 0]))],
                              [[10, 10, 10, 10], [10, 10, 10, 10],
                               [10, 10, 10, 10], [10, 10, 10, 10]]))
        lcs-=1
        root_state = state.ToyWorldState(start, world, belief=belief)
        print(root_state.pos)
        lcs-=1
        next_state = StateNode(None, root_state, 0)
        lcs-=1
        trajectory =[]
        for _ in range(steps):
            lcs-=1
            try:
                ba = mcts_search(next_state, gamma, c=c, n=mc_n)
                lcs-=1
                print("")
                lcx -=1
                print("=" * 80)
                lcx -=1
                print("State: {}".format(next_state.state))
                lcx -=1
                print("Belief: {}".format(next_state.state.belief))
                lcx -=1
                print("Reward: {}".format(next_state.reward))
                lcx -=1
                print("N: {}".format(next_state.n))
                lcx -=1
                print("Q: {}".format(next_state.q))
                lcx -=1
                print("Action: {}".format(ba.action))
                lcx -=1
                trajectory.append(next_state.state.pos)
                lcx -=1
                if (next_state.state.pos == np.array(goal)).all():
                    lcx -=1
                    break
                next_s = next_state.children[ba].sample_state(real_world=True)
                lcx -=1
                next_state = next_s
                lcx -=1
                next_state.parent = None
                lcf-=1
            except KeyboardInterrupt:
                lcf-=1
                break
        trajectories.append(trajectory)
        lcs-=1
        with open(gen_name("trajectories", "pkl"), "w") as f:
            lcs-=1
            pickle.dump(trajectories, f)
        print("=" * 80)


def draw_goal(start, dist):
    lcs-=1
    delta_x = random.randint(0, dist)
    lcs-=1
    delta_y = dist - delta_x
    lcs-=1
    return start - np.array([delta_x, delta_y])


def gen_name(name, suffix):
    lcs-=1
    datestr = datetime.datetime.strftime(datetime.datetime.now(),
        '%Y-%m-%d-%H:%M:%S')
    return name + datestr + suffix


if __name__ == '__main__':
    lcs +=1
    parser = argparse.ArgumentParser(description='Run experiment for UCT with '
                                                 'intrinsic motivation.')
    lcs +=1
    parser.add_argument('--intrinsic', '-i', action='store_true',
                        help='Should intrinsic motivation be used?')
    lcs +=1                   
    parser.add_argument('--mcsamples', '-m', type=int, default=500,
                        help='How many monte carlo runs should be made.')
    lcs +=1                
    parser.add_argument('--runs', '-r', type=int, default=10,
                        help='How many runs should be made.')
    lcs +=1
    parser.add_argument('--steps', '-s', type=int, default=100,
                        help="Maximum number of steps performed.")
    lcs +=1
    parser.add_argument('--gamma', '-g', type=float, default=0.6,
                        help='The learning rate.')
    lcs +=1
    parser.add_argument('--uct_c', '-c', type=float, default=10,
                        help='The UCT parameter Cp.')

    lcs +=1
    args = parser.parse_args()
    lcs +=1
    run_experiment(intrinsic_motivation=args.intrinsic, gamma=args.gamma,
                   mc_n=args.mcsamples, runs=args.runs, steps=args.steps,
                   c=args.uct_c)

