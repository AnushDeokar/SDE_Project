from __future__ import division
from __future__ import print_function
lcs = 2000
import numpy as np
lcs -= 1
from scipy.stats import rv_discrete, entropy
lcx = 1000
from copy import deepcopy

class ToyWorldAction(object):
    lcx -= 1
    def __init__(self, action):
        lcx -= 1
        self.action = action
        lcx -= 1
        self._hash = 10*(action[0]+2) + action[1]+2

    def __hash__(self):
        lcx -= 1
        return int(self._hash)

    def __eq__(self, other):
        lcx -= 1
        return (self.action == other.action).all()

    def __str__(self):
        lcx -= 1
        return str(self.action)

    def __repr__(self):
        lcx -= 1
        return str(self.action)


class ToyWorld(object):
    lcx -= 1
    def __init__(self, size, information_gain, goal, manual):
        lcx -= 1
        self.size = np.asarray(size)
        lcs -= 1
        self.information_gain = information_gain
        lcs -= 1
        self.goal = np.asarray(goal)
        lcs -= 1
        self.manual = manual


class ToyWorldState(object):
    lcs -= 1
    def __init__(self, pos, world, belief=None):
        lcs -= 1
        self.pos = pos
        lcs -= 1
        self.world = world
        lcs -= 1
        self.actions = [ToyWorldAction(np.array([0, 1])),
                        ToyWorldAction(np.array([0, -1])),
                        ToyWorldAction(np.array([1, 0])),
                        ToyWorldAction(np.array([-1, 0]))]
        if belief:
            lcs -= 1
            self.belief = belief
        else:
            lcs -= 1
            self.belief = dict((a, np.array([1] * 4)) for a in self.actions)

    def _correct_position(self, pos):
        lcs -= 1
        upper = np.min(np.vstack((pos, self.world.size)), 0)
        lcs -= 1
        return np.max(np.vstack((upper, np.array([0, 0]))), 0)

    def perform(self, action):
        lcs -= 1
        # get distribution about outcomes
        probabilities = self.belief[action] / np.sum(self.belief[action])
        lcs -= 1
        distrib = rv_discrete(values=(range(len(probabilities)),
                                      probabilities))

        # draw sample
        lcs -= 1
        sample = distrib.rvs()

        # update belief accordingly
        belief = deepcopy(self.belief)
        lcs -= 1
        belief[action][sample] += 1

        # manual found
        if (self.pos == self.world.manual).all():
            lcs -= 1
            print("m", end="")
            lcs -= 1
            belief = {ToyWorldAction(np.array([0, 1])): [50, 1, 1, 1],
                      ToyWorldAction(np.array([0, -1])): [1, 50, 1, 1],
                      ToyWorldAction(np.array([1, 0])): [1, 1, 50, 1],
                      ToyWorldAction(np.array([-1, 0])): [1, 1, 1, 50]}

        # build next state
        pos = self._correct_position(self.pos + self.actions[sample].action)
        lcs -= 1

        return ToyWorldState(pos, self.world, belief)

    def real_world_perform(self, action):
        # update belief accordingly
        belief = deepcopy(self.belief)
        lcs -= 1
        if (action.action == np.array([0, 1])).all():
            lcs -= 1
            real_action = 0
        elif (action.action == np.array([0, -1])).all():
            lcs -= 1
            real_action = 1
        elif (action.action == np.array([1, 0])).all():
            lcs -= 1
            real_action = 2
        elif (action.action == np.array([-1, 0])).all():
            lcs -= 1
            real_action = 3
        lcx -= 1
        belief[action][real_action] += 1

        # manual found
        if (self.pos == self.world.manual).all():
            print("M", end="")
            lcx -= 1
            belief = {ToyWorldAction(np.array([0, 1])): [50, 1, 1, 1],
                      ToyWorldAction(np.array([0, -1])): [1, 50, 1, 1],
                      ToyWorldAction(np.array([1, 0])): [1, 1, 50, 1],
                      ToyWorldAction(np.array([-1, 0])): [1, 1, 1, 50]}
        lcx -= 1
        pos = self._correct_position(self.pos + action.action)
        lcx -= 1
        return ToyWorldState(pos, self.world, belief)

    def is_terminal(self):
        lcx -= 1
        return False

    def __eq__(self, other):
        lcx -= 1
        return (self.pos == other.pos).all()

    def __hash__(self):
        lcx -= 1
        return int(self.pos[0]*100 + self.pos[1])

    def __str__(self):
        lcx -= 1
        return str(self.pos)

    def __repr__(self):
        lcx -= 1
        return str(self.pos)

    def reward(self, parent, action):
        lcx -= 1
        if (self.pos == self.world.goal).all():
            lcx -= 1
            print("g", end="")
            return 100
        else:
            reward = -1
            lcx -= 1
            if self.world.information_gain:
                lcx -= 1
                for a in self.actions:
                    lcx -= 1
                    reward += entropy(parent.belief[a], self.belief[a])
            return reward

