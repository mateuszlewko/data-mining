from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np


iris = datasets.load_iris() 

sepal_length = iris.data[:,iris.feature_names.index('sepal length (cm)')]
sepal_width = iris.data[:, iris.feature_names.index('sepal width (cm)')]

print(iris.data, iris.target, iris.feature_names, iris.target_names)

def drawn_by_line(line):
    above_line = line(sepal_length) < sepal_width
    below_line = line(sepal_length) >= sepal_width

    for target in set(iris.target):
        name = iris.target_names[target]
        if (name == 'versicolor'):
            continue

        ids = target == iris.target
        ids_above = np.logical_and(ids, above_line)
        ids_below = np.logical_and(ids, below_line)

        # print('ids', target, ids)
        plt.scatter(sepal_length[ids_above], sepal_width[ids_above], color= 'g' if name == 'setosa' else 'r')
        plt.scatter(sepal_length[ids_below], sepal_width[ids_below], color= 'r' if name == 'setosa' else 'g')
        
    plt.title('Iris')
    plt.xlabel('sepal length (cm)')
    plt.ylabel('sepal width (cm)')

    X = range(3, 10)
    plt.plot(X, line(X))
    plt.xticks(X)
    plt.yticks(range(1, 6))


drawn_by_line(np.vectorize(lambda x: 2.0 * x - 8.0))
# plt.show()
plt.savefig('zadanie2a.png')

plt.close()
drawn_by_line(np.vectorize(lambda x: 1.5 * x - 4.8))
# plt.show()
plt.savefig('zadanie2b.png')
