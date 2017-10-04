import numpy as np
import h_function
from cost_function import cost
from matplotlib import pyplot as plt


def gradient(X,y, theta, alpha, num_iters):
    m = len(y)
    cost_list = np.array([])
    for i in range(0, num_iters):
        cost_list= np.append(cost_list, cost(X,y,theta))
        h = h_function.h(X, theta)
        #print "shape(h-y):", np.shape(h-y)
        #print "shape(X):", np.shape(X)
        #print "shape(np.dot((h-y),X)):", np.shape(np.dot((h-y),X))
        theta = theta - alpha * 1.0/m * np.dot((h -y),X)
    print "shape(range(0, num_iters)):", np.shape(range(0, num_iters))
    print "shape(cost_list):", np.shape(cost_list)
    plt.title("cost-iteration relation")
    plt.xlabel("iteration")
    plt.ylabel("cost")
    plt.plot(range(0, num_iters),cost_list, 'r-')

    return theta
