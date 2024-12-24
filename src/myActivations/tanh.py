from math import exp

def myTanh(x):
    return 1 - (2 / (1 + exp(2*x)))