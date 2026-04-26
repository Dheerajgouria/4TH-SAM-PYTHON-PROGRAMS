# ============================================
# Practical 22: Matrix Multiplication
# ============================================
# Aim: Write a program to multiply two matrices

def get_matrix(name, rows, cols):
    print(f"\nEnter elements of {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"  [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def multiply_matrices(A, B, r1, c1, c2):
    result = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print("  ", row)

# ---- Main Program ----
print("--- Matrix Multiplication ---")
r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
c2 = int(input("Enter columns of Matrix B: "))

A = get_matrix("Matrix A", r1, c1)
B = get_matrix("Matrix B", c1, c2)

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

result = multiply_matrices(A, B, r1, c1, c2)
print_matrix(result, "Result (A x B)")

# Output Example:
# Matrix A:        Matrix B:
# [1, 2]           [5, 6]
# [3, 4]           [7, 8]
# Result:
# [19, 22]
# [43, 50]
