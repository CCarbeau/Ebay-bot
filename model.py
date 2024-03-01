import numpy as np

def buyNowModel(x):
    percent = np.log(x)/(6+x/2000)-x/10000
    return percent