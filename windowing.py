import numpy as np
import matplotlib.pyplot as plt
import scipy as scip

fs = 8000
fp = 1850/fs
fs = 2150/fs
wc = 2*np.pi*(fs+fp)/(2*fs)

n = np.linspace(0,2*np.pi,27)
hn = (wc/np.pi)*np.sinc(wc*n/np.pi)
hw = scip.signal.firwin(27,2000,300,window='boxcar',pass_zero=True,fs=8000)
#hreq = np.convolve(hn,hw)
w , h = scip.signal.freqz(hw)
plt.subplot(3,1,1)
plt.stem((wc/np.pi)*np.sinc(wc*(np.linspace(-2*np.pi,2*np.pi,(27*2)+1))/np.pi))
plt.subplot(3,1,2)
plt.plot(w,20*np.log10(np.abs(h)))
plt.subplot(3,1,3)
plt.plot(w,np.unwrap(np.angle(h)))
plt.show()
