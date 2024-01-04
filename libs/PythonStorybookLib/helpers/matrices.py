
import random
import numpy as np

def generateMatrixWithRandInts(size, maxNumber):
    rowSize = size[0]
    columnSize = size[1]
    M = np.zeros(size, dtype = int)

    for i in range(0, rowSize):
        for j in range(0, columnSize):
            M[i, j] = random.randint(0, maxNumber)

    return M