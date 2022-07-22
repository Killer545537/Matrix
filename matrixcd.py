#matrixcd.py
num=0
result=[]
def matrixc1():
    '''create a matrix A '''
    import pickle
    file1=open("matrix1.dat","wb")
    global num
    num=int(input('Enter no. of rows:'))
    global A
    A=[]
    for i in range(num):
        print('Enter row',i+1,':',end='')
        row=eval(input())
        A.append(row)
    pickle.dump(A,file1)
    print('matrix created as A')
    file1.close()
def matrixc2():
    '''create a matrix B '''
    import pickle
    file1=open("matrix2.dat","wb")
    global B
    B=[]
    for i in range(num):
        print('Enter row',i+1,':',end='')
        row=eval(input())
        B.append(row)
    pickle.dump(B,file1)
    print('matrix created!!')
    file1.close()    
def matrixd1():
    '''display a matrix'''
    import pickle
    file1=open("matrix1.dat","rb")
    try:
        while True:
            data=pickle.load(file1)
            l=len(data)
            for i in range(l):
                if i==0:
                    print(data[i])
                else:
                    print(' ',data[i])
    except EOFError:
        file1.close()
def matrixd2():
    '''display a matrix'''
    import pickle
    file1=open("matrix2.dat","rb")
    try:
        while True:
            data=pickle.load(file1)
            l=len(data)
            print('B=',end='')
            for i in range(l):
                if i==0:
                    print(data[i])
                else:
                    print(' ',data[i])
    except EOFError:
        file1.close()    
        
def matrixadd():
    '''Addition of two matrices'''
    global result 
    if num==2:
        result=[[0,0],
                [0,0]]
    else:
        result = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]  
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    print('A+B=',result[0])
    for i in range(1,num):
        print('  ',' ',result[i])
def matrixtranspose():
    '''Transpose of matrix'''
    if num==2:
        resultA=[[0,0],
                [0,0]]
        resultB=[[0,0],
                [0,0]]
    else:
        resultA = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        resultB = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            resultA[j][i] = A[i][j]
    print('The transpose of matrix A is:')
    for r in resultA:
        print(r) 
    for i in range(len(B)):
        for j in range(len(B[0])):
            resultB[j][i] = B[i][j]
    print('The transpose of matrix B is:')
    for r in resultB:
        print(r)  
        

         
    
        
        
    
    
               
    
  