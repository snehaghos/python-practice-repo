# Matrix operations in Python
# Supports: addition, subtraction, multiplication, transpose, determinant, identity matrix

def pretty_print(matrix):
    for row in matrix:
        print(" ".join(str(x).rjust(4) for x in row))

def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def subtract_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result

def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    
    if cols_a != rows_b:
        return None
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        minor = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            minor.append(row)
        sign = 1 if j % 2 == 0 else -1
        det += sign * matrix[0][j] * determinant(minor)
    return det

def identity_matrix(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        result.append(row)
    return result

def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        new_row = [x * scalar for x in row]
        result.append(new_row)
    return result

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
            if i != j and matrix[i][j] != 0:
                return False
    return True

if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    print("Matrix A:")
    pretty_print(A)
    print("\nMatrix B:")
    pretty_print(B)

    print("\n--- A + B ---")
    pretty_print(add_matrices(A, B))

    print("\n--- A - B ---")
    pretty_print(subtract_matrices(A, B))

    print("\n--- A x B ---")
    result = multiply_matrices(A, B)
    if result:
        pretty_print(result)
    else:
        print("Cannot multiply (dimensions mismatch)")

    print("\n--- Transpose of A ---")
    pretty_print(transpose(A))

    print("\n--- Determinant of A ---")
    print(determinant(A))

    print("\n--- 3x3 Identity Matrix ---")
    pretty_print(identity_matrix(3))

    print("\n--- Scalar multiply A * 2 ---")
    pretty_print(scalar_multiply(A, 2))

    print("\n--- Is A symmetric?", is_symmetric(A))
    print("--- Is Identity matrix?", is_identity(identity_matrix(3)))
