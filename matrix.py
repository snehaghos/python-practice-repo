#matrix in python

def create_matrix(rows, cols, fill=0):
    return [[fill for _ in range(cols)] for _ in range(rows)]

def pretty_print(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("Matrix:")
    pretty_print(m)

    z = create_matrix(4, 5)
    print("\n4x5 zero matrix:")
    pretty_print(z)

