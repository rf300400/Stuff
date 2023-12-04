import numpy as np
x1n = [[2],[1],[2],[1]]
x2n = [1,2,3,4]
matty = np.zeros((len(x2n),len(x2n)))

i = 0
j = 0
ptr = 0

while i < len(x2n):
    j = 0
    while j < len(x2n):
        matty[j,i] = x2n[ptr]
        if(ptr + 1 == 4):
            ptr = 0
        else:
            ptr = ptr + 1
        j = j + 1
    ptr = ptr + 1
    i = i + 1
finans = np.matmul(matty,x1n)
finans = np.transpose(finans)
print(matty)
print(finans)
