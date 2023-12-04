import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scip
a = 0.1
nume = np.array([(1+(a*a)),0,(1+(a*a))])
deno = np.array([2,0,(2*a*a)])
z,p,k = scip.tf2zpk(nume,deno)
w,h = scip.freqz_zpk(z,p,k)
plt.subplot(3,1,1)
plt.plot(w,(20*np.log10(np.abs(h))))
plt.xlabel("w")
plt.ylabel("h(w) in dB")
plt.subplot(3,1,2)
plt.plot(w,np.real(20*np.log10(np.abs(h))))
plt.xlabel("w")
plt.ylabel("Magnitude in dB")
plt.subplot(3,1,3)
plt.plot(w,np.unwrap(np.angle(h)))
plt.xlabel("w")
plt.ylabel("Phase shift in Radian")
plt.tight_layout()
plt.show()

fs = 10000
nume,deno = scip.iirnotch(50/fs,1,fs)
print(nume,' ',deno)
f1 = 300/fs
f2 = 50/fs
t= np.arange(0,1000,(1/fs))
xn = (3*np.sin(2*np.pi*f1*t)) + np.sin(2*np.pi*f2*t)
yn = scip.lfilter(nume,deno,xn)
plt.subplot(2,1,1)
plt.plot(t,xn)
plt.subplot(2,1,2)
plt.plot(t,yn)
plt.show()
