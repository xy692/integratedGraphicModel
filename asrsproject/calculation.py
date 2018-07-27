import numpy as np


def warehouse_init():
    warehouse_SHELF = {}
    shelfdiv = 3
    shelfCol = 6
    shelfGap = 1
    num=1

    for i in range(1,shelfdiv+1):
        for j in range(1,shelfCol+1):
            if i>1:
                warehouse_SHELF[num] = (i*(shelfGap+2)-2,j)
                num+=1
                warehouse_SHELF[num] = (i*(shelfGap+2)-1,j)
                num+=1
            else:
                warehouse_SHELF[num] = (i,j)
                num+=1
                warehouse_SHELF[num] = (i+1,j)
                num+=1
    return warehouse_SHELF, num

shelfsloc={}
shelfscontainer={}
num=0
[shelfsloc,num]=warehouse_init()

for i in range(1,num):
    shelfscontainer[i]=0

print(shelfscontainer)
print(shelfsloc)

