def null(rows,columns):
    null_matrix=[[0 for i in range(columns)] for i in range(rows)] #loop over columns then over rows
    return null_matrix

def row_wise(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end="\t")
        print("\n")

def transpose(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    transpose_matrix=null(columns, rows) #null matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i]+=matrix[i][j] #definition of transpose

    return transpose_matrix

A=[[1,2,3],[4,5,6],[1,1,1]]
print(transpose(A))


