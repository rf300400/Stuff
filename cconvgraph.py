import numpy as np
import matplotlib.pyplot as plt
import scipy as scp

def getCC(x1n,x2n):
    matty = np.zeros((len(x),len(x)))
    i = 0
    j = 0
    ptr = 0
    x2n = np.append(x2n,np.zeros(len(x1n)-len(x2n)))
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
    return finans


L = 21
f1 = 200
fs = 8000
F1 = f1/fs
t = np.linspace(0,0.05,fs)
x1n = np.sin(2*np.pi*f1*t)
x2n = 1*np.random.rand(len(x1n))
x = x1n + x2n
h = np.ones(L)/L
y = np.convolve(x,h)
plt.subplot(3,1,1)
plt.plot(x)
plt.subplot(3,1,2)
plt.plot(h)
plt.subplot(3,1,3)
plt.plot(y)
plt.show()
