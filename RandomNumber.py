import random

def randomInt(low, high, zero = False):
    i = random.randrange(low, high + 1)
    return i if i != 0 or zero else randomInt(low, high, zero)