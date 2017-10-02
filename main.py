import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt

from initialization import getX_y
from cost_function import cost
from gradient import gradient

alpha = 0.01
num_iters = 1500
theta = np.array([0.1, 0.2])
test = np.array([0.3, 0.4])



#get X, y as numpy array
(X,y) = getX_y()


print "cost before:", cost(X,y,theta)
theta = gradient(X,y, theta, alpha, num_iters)
print "cost after:", cost(X,y, theta)
print "theta:", theta
h = np.dot(X,theta)

t = np.array([1,2,3])
s = np.array([4,5,6])
print "X:",X[:,1]
plt.plot(X[:,1],y,'ro')
plt.plot(X[:,1],h,'b')
plt.show()