import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
import math

def calc_DFT(x):
    yReal = [None]*int((len(x)/2))
    yImag = [None]*int((len(x)/2))
    yMag  =  [None]*int((len(x)/2))
    for i in range(len(yReal)):
        yReal[i]=0
        yImag[i]=0

    for k in range(len(yReal)):
        for i in range(len(x)):
            yReal[k] = yReal[k]+ x[i]*math.cos(2*math.pi*k*i/len(x))
            yImag[k] = yImag[k]- x[i]*math.sin(2*math.pi*k*i/len(x))

    for k in range(len(yMag)):
        yMag[k] = math.sqrt(yReal[k]**2+yImag[k]**2)

    return yReal,yImag,yMag


def calc_IDFT(yReal,yImag):
    x = [None]*len(yReal)*2
    for i in range(len(x)):
        x[i]=0

    for i in range(len(x)):
        for k in range(len(yReal)):
            x[i] = x[i]+yReal[k]*math.cos(2*math.pi*k*i/len(x))+yImag[k]*math.sin(2*math.pi*k*i/len(x))

    return x

def plot_signals(x,yReal,yImag,yMag,xHat):
    style.use('ggplot')
    f,plt_arr = plt.subplots(5,sharex=True)
    f.suptitle('DFT')
    plt_arr[0].plot(x,color='red')
    plt_arr[0].set_title('Input')
    plt_arr[1].plot(yReal,color='blue')
    plt_arr[1].set_title('Real DFT',color='blue')
    plt_arr[2].plot(yImag,color='yellow')
    plt_arr[2].set_title('Imag DFT',color='yellow')
    plt_arr[3].plot(yMag,color='black')
    plt_arr[3].set_title('Magnitude DFT',color='black')
    plt_arr[4].plot(xHat,color='cyan')
    plt_arr[4].set_title('IDFT',color='cyan')
    plt.show()

[yReal,yImag,yMag] = calc_DFT(sigs.ecg_signal)
xHat = calc_IDFT(yReal,yImag)
plot_signals(sigs.ecg_signal,yReal,yImag,yMag,xHat)
            
    
