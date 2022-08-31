def null(rows,columns):
    null_matrix=[[0 for i in range(columns)] for i in range(rows)] #loop over columns then over rows
    return null_matrix

def row_wise(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end="\t")
        print("\n")

def Matrix_Sum(matrix1,matrix2):
    if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]): #Checking for compatibility for addition
        rows, columns=len(matrix1), len(matrix1[0])
        sum_matrix=null(rows,columns)
        for i in range(rows):
            for j in range(columns):
                sum_matrix[i][j]+=matrix1[i][j]+matrix2[i][j]
        return sum_matrix
    else:
        return -1

def Matrix_Difference(matrix1,matrix2):
    #The program is matrix1-matrix2, since subtraction is not commutative
    matrix2_new=null(len(matrix2),len(matrix2[0]))
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            matrix2_new[i][j]=-matrix2[i][j] #From the definition of the negative of a matrix
    return(Matrix_Sum(matrix1,matrix2_new))#From the definition of difference of two matrices
    


A=[[1,2,3],[4,5,6],[1,1,1]]
B=[[1,2,3],[4,5,6],[2,2,2]]
print(Matrix_Difference(A,B))



