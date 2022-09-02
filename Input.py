def null(rows, columns):
    null_matrix = [
        [0 for i in range(columns)] for i in range(rows)
    ]  # loop over columns then over rows
    return null_matrix


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose_matrix = null(columns, rows)  # null matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] += matrix[i][j]  # definition of transpose

    return transpose_matrix


def Minor_Matrix(mx, r, c):
    return [row[:c] + row[c + 1 :] for row in (mx[:r] + mx[r + 1 :])]


def Determinant(mx):
    # for a single celled matrix
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


def Division(mx, scalar: float):
    new_matrix = null(len(mx), len(mx[0]))
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            new_matrix[i][j] += mx[i][j] / scalar
    return new_matrix


def Inverse(mx):
    if Determinant(mx) == 0:
        return None  # The inverse does not exist in this case
    else:
        return Division(Adjoint(mx), Determinant(mx))  # By definition


print(Inverse([[4, 3, 2], [0, 1, -3], [0, -2, 3]]))
