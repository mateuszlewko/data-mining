import numpy as np

a = np.arange(1, 101, 1)
b = np.arange(1, 100, 2)
_c = np.arange(-1.0, 1.01, 0.01)
c = _c * np.pi
d = _c[(_c > 0.0001) | (_c < -0.0001)] * np.pi
e = np.maximum(np.sin(a), np.zeros(a.shape))

for v in (a, b, c, d, e):
    print(v)
print(c.shape, d.shape)

A = a.reshape((10, 10))
d1 = np.arange(99, 0, -1)
B = np.diag(d1, -1) + np.diag(a) + np.diag(d1, 1)
C = np.triu(np.ones((100, 100)))
D = np.array((np.arange(1, 11), np.arange(1, 11)))
for i in range(1, D.shape[1]):
    D[:, i] = [i + 1 + D[0, i - 1], (i + 1) * D[1, i - 1]]
    
E = np.array([[1 if i % j == 0 else 0 for j in range(1, 101)] for i in range(1, 101)])

for m in (A, B, C, D, E):
    print(m)