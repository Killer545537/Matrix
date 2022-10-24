from typing import *

from basicmatrices import *

def cyclic(pts:list[list])->bool:
    if Determinant(pts)==0:
        return True
    else:
        return False

id=[[1,1],[-6,0],[-2,2],[-2,8]]
for i in id:
    i.insert(0,(i[0]**2+i[1]**2))


row_wise(id)

id_new=joining_horizontally(id,null(4,1))


