def null(rows, columns):
    null_matrix = [
        [0 for i in range(columns)] for i in range(rows)
    ]  # loop over columns then over rows
    return null_matrix


def row_wise(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print("\n")


def upper_triangular(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    upper_matrix = null(rows, columns)  # null matrix
    for i in range(rows):
        for j in range(columns):
            if i >= j:
                upper_matrix[i][j] += matrix[i][j]
            else:
                continue
    return upper_matrix


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose_matrix = null(columns, rows)  # null matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] += matrix[i][j]  # definition of transpose

    return transpose_matrix


def Matrix_Sum(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(
        matrix2[0]
    ):  # Checking for compatibility for addition
        rows, columns = len(matrix1), len(matrix1[0])
        sum_matrix = null(rows, columns)
        for i in range(rows):
            for j in range(columns):
                sum_matrix[i][j] += matrix1[i][j] + matrix2[i][j]
        return sum_matrix
    else:
        return -1


def Matrix_Difference(matrix1, matrix2):
    # The program is matrix1-matrix2, since subtraction is not commutative
    matrix2_new = null(len(matrix2), len(matrix2[0]))
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            matrix2_new[i][j] = -matrix2[i][
                j
            ]  # From the definition of the negative of a matrix
    return Matrix_Sum(
        matrix1, matrix2_new
    )  # From the definition of difference of two matrices


def Division(mx, scalar: int):
    new_matrix = null(len(mx), len(mx[0]))
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            new_matrix[i][j] += mx[i][j] / scalar
    return new_matrix


def Minor_Matrix(mx, r, c):
    return [row[:c] + row[c + 1 :] for row in (mx[:r] + mx[r + 1 :])]


def Determinant(mx):
    # for an even smaller case
    if len(mx) == 1:
        return mx[0][0]
    # for the base case when the matrix is 2*2
    if len(mx) == 2:
        return mx[0][0] * mx[1][1] - mx[0][1] * mx[1][0]
    determinant = 0
    # We will only expand along the first row
    for i in range(len(mx)):
        determinant += (
            ((-1) ** i) * mx[0][i] * Determinant(Minor_Matrix(mx, 0, i))
        )  # By definition
    return determinant


def Adjoint(mx):
    temp_matrix = []  # Empty matrix before the transpose
    for i in range(len(mx)):
        row = []  # Initialise each row
        for j in range(len(mx)):
            row.append(
                ((-1) ** (i + j)) * Determinant(Minor_Matrix(mx, i, j))
            )  # from the definition of adjoint
        temp_matrix.append(row)
    return transpose(temp_matrix)


def Inverse(mx):
    if Determinant(mx) == 0:
        return None  # The inverse does not exist in this case
    else:
        return Division(Adjoint(mx), Determinant(mx))  # By definition
