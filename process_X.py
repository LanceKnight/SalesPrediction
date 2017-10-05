import numpy as np

#add x0 and x1,x2 ... to the power of i as needed

def process_X(x1, x2):

    x0 = np.ones(np.size(x1))
    x1 = x1
    x2 = x2#np.square(X)
    x3 = np.power(x1,2)
    x4 = np.power(x2, 2)
    x5 = np.power(x1,3)
    #X = np.vstack([np.hstack(x0),np.hstack(x1)]).transpose() # for x to the power of 1
    #X =  np.vstack([np.hstack(x0),np.hstack(x1),np.hstack(x2)]).transpose()
    #X = np.vstack([np.hstack(x0), np.hstack(x1), np.hstack(x2), np.hstack(x3)]).transpose()
    X = np.vstack([np.hstack(x0), np.hstack(x1), np.hstack(x2), np.hstack(x3),np.hstack(x4), np.hstack(x5)]).transpose()
    return X
