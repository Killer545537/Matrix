import pickle
from typing import *

f=open("new.dat", "wb")

matrix=[[1,2,3],[4,5,6]]
def writing(filename:BinaryIO,mx1:list[list])-> None:
    f=open(filename,"wb")
    for i in mx1:
        pickle.dump(i,filename)
    f.close()

writing("new.dat", matrix)
