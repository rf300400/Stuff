import numpy as np
import matplotlib.pyplot as plt
import scipy

fs = 8000
fp = 1500
fst = 3000
wp = 2*np.pi*fp/fs
wst = 2*np.pi*fst/fs
print('Pass = ',wp,' stop = ',wst)

orders,wn = scipy.signal.buttord(wp,wst,3,10.0,fs=fs)
print(orders,'\n')
print(wn*fs/(2*np.pi))
b,a = scipy.signal.butter(N = orders, Wn = wn, btype = 'lowpass', analog = False, output = 'ba',fs = 2*np.pi)
#h,w = scipy.signal.freqz(b,a)
order = 1
h = 1 / (1 + 1j * (np.arange(0,4000,1) / fs) ** (2 * orders))
#plt.subplot(2,1,1)
#plt.plot(w*fs/(2*np.pi),20*np.log10(np.abs(h)+(1e-9)))
#plt.subplot(2,1,2)
#plt.plot(w*fs/(2*np.pi),np.unwrap(np.angle(h)))
#plt.show()
plt.subplot(2,1,1)
plt.plot(20*np.log10(np.abs(h)+(1e-9)))
plt.subplot(2,1,2)
plt.plot(np.unwrap(np.angle(h)))
plt.show()
