import numpy as np
from pathlib import Path
def dataLoad(filename):
    bacteria=np.array([1,2,3,4])

    if not Path(filename).is_file():
        print("Error: Invalid File Name/Path!")
        return np.zeros((2, 3))

    f = open(filename)
    # zero matrix to which we will append particular lines of data
    data=np.zeros((2,3))
    i=0
    for line in f.readlines():
        i = i+1
        elements = np.array(line.split()).astype(np.float)
        if elements[0]<10:
            print("Error: The temperature is lower than 10°C in line number",i)
        elif elements[0]>60:
            print("Error: The temperature is higher than 60°C in line number",i)
        elif elements[1]<0:
            print("Error: The growth rate is not a positive number in line number",i)
        elif np.isin(elements[2],bacteria) == False:
            print("Error: The desired bacteria does not match the database in line number",i)  
        else:
            data=np.vstack((data,elements))
    if data.shape[0]==2:
        print(("Error: No input fullfils given parameters ",i))
    else:
        # deleting the zero matrix from the beginning
        data = data[2:data.shape[0],:]
    f.close()
    return data
