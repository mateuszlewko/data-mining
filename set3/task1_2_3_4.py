from profilehooks import timecall
from task0 import kmeans, print_kmeans_errors
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
import scipy.spatial
import random
import scipy.stats
import csv

### Task 3 ###

def test_data(path, get_data, get_labels, k):
    data = np.genfromtxt(path, delimiter=',')
    labels = get_labels(data)
    data = get_data(data)

    predict_labels, _ = kmeans(data, k)
    print('Data:', path[5:-4])
    print_kmeans_errors(k, labels, predict_labels)
    
test_data("data/pokerhand.csv", lambda x: x[:,  : -1], lambda x: x[:, -1] - 1 , 9)
test_data("data/wine.csv"     , lambda x: x[:, 1:   ], lambda x: x[:, 0]  - 1 , 3)
test_data("data/iris.csv"     , lambda x: x[:,  : -1], lambda x: x[:, -1]     , 3)
test_data("data/spam.csv"     , lambda x: x[:,  : -1], lambda x: x[:, -1]     , 2)
test_data("data/glass.csv"    , lambda x: x[:, 1: -1], lambda x: x[:, -1] - 1 , 6)

### Task 4 ### 

def gen_pic(picture, colors):
    shape = picture.shape
    print(shape)
    flat = picture.reshape((-1, 3))
    labels, centers = kmeans(flat, colors)
    print(centers)
    print(labels)

    new_picture = np.array(list(map(lambda x: list(map(int, centers[x])), labels)))
    new_picture = new_picture.reshape(shape)
    return new_picture

for i in range(5):
    path = 'data/cat' + str(i + 1) + '.jpg'
    img = scipy.misc.imread(path)
    
    plt.imshow(img)
    plt.show()

    for k in (3, 5, 8):
        pic = gen_pic(img, k)
        plt.close()
        plt.imshow(pic)
        plt.savefig(path + str(k) + '.jpg')
        plt.show()