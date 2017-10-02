import numpy as np
import h_function
def gradient(X,y, theta, alpha, num_iters):
    m = len(y)

    for i in range(0, num_iters):
        h = h_function.h(X, theta)
        theta = theta - alpha * 1.0/m * np.dot((h -y),X)
    return theta
