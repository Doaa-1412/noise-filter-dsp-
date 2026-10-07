import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs=1000
t=np.linspace(0,1,fs)
clean_signal=np.sin(2*np.pi*50*t)

noise=np.random.normal(0,0.5,clean_signal.shape)
noisy_signal=clean_signal+noise

b,a=signal.butter(4,100,btype='low',fs=fs)
filtered_signal=signal.filtfilt(b,a,noisy_signal)

plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(t,clean_signal)
plt.title('Clean Signal')

plt.subplot(3,1,2)
plt.plot(t,noisy_signal,color='red')
plt.title('Noisy Signal')

plt.subplot(3,1,3)
plt.plot(t,filtered_signal,color='green')
plt.title('Filtered Signal')

plt.tight_layout()
plt.show()
