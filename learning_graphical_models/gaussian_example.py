import numpy as np

def pretty(mat, label):
    print('Covariance Matrix {}'.format(label))
    print(mat)
    matinv = np.linalg.inv(mat)
    print('Inverse Covariance Matrix {}'.format(label))
    print(matinv)

A = np.array([[9, 3, 1], [3, 9, 3], [1, 3, 9]])
B = np.array([[8, -3, 1], [-3, 9, -3], [1, -3, 8]])
C = np.array([[9, 3, 0], [3, 9, 3], [0, 3, 9]])
D = np.array([[9, -3, 0], [-3, 10, -3], [0, -3, 9]])

K = np.array([[1, 0.5, 0], [0.5, 1, 0.5], [0, 0.5, 1]])
pretty(C, 'C')
pretty(D, 'D')
pretty(K, 'K')
