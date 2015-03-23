__author__ = 'wemstar'


import pylab as P
from matplotlib.mlab import PCA
lista=[]
for x in open("seeds_dataset.txt"):
    lista.append(x.split(";"))
lista=P.array(lista)
lista=lista.astype(float)


listaPCA=PCA(lista[:,:-1]).Y

ziarno1=listaPCA[lista[:,-1]==1.0]
ziarno2=listaPCA[lista[:,-1]==2.0]
ziarno3=listaPCA[lista[:,-1]==3.0]
P.scatter(ziarno1[:,0],ziarno1[:,1],color='r')
P.scatter(ziarno2[:,0],ziarno2[:,1],color='g')
P.scatter(ziarno3[:,0],ziarno3[:,1],color='b')
P.show()

