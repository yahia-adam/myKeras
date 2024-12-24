
def myConstant_initializer(n_units, n_inputs, constant):
    weights = [[constant for _ in range(n_units)] for _ in range(n_inputs)]
    bias = [constant for _ in range(n_units)]
    return weights, bias

def myZeros_initializer(n_units, n_inputs):
    return myConstant_initializer(n_units, n_inputs, 0)

def myOnes_initializer(n_units, n_inputs):
    return myConstant_initializer(n_units, n_inputs, 1)