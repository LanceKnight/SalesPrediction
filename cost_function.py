import numpy as np
import h_function
def cost(X,y, theta):
    m = len(y)
    h = h_function.h(X,theta)
    return 2.0/m*sum((np.square(h-y)))