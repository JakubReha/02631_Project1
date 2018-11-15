def sortTemperatureGrowthRate(Temperature, GrowthRate):
    import numpy as np

    sortedTemperature=[]
    sortedGrowthrate=[]
    T1=[]
    dtype=[('temperature',int),('GRate',float)]



    for i in range (len(Temperature)):
        T1.append((Temperature[i],GrowthRate[i]))
        
    TemperatureGrowthrate1=np.array(T1, dtype=dtype)
    TemperatureGrowthrate1=np.sort(TemperatureGrowthrate1, order='temperature')

    for i in range (len(TemperatureGrowthrate1)):
        sortedTemperature.append(TemperatureGrowthrate1[i][0])
        sortedGrowthrate.append(TemperatureGrowthrate1[i][1])
    
    return(sortedTemperature,sortedGrowthrate)
from Data_load_function import dataLoad    
import numpy as np
import matplotlib.pyplot as plt
def dataPlot2(data):
    Temperature1=np.array([])
    Temperature2=np.array([])
    Temperature3=np.array([])
    Temperature4=np.array([])
    for i in range (len(data[:,0])):
        if data[i,2]==1:
            Temperature1=np.append(Temperature1,np.array([data[i,0]]))
        elif data[i,2]==2:
            Temperature2=np.append(Temperature2,np.array([data[i,0]]))
        elif data[i,2]==3:
            Temperature3=np.append(Temperature3,np.array([data[i,0]]))
        elif data[i,2]==4:
            Temperature4=np.append(Temperature4,np.array([data[i,0]]))
    
    GRate1=([])
    GRate2=([])
    GRate3=([])
    GRate4=([])
    for i in range(len(data[:,1])):
        if data[i,2]==1:
            GRate1=np.append(GRate1,np.array([data[i,1]]))
        elif data[i,2]==2:
            GRate2=np.append(GRate2,np.array([data[i,1]]))
        elif data[i,2]==3:
            GRate3=np.append(GRate3,np.array([data[i,1]]))
        elif data[i,2]==4:
            GRate4=np.append(GRate4,np.array([data[i,1]]))
            
    plt.plot((sortTemperatureGrowthRate(Temperature1,GRate1)[0]),(sortTemperatureGrowthRate(Temperature1,GRate1)[1]),color='green')
    plt.plot((sortTemperatureGrowthRate(Temperature2,GRate2)[0]),(sortTemperatureGrowthRate(Temperature2,GRate2)[1]), color='orange')
    plt.plot((sortTemperatureGrowthRate(Temperature3,GRate3)[0]),(sortTemperatureGrowthRate(Temperature3,GRate3)[1]), color='red')
    plt.plot((sortTemperatureGrowthRate(Temperature4,GRate4)[0]),(sortTemperatureGrowthRate(Temperature4,GRate4)[1]), color='yellow')
    plt.xlabel('Temperature')
    plt.ylabel('Growth Rate')
    plt.title('Graph for bacteria growth with Temperature')
    plt.show()
