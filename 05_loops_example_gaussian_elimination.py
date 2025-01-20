import numpy as np

# Example matrix (coefficients) and vector (constants)
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

b = np.array([8, -11, -3], dtype=float)

rows, cols = A.shape  # Number of rows and columns

print("Initial Matrix (A) and Vector (b):")
print("A =\n", A)
print("b =", b, "\n")

# Gauss-Jordan Elimination
for i in range(rows):  # Outer loop for each pivot row
    # Normalize the pivot row
    pivot = A[i, i]
    A[i] = A[i] / pivot
    b[i] = b[i] / pivot
    print(f"Step {i + 1}: Normalized row {i}.")
    print("A =\n", A)
    print("b =", b, "\n")

    # Eliminate entries below and above the pivot
    for j in range(rows):  # Loop through all rows (not just below the pivot)
        if j != i:  # Skip the pivot row
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            print(f"Eliminating entry in row {j}, column {i}.")
            print("A =\n", A)
            print("b =", b, "\n")

print("Reduced Row Echelon Form (RREF):")
print("A =\n", A)
print("b =", b, "\n")

# Solution is directly in the vector b
print("Solution Vector (x):", b)