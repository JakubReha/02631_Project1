import numpy as np
import matplotlib.pyplot as plt
def dataPlot(data):
    height = [sum(data[:,2]==1),sum(data[:,2]==2),sum(data[:,2]==3),sum(data[:,2]==4)]
    bars = ('Salmonella enterica', 'Bacillus cereus', 'Listeria', ' Brochothrix thermosphacta')
    y_pos = [2,5,7,10]
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.xlabel("Type of Bacteria") # Set the x-axis label
    plt.ylabel("Number of the individual type bacteria")
    plt.show()
