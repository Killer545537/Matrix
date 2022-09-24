import pickle
from basicmatrices import *

f=open("new.dat", "rb")

empty=[]
while True:
    try:
        row=pickle.load(f)
        print(row)
        empty.append(row)
    except EOFError:
        break