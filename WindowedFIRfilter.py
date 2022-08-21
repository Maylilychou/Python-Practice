#Apply Different Windowed FIR filter
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
from numpy import arange, cos, sin, pi, absolute
from scipy.fftpack import fft,fftshift

#create signals

sampling_rate = 100
nsamples = 400

t = arange(nsamples)/sampling_rate
x1=cos(2*pi*0.5*t)+0.2*sin(2*pi*2.5*t+0.1)
x2=0.2*sin(2*pi*15.3*t)+0.1*sin(2*pi*16.7*t+0.1)
x3=0.1*sin(2*pi*23.45*t+0.8)

x=x1+x2+x3

#get different window functions
window1 = signal.get_window(('kaiser',4.0),30.0)

window3 = signal.barthann(51)

#create FIR filter
nyq_rate = sampling_rate/2.0
width = 5.0/nyq_rate
ripple_db=60.0

N,beta = signal.kaiserord(ripple_db,width)
fc_hz = 10.0

taps = signal.firwin(N,fc_hz/nyq_rate,window=('kaiser',beta))
filtered_x = signal.lfilter(taps,1.0,x)

plt.figure(1)
plt.plot(taps,'bo-',linewidth=2)
plt.title('Kaiser Filter (%d taps)'%N)
plt.grid()

plt.figure(2)
w,h = signal.freqz(taps,worN=8000)
plt.plot(w*nyq_rate/pi,absolute(h),color='b')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Magnitude')
plt.grid()

#insert window plot in the current plot
ax1=plt.axes([0.42,0.6,0.45,0.25])
plt.plot(w*nyq_rate/pi,absolute(h),color='r')
plt.xlim(0,8)
plt.ylim(0.9985,1.001)


delay = 0.5*(N-1)/sampling_rate
plt.figure(3)
plt.plot(t,x,'r')
plt.plot(t-delay,filtered_x,'b')
plt.plot(t[N-1:]-delay,filtered_x[N-1:],'g')

print(filtered_x)

plt.show()
                            
                    

