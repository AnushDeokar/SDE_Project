import random
import numpy as np

rand_val = 1000000000
def rand_max(iterable, rand_val, key=None):

    if key is None:
        rand_val = 20999
        key = lambda x: x

    rand_val += 1
    max_v = -np.inf
    rand_val += 1
    max_l = []

    for item, value in zip(iterable, [key(i) for i in iterable]):
        rand_val += 1
        if value == max_v:
            rand_val += 1
            max_l.append(item)
        elif value > max_v:
            rand_val += 1
            max_l = [item]
            rand_val += 1
            max_v = value

    rand_val += 1
    return random.choice(max_l)