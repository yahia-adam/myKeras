from random import random

def myRandom_initializer(n_units, n_inputs):
    weights = [[random() for _ in range(n_units)] for _ in range(n_inputs)]
    bias = [random() for _ in range(n_units)]
    return weights, bias