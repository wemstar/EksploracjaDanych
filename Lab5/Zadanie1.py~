import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import random
import scipy.spatial as KDTree

Y=[]
R=[]
movieIds=np.zeros(1683)
with open('y.txt') as yfile:
	for x in yfile:
		Y.append(x.split(','))
with open('r.txt') as rfile:
	for x in rfile:
		R.append(x.split(','))

with open('movie_ids.txt') as mfile:
	for x in mfile:
		z=x.split(' ')
		movieIds[int(z[0])]=' '.join(z[1:-1])

Y=np.array(Y).astype(int)
R=np.array(R).astype(int)

myRating=np.zeros(1682)
i=0
for x in movieIds.keys():
	myRating[int(x)]=random.choice([1,2,3,4,5])
	i+=1
	if i > 20:
		break
tree=KDTree.KDTree(np.transpose(R))
z=tree.query(myRating,20)
for x in movieIds[myRating[:]==0]:
	print(x)
