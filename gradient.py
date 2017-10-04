import numpy as np
import h_function
from cost_function import cost

def gradient(X,y, theta, alpha, num_iters):
    m = len(y)

    for i in range(0, num_iters):

        h = h_function.h(X, theta)
        #print "shape(h-y):", np.shape(h-y)
        #print "shape(X):", np.shape(X)
        #print "shape(np.dot((h-y),X)):", np.shape(np.dot((h-y),X))
        theta = theta - alpha * 1.0/m * np.dot((h -y),X)
    return theta
