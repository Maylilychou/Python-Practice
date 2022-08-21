#Convolution function
from matplotlib import pyplot as plt
import mysignals as sigs
from matplotlib import style
from scipy import signal
import csv
import numpy as np

csvfile = "test_conv"
def convZDM(x,y):
    z=[None]*(len(x)+len(y))
    for i in range(len(x)+len(y)):
        z[i]=0

    for i in range(len(x)):
        for k in range(len(y)):
            z[i+k] = z[i+k]+x[i]*y[k]

    with open(csvfile,"w") as output:
        writer = csv.writer(output,lineterminator ='.')
        for i in z:
            writer.writerow([i])

    return z

    
# Convolution
x=sigs.InputSignal_1kHz_15kHz
y = np.array([1,1,0])
z=convZDM(sigs.InputSignal_1kHz_15kHz,y)

# Deconvolution
deconv,remainder = signal.deconvolve(z,y)

style.use('ggplot')
f,plt_arr = plt.subplots(2,2)
f.suptitle("Input signal and output")
plt_arr[0,0].plot(x,color='red')
plt_arr[0,0].set_title("Input Signal")
plt_arr[0,1].plot(y,color='blue')
plt_arr[0,1].set_title("Impulse Response")
plt_arr[1,0].plot(z,color='black')
plt_arr[1,0].set_title("Output Signal")
plt_arr[1,1].plot(deconv,color='red')
plt_arr[1,1].set_title("Deconvoled Signal")
plt.show()
