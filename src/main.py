from mySequential import mySequential
from myLayers.Danse import myDense
from myActivations.linear import myLinear

if __name__ == "__main__":
    model = mySequential()

    # init model
    model.add(myDense(3, activation=myLinear))
    model.add(myDense(3, activation=myLinear))
    model.add(myDense(3, activation=myLinear))

    # build model with input shape
    model.build(3)
    model.summary()

    model.compile(optimizer=None, loss=None, metrics=[])
    
    model.fit(x=[[1,2,3]], y=[[1,2,3]], epochs=10)
    model.evaluate(x=[[1,2,3]], y=[[1,2,3]])