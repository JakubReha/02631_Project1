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


def dataFilter():
    selection = -1
    filters = [0, -1, -1]  # array to hold filers, 0 - name filter, 1 - lower bound, 2 - upper bound

    while (selection == -1):
        selection = isValid(input("Enter the type of Bacteria you would like to filter:"))
        if (selection == -1): print("Invalid Input, Please Try Again")

    filters[0] = selection

    selection = "scooby doo"

    while not isinstance(selection, int):
        selection = input(
            "Enter the lower bound for the range filter (enter a negative value if you don't wish to filter):")
    if not isinstance(selection, int): print("Please Input A Valid Integer")

    filters[1] = selection

    if (selection < 0):  # if selection is neg, then return filters
        return filters

    selection = "chocolate chip"

    while (selection < filters[1] or not isinstance(selection, int)):
        selection = input("Enter the upper bound for the range filter:")
    if not isinstance(selection, int):
        print("Please Input A Valid Integer")
    elif selection < filters[1]:
        print("Upper Bound Must Be Greater Than Lower Bound")


    filters[2] = selection

    return filters
