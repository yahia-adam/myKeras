from myLayers.Danse import myDense

class mySequential():
    def __init__(self, layers: [myDense] = [], name=None):
        optimizer = None
        loss = None
        self.layers = layers
        self.name = name
        self.isbuild = False

    def build(self, n_input):
        self.isbuild = True
        for i, layer in enumerate(self.layers):
            if i == 0:
                layer.build(n_input)
            else:
                layer.build(self.layers[i-1].units)
                
    def add(self, layer):
        self.layers.append(layer)

    def compile(self, optimizer, loss, metrics=[]):
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics
    
    def fit(self, x, y, epochs, batch_size=32):
        if (self.build == False):
            self.build(len(x[0]))
        
        for epoch in range(epochs):
            pass

    def evaluate(self, x, y):
        pass

    def predict(self, x):
        for i, layer in enumerate(self.layers):
            if i == 0:
                layer(x)
            else:
                layer(self.layers[i-1].activations)           
        return self.layers[-1].activations
    
    def summary(self):
        if self.name:
            print(self.name)
        for i, layer in enumerate(self.layers):
            if (layer.weights == None):
                print(f"Layer_{i}: w=? A={layer.activation.__name__}")
            else:
                print(f"Layer_{i}: W={len(layer.weights)}x{len(layer.weights[0])} A={layer.activation.__name__}")
