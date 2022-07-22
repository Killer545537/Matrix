def lower_triangular(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    lower_matrix=null(rows,columns) #null matrix
    for i in range(rows):
        for j in range(columns):
            if j>=i: #Condition for a null
                lower_matrix[i][j]+=matrix[i][j]
            else:
                continue
    return lower_matrix
