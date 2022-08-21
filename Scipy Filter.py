#Forward-backward filter

from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal
from matplotlib import style
from numpy import sin,cos,pi,linspace
from numpy import random

t = linspace(-1,1.0,201)
x1 = sin(2*pi*0.75*t)
x2 = 1+0.1*sin(2*pi*1.25*t)
x=x1+x2+random.randn(len(t))*0.01
#125Hz cutoff frequency
b,a = signal.butter(3,0.05)
filtered_signal1 = signal.filtfilt(b,a,x,padlen=150)
filtered_signal2 = signal.lfilter(b,a,x)

plt.figure(1)
plt.plot(t,x,'b')
plt.plot(t,filtered_signal1,'r')
plt.plot(t,filtered_signal2,'k')
plt.show()
