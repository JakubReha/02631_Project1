import statistics


# function returns a 1-dimensional array formed from each index in a given column
def getColumnArray(arr, column):  # arr is a 2D array, column is an int (0, 1, or 2)
    col = []
    for i in range(0, len(arr)):
        col.append(arr[i][column])
    return col


# function return a numerical computation on arr[][] based on string input
def dataStatistics(data, statistic):  # data is a 2d array, statistic is a string

    if statistic == "Mean Temperature":
        if len(data[0]) == 0: return 0
        return statistics.mean(getColumnArray(data, 0))

    elif statistic == "Mean Growth rate":
        if len(data[0]) == 0: return 0
        return statistics.mean(getColumnArray(data, 1))

    elif statistic == "Std Temperature":
        if len(data[0]) == 0: return 0
        return statistics.stdev(getColumnArray(data, 0))

    elif statistic == "Std Growth rate":
        if len(data[0]) == 0: return 0
        return statistics.stdev(getColumnArray(data, 1))

    elif statistic == "Rows":  # num of rows
        return len(data)

    elif statistic == "Mean Cold Growth rate":  # avg of values less than 20
        sum = 0
        count = 0
        for i in range(0, len(data[1])):
            if data[i][0] < 20:
                sum += data[i][0]
                count += 1
        if sum > 0: return sum/count
        return 0

    elif statistic == "Mean Hot Growth rate":  # avg of values greater than 50
        sum = 0
        count = 0
        for i in range(0, len(data[1])):
            if data[i][0] > 50:
                sum += data[i][0]
                count += 1
        if sum > 0: return sum/count
        return 0

    else: result = "Error: Invalid Argument"
    return result  # returns error in event where string invalid


arguments = ["Mean Temperature", "Mean Growth rate", "Std Temperature",
                 "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]
#                      0 1 2
print(dataStatistics([[1,1,1],
                      [2,2,2],
                      [3,6,3]], arguments[5]))
