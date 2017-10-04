import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

from initialization import getX_y
from gradient import gradient
from h_function import h
from process_X import process_X
from cost_function import cost


alpha = 0.00001
num_iters = 40000
theta = np.array([0.1, 0.2, 0.3])


#get X, y as numpy array
(x1,x2, y) = getX_y()
X = process_X(x1, x2)
# print "shape(X):", np.shape(X)
# print "shape(theta):", np.shape(theta)
# print h(X,theta)
print "Cost before:", cost(X, y, theta)

theta = gradient(X, y, theta, alpha, num_iters)

print "Cost after:", cost(X, y, theta)
h = h(X,theta)


#print "X:", X
#print "Theta:", theta
plt.figure()
plt.title("Sales Prediction")
plt.xlabel("month(from Jun, 2016 to Sept,2017)")
plt.ylabel("sales amount")
plt.plot(X[:,2],y,'ro')
plt.plot(X[:,2],h,'b')
#plt.show()

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

x1 = X[:,1]
x2 = X[:,2]
ax.plot_wireframe(x1,x2, h, rstride=10, cstride=10)
ax.scatter(x1, x2, y, label = "test", c = 'r')
ax.set_xlabel('Size')
ax.set_ylabel('Month')
ax.set_zlabel('Sales Qty(SF)')
ax.legend()

plt.show()