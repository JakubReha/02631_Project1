import numpy as np
from dataLoadFunction import dataLoad
from displayMenu import displayMenu
from dataStatistics import dataStatistics
from plottingFunction import dataPlot
from filter import dataFilter, filterArray

menuItems = np.array([ "Load Data","Filter data","Display statistics","Generate plots","Quit"])
filter = np.array([0, -1, -1])
isDataLoaded = False
isRunning = True
data = np.array([])
filtered = np.array([])

while isRunning:

    choice = displayMenu(menuItems)

    # ------------------------------------------------------------------
    if choice == 1:
        data = dataLoad(input("Please enter the name of the file: "))
        filtered = data.copy()
        isDataLoaded = True
    # ------------------------------------------------------------------
    elif choice == 2:
        filter = dataFilter()
        filtered = filterArray(data, filtered, filter)
    # ------------------------------------------------------------------
    elif choice == 3:
        if isDataLoaded:
            print(dataStatistics(filtered, input("Please enter the name of the statistic you would like to calculate:")))
        else:
            print("You Must Load Data Prior To Calculations")
    # ------------------------------------------------------------------
    elif choice == 4:
        if isDataLoaded:
            print(dataPlot(filtered))
        else:
            print("You Must Load Data Prior To Calculations")
    # ------------------------------------------------------------------
    elif choice == 5:    
        isRunning = False
