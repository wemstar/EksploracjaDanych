import pylab as P
from matplotlib.mlab import PCA
import scipy.spatial as spatial
import numpy as np
lista=[]

def kneighbours(learn,test, neighbur=5, itemsToEliminate=5):
    tree1 = spatial.KDTree(learn[:, :-1])
    distance,indexes= tree1.query(test[:,:-1], neighbur,p=1.5)
    indexes=indexes.astype(int)
    return distance,indexes


for x in open("seeds_dataset.txt"):
    lista.append(x.split(";"))
lista=P.array(lista)
lista=lista.astype(float)
de=[]
for x in range(100):
	np.random.shuffle(lista)
	test,learn=lista[:int(len(lista)/2)], lista[int(len(lista)/2):]
	distance,indexes=kneighbours(learn,test,10)
	poprawne=learn[indexes[:,-1],-1] == test[:,-1]
	de.append(np.sum(poprawne)/float(len(poprawne)))
P.plot(de)
P.show()
