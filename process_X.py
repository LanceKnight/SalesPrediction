import numpy as np

#add x0 and x1,x2 ... to the power of i as needed

def process_X(X):

    x0 = np.ones(np.size(X))
    x1 = X
    x2 = np.square(X)
    x3 = np.power(X,3)
    x4 = np.power(X, 4)
    #X = np.vstack([np.hstack(x0),np.hstack(x1)]).transpose() # for x to the power of 1
    X =  np.vstack([np.hstack(x0),np.hstack(x1),np.hstack(x2)]).transpose()
    #X = np.vstack([np.hstack(x0), np.hstack(x1), np.hstack(x2), np.hstack(x3)]).transpose()
    #X = np.vstack([np.hstack(x0), np.hstack(x1), np.hstack(x2), np.hstack(x3),np.hstack(x4)]).transpose()
    return X
