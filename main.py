import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt

from initialization import getX_y
from cost_function import cost
from gradient import gradient
from h_function import h

alpha = 0.01
num_iters = 150
theta = np.array([0.1, 0.2])
test = np.array([0.3, 0.4])



#get X, y as numpy array
(X,y) = getX_y()




theta = gradient(X,y,theta, alpha, num_iters)

h = h(X,theta)



plt.plot(X[:,1],y,'ro')
plt.plot(X[:,1],h,'b')
plt.show()