# Matrix patterns in Python
# Covers: spiral order, diagonal traversal, zigzag, rotation, wave, bordered matrix

def pretty_print(matrix):
    for row in matrix:
        print(" ".join(str(x).rjust(4) for x in row))

def spiral_order(matrix):
    if not matrix:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

def anti_diagonal(matrix):
    n = len(matrix)
    for k in range(2 * n - 1):
        if k < n:
            i, j = 0, k
        else:
            i, j = k - n + 1, n - 1
        line = []
        while i < n and j >= 0:
            line.append(matrix[i][j])
            i += 1
            j -= 1
        print(" ".join(str(x).rjust(4) for x in line))

def main_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        print(str(matrix[i][i]).rjust(4), end="")
    print()

def anti_diagonal_line(matrix):
    n = len(matrix)
    for i in range(n):
        print(str(matrix[i][n - 1 - i]).rjust(4), end="")
    print()

def zigzag_order(matrix):
    result = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix[0])):
                result.append(matrix[i][j])
        else:
            for j in range(len(matrix[0]) - 1, -1, -1):
                result.append(matrix[i][j])
    return result

def wave_order(matrix):
    result = []
    for j in range(len(matrix[0])):
        if j % 2 == 0:
            for i in range(len(matrix)):
                result.append(matrix[i][j])
        else:
            for i in range(len(matrix) - 1, -1, -1):
                result.append(matrix[i][j])
    return result

def rotate_90_clockwise(matrix):
    n = len(matrix)
    result = []
    for j in range(n):
        row = []
        for i in range(n - 1, -1, -1):
            row.append(matrix[i][j])
        result.append(row)
    return result

def rotate_90_anticlockwise(matrix):
    n = len(matrix)
    result = []
    for j in range(n - 1, -1, -1):
        row = []
        for i in range(n):
            row.append(matrix[i][j])
        result.append(row)
    return result

def rotate_180(matrix):
    n = len(matrix)
    result = []
    for i in range(n - 1, -1, -1):
        row = []
        for j in range(n - 1, -1, -1):
            row.append(matrix[i][j])
        result.append(row)
    return result

def bordered_matrix(matrix):
    n = len(matrix)
    border = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                row.append(matrix[i][j])
            else:
                row.append(0)
        border.append(row)
    return border

def inner_matrix(matrix):
    n = len(matrix)
    inner = []
    for i in range(1, n - 1):
        row = []
        for j in range(1, n - 1):
            row.append(matrix[i][j])
        inner.append(row)
    return inner

def sum_of_diagonals(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return primary, secondary

def boundary_elements(matrix):
    n = len(matrix)
    elements = []
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                elements.append(matrix[i][j])
    return elements

def saddle_points(matrix):
    points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]
            row_min = all(val <= matrix[i][k] for k in range(len(matrix[0])))
            col_max = all(val >= matrix[k][j] for k in range(len(matrix)))
            if row_min and col_max:
                points.append((i, j, val))
    return points

if __name__ == "__main__":
    m = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16],
    ]

    print("Matrix:")
    pretty_print(m)

    print("\n--- Spiral Order ---")
    print(" ".join(str(x) for x in spiral_order(m)))

    print("\n--- Main Diagonal ---")
    main_diagonal(m)

    print("--- Anti Diagonal ---")
    anti_diagonal_line(m)

    print("\n--- All Anti Diagonals ---")
    anti_diagonal(m)

    print("\n--- Zigzag Order (row by row, alternating direction) ---")
    print(" ".join(str(x) for x in zigzag_order(m)))

    print("\n--- Wave Order (column by column, alternating direction) ---")
    print(" ".join(str(x) for x in wave_order(m)))

    print("\n--- Rotate 90 Clockwise ---")
    pretty_print(rotate_90_clockwise(m))

    print("\n--- Rotate 90 Anticlockwise ---")
    pretty_print(rotate_90_anticlockwise(m))

    print("\n--- Rotate 180 ---")
    pretty_print(rotate_180(m))

    print("\n--- Bordered Matrix (keep edges, zero inner) ---")
    pretty_print(bordered_matrix(m))

    print("\n--- Inner Matrix (remove edges) ---")
    pretty_print(inner_matrix(m))

    print("\n--- Diagonal Sums ---")
    p, s = sum_of_diagonals(m)
    print(f"Primary: {p}, Secondary: {s}")

    print("\n--- Boundary Elements ---")
    print(" ".join(str(x) for x in boundary_elements(m)))

    print("\n--- Saddle Points (min in row, max in column) ---")
    sp = saddle_points(m)
    if sp:
        for r, c, v in sp:
            print(f"  Position ({r},{c}) = {v}")
    else:
        print("  None found")
