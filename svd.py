import numpy as np

""" sample matrix """
matrix = np.array([[9, 7, 4],
                   [1, 3, 5],
                   [7, 12, 11]])

""" singular value decomposition """"
left_vectors, singular_values, right_transpose = np.linalg.svd(matrix)

"""" factorized matrices """
print("U matrix:")
print(left_vectors)
print("\nS matrix (diagonal values):")
print(singular_values)
print("\nVT matrix:")
print(right_transpose)