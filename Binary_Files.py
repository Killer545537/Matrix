import pickle
import typing

f1=open("binary1.dat", "ab+")

matrix=[[1,2,3],[4,5,6]]

def writing(mx:list[list])-> None:
    for i in mx:
        pickle.dump(i,f1)

def view()-> list[list]:
    empty=[]
    while True:
        try:
            row=pickle.load(f1)
            empty.append(row)
        except EOFError:
            break
    return empty

writing(matrix)

print(pickle.load(f1))
