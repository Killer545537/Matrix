import pickle

f=open("new.dat", "wb")

matrix=[[1,2,3],[3,4,5],[6,7,8]]

for i in matrix:
    pickle.dump(i,f)

f.close()