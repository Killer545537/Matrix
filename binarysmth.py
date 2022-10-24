import pickle

f=open("new.dat", "wb")

matrix=[[1,2,3],[3,10,5],[6,7,8]]
with open("new.dat", "wb+"):
    for i in matrix:
        pickle.dump(i,f)


