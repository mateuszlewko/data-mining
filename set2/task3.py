from matplotlib import pyplot as plt
import numpy as np

X = range(1, 11)
Y = (10, 10, 11, 11, 12, 18, 18, 26, 19, 26)
plt.scatter(X, Y)
line = np.vectorize(lambda x: 2.0 * x + 5.0)
plt.plot(X, line(X))

plt.savefig('zadanie3a.png')

# line: a*x + b = y; 
def point_to_line_dist(a, b, xp, yp):
    return np.absolute(a * xp - yp + b) / np.sqrt(a * a + 1)

def dists(a, b):
    s = 0
    for x, y in zip(X, Y):
        d = point_to_line_dist(a, b, x, y)
        s += d
        print('(%d, %d) => %f' % (x, y, d))

    print('dist sum:', s)
    
dists(2.0, 5.0)

plt.close()
plt.scatter(X, Y)
na = 2.12
nb = 4.6
line2 = np.vectorize(lambda x: na * x + nb)
plt.plot(X, line2(X))

plt.savefig('zadanie3b.png')

dists(na, nb)
# plt.show()