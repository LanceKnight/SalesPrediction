import numpy as np

def getX_y():
    file_dir = "data/Processed Data.csv"
    y = np.array([])
    X = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #get data and put them into X, y respectively
    count = 0
    with open(file_dir,"r+") as file:
        file.readline()
        for line in file:
            count +=1
            #print line
            contents = line.split(",")
            numbers = contents[2].split("\n")
            number = float(numbers[0])
            y = np.append(y,number)
    X = np.array(range(1,count+1))

    return X,y