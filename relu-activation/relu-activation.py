import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    # if(len(x)==0) return x
    x=np.array(x, ndmin=1)
    # max1=0
    # if (x.ndim==1):
    #     for i in range(len(x)):
    #         x[i]=max(x[i], 0)
    #     return x
    # if (x.ndim==2):
    #     for i in range(len(x)):
    #         for j in range(len(x[0])):
    #             x[i][j]=max(x[i][j], 0)
    #     return x
    # else:
    return np.maximum(0, x)

    pass