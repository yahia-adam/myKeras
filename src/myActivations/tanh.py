from math import exp

def myTanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def myTanh_prime(x):
    t = myTanh(x)
    return 1 - t*t