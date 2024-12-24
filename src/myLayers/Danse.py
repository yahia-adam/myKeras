from myActivations.linear import myLinear
from myInitializers.random_initializer import myRandom_initializer
from myMath.matrix import myMatrix_multiply

class myDense():
    def __init__(self, n_units, activation=myLinear, kernel_initializer=myRandom_initializer):
        self.n_units = n_units
        self.activation = activation
        self.kernel_initializer = kernel_initializer
        self.weights = None
        self.activations = None
        self.bias = None

    def __call__(self, inputs):
        self.activations = [sum(w,b) for w,b in zip(myMatrix_multiply([inputs], self.weights), self.bias)]
        return self.activations
    
    def build(self, n_inputs):
        self.weights, self.bias = self.kernel_initializer(self.n_units, n_inputs)
        self.activations = [0 for _ in range(self.n_units)]