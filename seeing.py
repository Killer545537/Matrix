import pickle
from basicmatrices import *

f=open("Input.dat", "rb")
f1=open("Inputn.dat", "rb")
matrix1=[]
matrix2=[]
while True:
    try:
        row=pickle.load(f)
        matrix1.append(row)
    except EOFError:
        break
while True:
    try:
        row=pickle.load(f1)
        matrix2.append(row)
    except EOFError:
        break