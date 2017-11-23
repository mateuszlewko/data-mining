from profilehooks import timecall
import numpy as np
import scipy as sp
import scipy.spatial


@timecall
def kmeans(data, k):
    center = data[np.random.randint(0, data.shape[0], k)]
    label = np.zeros(data.shape[0])

    while True:
        dist_mat = sp.spatial.distance.cdist(data, center, 'euclidean')
        
        center = np.zeros(center.shape)
        new_label = np.argmin(dist_mat, axis=1)

        for i in range(k):
            ith_group_idx = new_label == i
            ith_cnt = np.sum(ith_group_idx)
            
            if ith_cnt > 0.01: 
                center[i] = np.sum(data[ith_group_idx], axis=0) / ith_cnt
            else:
                center[i] = data[np.random.randint(0, data.shape[0])]
        
        if np.array_equal(label, new_label):
            return label, center

        label = new_label

def errors(data)
    