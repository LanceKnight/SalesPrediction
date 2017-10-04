import numpy as np

def getX_y():
    file_dir = "data/Processed Data2.csv"
    y = np.array([])
    x1 = np.array([])
    x2 = np.array([])
    X = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #get data and put them into X, y respectively
    count = 0
    with open(file_dir,"r+") as file:
        file.readline()
        for line in file:
            count +=1
            #print line
            contents = line.split(",")
            input1 = float(contents[0])
            input2 = float(contents[1])
            #outputs = contents[2].split("\n")
            output = float(contents[2])
            x1 = np.append(x1, input1)
            x2 = np.append(x2, input2)
            y = np.append(y,output)
    #X = np.array(range(1,count+1))

    return x1,x2,y