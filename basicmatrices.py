import pickle
from typing import *


def pow_2(num: int | float) -> bool:  # Used later in the file
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def null(rows: int, columns: int) -> list[list[int]]:
    null_matrix = [
        [0 for i in range(columns)] for i in range(rows)
    ]  # loop over columns then over rows
    return null_matrix


def row_wise(matrix: list[list]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print("\n")


def upper_triangular(matrix: list[list]) -> list[list]:
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


def transpose(matrix: list[list]) -> list[list]:
    rows = len(matrix)
    columns = len(matrix[0])
    transpose_matrix = null(columns, rows)  # null matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] += matrix[i][j]  # definition of transpose

    return transpose_matrix


def Matrix_Sum(matrix1: list[list], matrix2: list[list]) -> list[list] | int:
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


def Matrix_Difference(matrix1: list[list], matrix2: list[list]) -> list[list] | int:
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


def Division(mx: list[list], scalar: float) -> list[list]:
    new_matrix = null(len(mx), len(mx[0]))
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            new_matrix[i][j] += mx[i][j] / scalar
    return new_matrix


def Minor_Matrix(mx: list[list], r: int, c: int) -> list[list]:
    return [row[:c] + row[c + 1 :] for row in (mx[:r] + mx[r + 1 :])]


def Determinant(mx: list[list]) -> float:
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


def Adjoint(mx: list[list]) -> list[list]:
    temp_matrix = []  # Empty matrix before the transpose
    for i in range(len(mx)):
        row = []  # Initialise each row
        for j in range(len(mx)):
            row.append(
                ((-1) ** (i + j)) * Determinant(Minor_Matrix(mx, i, j))
            )  # from the definition of adjoint
        temp_matrix.append(row)
    return transpose(temp_matrix)


def Inverse(mx: list[list]) -> list[list] | None:
    if Determinant(mx) == 0:
        return None  # The inverse does not exist in this case
    else:
        return Division(Adjoint(mx), Determinant(mx))  # By definition


def Matrix_Multiplication(mx1: list[list], mx2: list[list]) -> list[list]:
    return [
        [
            sum([mx1[i][k] * mx2[k][j] for k in range(len(mx1[0]))])
            for j in range(len(mx2[0]))
        ]
        for i in range(len(mx1))
    ]  # Basically a one-liner, but looks bigger due to formatting


def joining_horizontally(mx1: list[list], mx2: list[list]) -> list[list]:
    a_matrix = null(len(mx1), len(mx1[0]) + len(mx2[0]))

    for i in range(len(mx1)):
        for j in range(len(mx1[0])):
            a_matrix[i][j] = mx1[i][j]
    for i in range(len(mx2)):
        for j in range(len(mx2[0])):
            a_matrix[i][j + len(mx1[0])] = mx2[i][j]
    return a_matrix


def joining_vertically(mx1: list[list], mx2: list[list]) -> list[list]:
    n = len(mx1)
    new_matrix = []
    for i in mx1:
        new_matrix.append(i)
    for j in mx2:
        new_matrix.append(j)
    return new_matrix


def split(mx: list[list]) -> Any:
    if len(mx) == len(mx[0]) and pow_2(len(mx)):
        n = len(mx) // 2
        a = mx[:n]
        b = mx[n:]
        a_11 = [a[i][:n] for i in range(n)]
        a_12 = [a[i][n:] for i in range(n)]
        a_13 = [b[i][:n] for i in range(n)]
        a_14 = [b[i][n:] for i in range(n)]
    return a_11, a_12, a_13, a_14


def strassen(mx1: list[list], mx2: list[list] | int) -> list[list]:
    if len(mx1) == 1:
        return [[mx1[0][0] * mx2[0][0]]]
    a_11, a_12, a_21, a_22 = split(mx1)
    b_11, b_12, b_21, b_22 = split(mx2)
    p_1, p_2, p_3, p_4, p_5, p_6, p_7 = (
        strassen(Matrix_Sum(a_11, a_22), Matrix_Sum(b_11, b_22)),
        strassen(a_22, Matrix_Difference(b_21, b_11)),
        strassen(Matrix_Sum(a_11, a_12), b_22),
        strassen(Matrix_Difference(a_12, a_22), Matrix_Sum(b_21, b_22)),
        strassen(a_11, Matrix_Difference(b_12, b_22)),
        strassen(Matrix_Sum(a_21, a_22), b_11),
        strassen(Matrix_Difference(a_11, a_21), Matrix_Sum(b_11, b_12)),
    )  # Exactly from the theory
    c_11, c_12, c_21, c_22 = (
        Matrix_Difference(Matrix_Sum(Matrix_Sum(p_1, p_2), p_4), p_3),
        Matrix_Sum(p_3, p_5),
        Matrix_Sum(p_2, p_6),
        Matrix_Difference(Matrix_Sum(p_1, p_5), Matrix_Sum(p_6, p_7)),
    )  # Exactly from the theory
    return joining_vertically(
        joining_horizontally(c_11, c_12), joining_horizontally(c_21, c_22)
    )
