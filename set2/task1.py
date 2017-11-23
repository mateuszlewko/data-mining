from sklearn import datasets
from matplotlib import pyplot as plt


iris = datasets.load_iris() 

sepal_length = iris.data[:,iris.feature_names.index('sepal length (cm)')]
sepal_width = iris.data[:, iris.feature_names.index('sepal width (cm)')]

print(iris.data, iris.target, iris.feature_names, iris.target_names)

for target in set(iris.target):
    ids = target == iris.target
    print('ids', target, ids)
    plt.scatter(sepal_length[ids], sepal_width[ids], color='bgr'[target])
    

plt.title('Iris')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.xticks(range(3, 10))
plt.yticks(range(1, 6))
# plt.show()
plt.savefig('zadanie1.png')
