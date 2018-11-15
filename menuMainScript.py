import numpy as np
from dataLoadFunction import dataLoad
from displayMenu import displayMenu
from dataStatistics import dataStatistics
from plottingFunction import dataPlot

menuItems = np.array([ "Load Data","Filter data","Display statistics","Generate plots","Quit"])

while True:

    choice = displayMenu(menuItems)
    # ------------------------------------------------------------------
    if choice == 1:
        dataLoad(input("Please enter the name of the file: "))
    # ------------------------------------------------------------------
    elif choice == 2:
        o = 9
    # ------------------------------------------------------------------        
    elif choice == 3:
        p = 3
    # ------------------------------------------------------------------
    elif choice == 4:
        j = 4
    # ------------------------------------------------------------------
    elif choice == 5:    
        break
