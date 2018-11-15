# takes in user input, and checks to see if it is a valid choice.  Returns int representation of choice
def isValid(input):
    if input == "Salmonella enterica":
        return 1
    elif input == "Bacillus cereus":
        return 2
    elif input == "Listeria":
        return 3
    elif input == "Brochothrix thermosphacta":
        return 4
    elif input == "None":
        return 0
    else:
        return -1


def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def dataFilter():
    selection = -1
    filters = [0, -1, -1]  # array to hold filers, 0 - name filter, 1 - lower bound, 2 - upper bound

    while selection == -1:
        selection = isValid(input("Enter the type of Bacteria you would like to filter:"))
        if selection == -1: print("Invalid Input, Please Try Again")

    filters[0] = selection

    selection = "scooby doo"

    while not isNumber(selection) and not selection == "-1":  # lower bound
        selection = input("Enter the lower bound for the range filter (enter '-1' value if you don't wish to filter):")
        if not isNumber(selection) and selection != "-1": print("Please Input A Valid Integer")

    filters[1] = float(selection)

    if float(selection) < 0:  # if selection is neg, then return filters
        return filters

    selection = "chocolate chip scooby snack"
    isLessThan = True

    while not isNumber(selection) or isLessThan:  # upper bound
        selection = input("Enter the upper bound for the range filter:")
        if not isNumber(selection): print("Please Input A Valid Integer")
        elif float(selection) < filters[1]: print("Upper Bound Must Be Greater Than Lower Bound")
        else: isLessThan = False

    filters[2] = float(selection)

    return filters


def filterArray(data, filtered, filter):  # takes in data and filter arrays, and returns filtered array

    filtered = data.copy()

    if filter[0] > 0:  # if has item to filter
        filtered = filtered[filter[0] != filtered[:, 2]]

    if filter[1] >= 0:
        filtered = filtered[filter[1] <= filtered[:, 1]]
        filtered = filtered[filter[2] >= filtered[:, 1]]

    return filtered