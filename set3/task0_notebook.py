#%%
from task0 import kmeans
from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp


#%%
iris = datasets.load_iris() 
labels, centers = kmeans(iris.data, 3)


sepal_length = iris.data[:,iris.feature_names.index('sepal length (cm)')]
sepal_width = iris.data[:, iris.feature_names.index('sepal width (cm)')]

print(iris.data, iris.target, iris.feature_names, iris.target_names)

for target in set(iris.target):
    ids = target == iris.target
    print('ids', target, ids)
    plt.scatter(sepal_length[ids], sepal_width[ids], color='bgr'[target])
    

colors = ["g.","r.","c.","y."]

#%%
for i in range(len(X)):
    print("coordinate:",X[i], "label:", l[i])
    plt.plot(X[i][0], X[i][1], colors[l[i]], markersize = 10)
plt.scatter(c[:, 0],c[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
