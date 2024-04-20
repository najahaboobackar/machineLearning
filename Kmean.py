from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
w=load_iris()
x=w.data
y=w.target
k=10
model=KMeans(n_clusters=k)
model.fit(x)
cen=model.cluster_centers_
labels=model.labels_
plt.scatter(x[:,0],x[:,1],c=labels,cmap="magma",s=50,alpha=0.5)
plt.scatter(cen[:,0],cen[:,1],marker="x",s=200,c="red",label="centroid")
plt.legend()
plt.show()