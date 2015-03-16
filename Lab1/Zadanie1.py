__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def filterMethodOne(list,axis):
    srednia=np.mean(list[:,axis])
    sigma=np.std(list[:,axis])
    print("{0} {1}".format(srednia,sigma))
    return list[abs(list[:,axis]-srednia)> 3.0*sigma]
file =open("haberman.data","r")
data=[]
for x in file:
    line=[int(value) for value in x.split(',')]
    data.append(line)
data=np.array(data)
data_group1=data[data[:,3]==1]
data_group2=data[data[:,3]==2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_group1[:,0],data_group1[:,1],data_group1[:,2],c='r',marker='o')
ax.scatter(data_group2[:,0],data_group2[:,1],data_group2[:,2],c='b',marker='x')
ax.set_xlabel('Wiek')
ax.set_ylabel('Rok')
ax.set_zlabel('Węzły')
print("Kolumna 1")
print(filterMethodOne(data,0))
print("Kolumna 2")
print(filterMethodOne(data,1))
print("Kolumna 3")
print(filterMethodOne(data,2))
#plt.show()

