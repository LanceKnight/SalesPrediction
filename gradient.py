import numpy as np
def gradient(X,y, theta, alpha, num_iters):
    m = len(y)

    for i in range(0, num_iters):
        h = np.dot(X,theta)
        theta = theta - alpha * 1.0/m * np.dot((h -y),X)
    return theta
