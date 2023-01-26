from basicmatrices import *
import pickle as p

f1=open("Input.dat", "rb")
f2=open("Inputn.dat", 'rb')

matrix1=[]
matrix2=[]

while True:
    try:
        row=pickle.load(f1)
        matrix1.append(row)
    except EOFError:
        break
while True:
    try:
        row=pickle.load(f2)
        matrix2.append(row)
    except EOFError:
        break

temp_result=strassen(matrix1,matrix2)
result=[]
for i in temp_result:
    result.append(list(map(int,i)))

row_wise(result)