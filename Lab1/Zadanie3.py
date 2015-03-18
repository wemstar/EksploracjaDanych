__author__ = 'wemstar'

import scipy.spatial as spatial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def kneighbours(data, neighbur=5, itemsToEliminate=5):
    tree1 = spatial.KDTree(data[:, :-1])
    distance,indexes= tree1.query(data[:,:-1], neighbur)
    indexes=indexes.astype(int)
    return distance,indexes

def gestosc(distance):

    gestoscTab=np.mean(distance,axis=1)
    return gestoscTab

def neighbourMena(gestosc,indexes):
    np.zeros(len(ge))
file = open("haberman.data", "r")
data = []
for x in file:
    line = [int(value) for value in x.split(',')]
    data.append(line)
data = np.array(data)
distance,indexes = kneighbours(data)
gestosciPunkt=gestosc(distance)
gestosciSasiadow=neighbourMena(gestosciPunkt,indexes)


