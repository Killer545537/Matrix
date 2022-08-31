def Matrix_Difference(matrix1,matrix2):
    #The program is matrix1-matrix2, since subtraction is not commutative
    matrix2_new=null(len(matrix2),len(matrix2[0]))
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            matrix2_new[i][j]=-matrix2[i][j] #From the definition of the negative of a matrix
    return(Matrix_Sum(matrix1,matrix2_new))#From the definition of difference of two matrices