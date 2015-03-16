__author__ = 'wemstar'

import scipy.spatial as spatial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def method2(data, axis, neighbur=5, itemsToEliminate=5):
    tree1 = spatial.KDTree(data[:, :-1])
    distance,indexes= tree1.query(data[:,:-1], neighbur)
    a=np.vstack((distance[:,4],indexes[:,4],range(len(indexes[:,4])))).T
    toDelete=a[a[:,0].argsort()][-5:].astype(int)
    return np.delete(data,toDelete[:,2],0)


file = open("haberman.data", "r")
data = []
for x in file:
    line = [int(value) for value in x.split(',')]
    data.append(line)
data = np.array(data)
data2 = method2(data, 0)
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection='3d')

ax.scatter(data[:,0],data[:,1],data[:,2],c='r',marker='o')
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.scatter(data2[:,0],data2[:,1],data2[:,2],c='b',marker='x')
ax.set_xlabel('Wiek')
ax.set_ylabel('Rok')
ax.set_zlabel('Węzły')
plt.show()

