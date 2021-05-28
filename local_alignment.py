import copy
import numpy as np
import matplotlib.pyplot as plt


def make_matrix(sizex, sizey):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0] * sizey for i in range(sizex)]


# the desired strings to compare
v = 'AGCGTAG'
w = 'CTCGTCG'

# the scoring values
match = 10
mismatch = -5
gap = -7

best = 0
optloc = (0, 0)


def local_align(x, y, gap, match, mismatch):
    """Do a local alignment between x and y"""
    # create a zero-filled matrix
    A = make_matrix(len(x) + 1, len(y) + 1)
    # make a copy of A to keep the path
    path = make_matrix(len(x) + 1, len(y) + 1)
    print(len(A[0]))
    print(len(A))
    # print(A[12][11])
    best = 0
    optloc = (0, 0)
    # fill in A in the right order
    for i in range(1, len(y)):
        for j in range(1, len(x)):
            print("Test")
            # get the values of the neighbouring cells
            left = A[i][j - 1] + gap
            up = A[i - 1][j] + gap
            diagonally = A[i - 1][j - 1] + (match if x[i] == y[j] else mismatch)

            maxCell = max(left, up, diagonally, 0)

            # the local alignment recurrance rule:
            A[i][j] = maxCell

            # track the cell with the largest score
            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i, j)

            # track the path in a matrix
            # 0 is left
            # 1 is up
            # 2 is diagonally
            # 3 is zero value
            if left == maxCell:
                path[i][j] = 0
            elif up == maxCell:
                path[i][j] = 1
            elif diagonally == maxCell:
                path[i][j] = 2
            else:
                path[i][j] = 3

    # track where we got
    # return the opt score and the best location
    return best, optloc, path, A


best, optloc, path, matrix = local_align(v, w, gap, match, mismatch)

print("The biggest value is: " + str(best) + " in position " + str(optloc))

print("The final matrix is:")
for i in range(1, len(path)):
    print(matrix[i])

print("The matrix for the path is:")
for i in range(1, len(path)):
    print(path[i])
'''
plt.imshow(matrix)
plt.colorbar()
plt.show()
'''
