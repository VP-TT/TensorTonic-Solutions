import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    mse=0;
    for i in range(len(y_pred)):
        mse+=((y_pred[i]-y_true[i])**2)
    # Write code here
    return mse/len(y_true)
    pass
