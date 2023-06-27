
x = Vector(1, 2)
print(x.y)
print(normalize(x).x, normalize(x).y)

import numpy as np
A = np.array([0, 1])
B = np.array([1, 2])
print(np.mean(B))
dist = np.linalg.norm(A - B)
print(dist)

C = A + B
print(C[0])
C = A * B
C = C.T
C = np.dot(A, B)