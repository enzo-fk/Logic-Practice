import numpy as np
import time
from tqdm.auto import tqdm

class MatrixOperations:
    def readMat(self, file):
        with open(file, 'r') as f:
            return [list(map(float, line.split(','))) for line in f.readlines()]

    def MatMul(self, matA, matB):
        if len(matA[0]) != len(matB):
            return 'Error: Matrixes cannot be multiplied.'
        result = [[sum(a*b for a, b in zip(rowA, colB)) for colB in zip(*matB)] for rowA in matA]
        return result

    def dumpMat(self, result, filename):
        with open(filename, 'w') as f:
            for row in result:
                f.write(','.join(map(str, row)) + '\n')

matrix_ops = MatrixOperations()
mat1 = matrix_ops.readMat('mat1.txt')
mat2 = matrix_ops.readMat('mat4.txt')
start_time = time.time()
result_list_method = matrix_ops.MatMul(mat1, mat2)
end_time = time.time()
time_list_method = end_time - start_time
print(result_list_method)

if isinstance(result_list_method, str):
    print(result_list_method)
else:
    matrix_ops.dumpMat(result_list_method, 'result.txt')
    print('\nList-based matrix multiplication completed in:', time_list_method, 'seconds\n')

mat1_np = np.array(mat1)
mat2_np = np.array(mat2)
try:
    start_time_np = time.time()
    result_numpy_method = np.dot(mat1_np, mat2_np)
    end_time_np = time.time()
    time_numpy_method = end_time_np - start_time_np
    print(result_numpy_method)
    print('\nNumpy-based matrix multiplication completed in:', time_numpy_method, 'seconds')
except ValueError as e:
    print(str(e))