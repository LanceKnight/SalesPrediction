import numpy as np
def cost(X,y, theta):
    m = len(y)
    h = np.dot(X,theta)
    return 2.0/m*sum((np.square(h-y)))