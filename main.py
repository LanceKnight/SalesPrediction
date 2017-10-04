import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt

from initialization import getX_y
from gradient import gradient
from h_function import h
from process_X import process_X
from cost_function import cost


alpha = 0.0000001
num_iters = 150000
theta = np.array([0.1, 0.2,0.3, 0.4])


#get X, y as numpy array
(X,y) = getX_y()
X = process_X(X)
# print "shape(X):", np.shape(X)
# print "shape(theta):", np.shape(theta)
# print h(X,theta)
print "Cost before:", cost(X, y, theta)

theta = gradient(X,y,theta, alpha, num_iters)

print "Cost after:", cost(X, y, theta)
h = h(X,theta)


print "X:", X
print "Theta:", theta
plt.plot(X[:,1],y,'ro')
plt.plot(X[:,1],h,'b')
plt.show()