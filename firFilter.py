from matplotlib import pyplot as plt
from scipy import signal
from matplotlib import style
import numpy as np



# generate signals with fs=2000Hz, nyquist frquency=1000

t=np.linspace(0,1.0,2001)
sig_5Hz = np.sin(2*np.pi*5*t)
sig_50Hz = np.sin(2*np.pi*50*t)
sig_250Hz = np.sin(2*np.pi*250*t)
sigComb = sig_5Hz+sig_50Hz+sig_250Hz

numTaps = 101
lpf_cutoff = 7
hpf_cutoff = 100
bpf_cutoff1 = 40
bpf_cutoff2 = 100

#lowpass
lowpass_coef = signal.firwin(numTaps,lpf_cutoff,nyq=1000)
lpf_output = signal.convolve(sigComb,lowpass_coef,mode='same')


highpass_coef = signal.firwin(numTaps,hpf_cutoff,pass_zero=False,nyq=1000)
hpf_output = signal.convolve(sigComb,highpass_coef,mode='same')

bandpass_coef = signal.firwin(numTaps,[bpf_cutoff1,bpf_cutoff2],pass_zero=False,nyq=1000)
bpf_output = signal.convolve(sigComb,bandpass_coef,mode='same')

f,plt_arr = plt.subplots(2,2,sharex=True,sharey=True)
plt_arr[0,0].plot(sigComb,color='red')
plt_arr[0,1].plot(lpf_output,color='blue')
plt_arr[1,0].plot(hpf_output,color='green')
plt_arr[1,1].plot(bpf_output,color='black')

plt.show()

