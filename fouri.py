import numpy as np
import matplotlib.pyplot as plt
import scipy

n = np.arange(0,160,1)
xn = np.sin(np.pi*n/40) + (0.6*np.cos(3*np.pi*n/40)) + (0.4*np.sin(9*np.pi*n/40))
xf = scipy.fft.fft(xn)
xfn = scipy.fft.ifft(xf)
plt.subplot(3,1,1)
plt.plot(xn)
plt.subplot(3,1,2)
plt.plot(10*np.log10(np.abs(xf)))
plt.subplot(3,1,3)
plt.plot(np.real(xfn))
plt.tight_layout()
plt.show()
