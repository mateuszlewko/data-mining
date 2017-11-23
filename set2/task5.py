from matplotlib import pyplot as plt
from task4 import get_clouds
import numpy as np


def dist(a, b, x, y):
    return (a - x) ** 2 + (b - y) ** 2

def draw_redgreen(K, d):
    clouds = get_clouds(K, d)
    reds_x = []
    reds_y = []
    greens_x = []
    greens_y = []

    for i, (xc, yc, xs, ys) in enumerate(clouds):
        for x, y in zip(xs, ys):
            closest = np.argmin(list(map(lambda c: dist(x, y, c[0], c[1]), clouds)))
            
            if closest == i:
                greens_x.append(x)
                greens_y.append(y)
            else:
                reds_x.append(x)
                reds_y.append(y)

    plt.scatter(reds_x, reds_y, s=0.1, color='r')
    plt.scatter(greens_x, greens_y, s=0.1, color='g')


draw_redgreen(7, 5)
plt.savefig('zadanie5a.png', dpi=500)
plt.close()

draw_redgreen(11, 10)
plt.savefig('zadanie5b.png', dpi=500)
plt.close()

draw_redgreen(23, 15)
plt.savefig('zadanie5c.png', dpi=500)
plt.close()