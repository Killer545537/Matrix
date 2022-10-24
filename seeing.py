import pickle
from basicmatrices import *

f = open("new.dat", "rb")

empty = []
while True:
    try:
        row = pickle.load(f)
        print(row)
        empty.append(row)
    except EOFError:  # As Python raises an exception if we try to read after the file is over
        break
