import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform some operations
print("Array:", arr)
print("Array multiplied by 2:", arr * 2)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):")
print(matrix)

# Perform matrix multiplication
matrix_mult = np.dot(matrix, matrix.T)  # Transpose and multiply
print("Matrix multiplied by its transpose:")
print(matrix_mult)

# Get statistics
print("Mean of the array:", np.mean(arr))
print("Standard deviation of the array:", np.std(arr))
