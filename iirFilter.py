from matplotlib import pyplot as plt
from scipy import signal
from matplotlib import style
import numpy as np

#Design IIR filte

def butter_bandpass(lowcut,highcut,fs,order=5):
    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq
    b,a = signal.butter(order,[low,high],'band')
    return b,a

def butter_bandpass_filter(data,lowcut,highcut,fs,order=5):
    b,a = butter_bandpass(lowcut,highcut,fs,order=order)
    y=signal.lfilter(b,a,data)
    return y

def run():
    fs=5000
    lowcut=500
    highcut=1200
    plt.figure(1)
    for n in [3,5,6,9]:
        b,a=butter_bandpass(lowcut,highcut,fs,n)
        w,h = signal.freqz(b,a,worN=2000)
        plt.plot((fs*0.5/np.pi)*w,abs(h),label='order=%d'%n)

    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Gain')
    plt.legend(loc='best')
    plt.show()

    #Test filter
    T=0.1
    nsamples = int(T*fs)
    a=0.02
    f0=600
    t=np.linspace(0.0,T,nsamples)

    x1 =0.1*np.sin(2*np.pi*1.2*np.sqrt(t))
    x2 =0.01*np.cos(2*np.pi*312*t+0.1)
    x3 =0.02*np.cos(2*np.pi*f0*t+0.11)
    x4 =0.03*np.sin(2*np.pi*2000*t)

    x=x1+x2+x3+x4
    plt.figure(2)
    plt.plot(t,x,label='noisy signal')
    y = butter_bandpass_filter(x,lowcut,highcut,fs,order=6)
    plt.plot(t,y,label='filtered signal')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Amplitude')
    plt.legend(loc='best')
    plt.show()
    

run()



