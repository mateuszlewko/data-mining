from matplotlib import pyplot as plt
import numpy as np


def get_centers(K, d):
    args = range(K)
    alpha = 2.0 * np.pi / K
    r = d / (np.sin(alpha / 2.0) * 2)
    xcs = np.vectorize(lambda k: r * np.cos(k * 2 * np.pi / K))(args)
    ycs = np.vectorize(lambda k: r * np.sin(k * 2 * np.pi / K))(args)
    return zip(xcs, ycs)

def get_clouds(K, d):
    points = []

    for (xc, yc) in get_centers(K, d):
        xs = np.random.normal(xc, 1., 1000)
        ys = np.random.normal(yc, 1., 1000)

        points.append((xc, yc, xs, ys))
        plt.scatter(xs, ys, s=0.1)

    return points 

def main():
    get_clouds(7, 5)
    plt.savefig('zadanie4a.png', dpi=500)
    plt.close()

    get_clouds(11, 10)
    plt.savefig('zadanie4b.png', dpi=500)
    plt.close()

    get_clouds(23, 15)
    plt.savefig('zadanie4c.png', dpi=500)
    plt.close()

if __name__ == '__main__':
    main()
