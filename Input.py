from typing import *

from basicmatrices import *


def pow_2(num: int | float) -> bool:
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def null(rows: int, columns: int) -> list:
    null_matrix = [
        [0 for i in range(columns)] for i in range(rows)
    ]  # loop over columns then over rows
    return null_matrix


def row_wise(matrix: list[list]) -> Any:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print("\n")


def transpose(matrix: list) -> list:
    rows = len(matrix)
    columns = len(matrix[0])
    transpose_matrix = null(columns, rows)  # null matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] += matrix[i][j]  # definition of transpose

    return transpose_matrix


def Minor_Matrix(mx: list[list], r: int, c: int):
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


def Division(mx, scalar: int | float):
    new_matrix = null(len(mx), len(mx[0]))
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            new_matrix[i][j] += mx[i][j] / scalar
    return new_matrix


def Inverse(mx: list) -> list:
    if Determinant(mx) == 0:
        return None  # The inverse does not exist in this case
    else:
        return Division(Adjoint(mx), Determinant(mx))  # By definition


def Multiplication(mx1: list, mx2: list) -> list:
    if len(mx1[0]) != len(mx2):
        return "The matrices are incompatible for multiplication."
    else:
        result = null(len(mx1), len(mx2[0]))
        for i in range(len(mx1)):  # Loop through rows of first matrix
            for j in range(len(mx2[0])):  # Loop through each column of second matrix
                for k in range(len(mx2)):  # Loop through each row of second matrix
                    result[i][j] += mx1[i][k] * mx2[k][j]  # By definition
        return result


def Matrix_Multiplication(mx1: list, mx2: list) -> list:
    return [
        [
            sum([mx1[i][k] * mx2[k][j] for k in range(len(mx1[0]))])
            for j in range(len(mx2[0]))
        ]
        for i in range(len(mx1))
    ]


# Use only for square matrices for now (not tested for rectangular)
def joining_horizontally(a: list, b: list) -> list[list]:
    n = len(a)
    new_matrix = null(
        len(a), len(a[0]) + len(b[0])
    )  # Null matrix of the same order as the expected output
    for i in range(n):
        for j in range(n):  # Two loops make it slow, better way?
            new_matrix[i][j] = a[i][j]  # First matrix
            new_matrix[i][j + n] = b[i][j]  # Second matrix
    return new_matrix


def joining_vertically(mx1: list[list], mx2: list[list]) -> list[list]:
    n = len(mx1)
    new_matrix = []  # Empty list
    for i in mx1:
        new_matrix.append(i)  # First the first matrix
    for j in mx2:
        new_matrix.append(j)  # Now the second matrix
    return new_matrix


def split(mx: list[list]) -> list[list]:
    if len(mx) == len(mx[0]) and pow_2(len(mx)):
        n = len(mx) // 2
        a = mx[:n]
        b = mx[n:]
        a_11 = [a[i][:n] for i in range(n)]
        a_12 = [a[i][n:] for i in range(n)]
        a_13 = [b[i][:n] for i in range(n)]
        a_14 = [b[i][n:] for i in range(n)]
    return a_11, a_12, a_13, a_14


def strassen(mx1: list[list], mx2: list[list]) -> list[list]:
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
 
print(strassen([[1,2],[3,4]],[[1,2],[3,4]]))

m1=[[5,7,9,10],[2,3,3,8],[8,10,2,3],[3,3,4,8]]
m2=[[3,10,12,18],[12,1,4,9],[9,10,12,2],[3,12,4,10]]

row_wise(strassen(m1,m2))