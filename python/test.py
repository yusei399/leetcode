import numpy as np
import matplotlib.pyplot as plt
import math
import commpy as cp 
from scipy import signal 
def main():
    fs = 8000 # sampling frequency 
    fc = 440  # carrier frequency 
    fb = 100   # data rate
    duration = 10  # total duration 
    t = np.arange(0,duration-1/fs,1/fs) # time generation 
    f = np.arange(1/duration,fs, 1/duration) # frequency axis generation
    a1 = baseband(fs, fb, duration)  # baseband signal generation
    y = a1*np.sin(2*math.pi*fc*t) # signal generation
    fy = np.fft.fft(y)/fs/duration # FFT to generate frequency domain signal
    fig,axs = plt.subplots(2)  # generate figure for frequency and time domain signals. 
    axs[0].plot(f,abs(fy), lw=0.5)
    axs[0].set_yscale('log')
    axs[0].set_xlabel("frequency(Hz)")
    axs[0].set_ylabel("amplitude")
    axs[0].set_ylim([0.00001,1])
    axs[0].set_xlim([0,1000])
    axs[1] = plt.subplot(2,1,2)
    axs[1].plot(t[0:10000], y[0:10000],lw=0.5)
    axs[1].set_xlabel("time (second)")
    axs[1].set_ylabel("amplitude")
    plt.show()
def baseband(fs, fb, duration):
    a = np.arange(fs*duration-1)
    v = np.random.randint(0,2)
    count = 0
    pb = fs/fb
    filter = False
    os = fs/fb 
    sd = 1/fb
    for i in range(fs*duration-1):
        if (count==pb):
          count=1
          a[i] = v
          v = np.random.randint(0,2)
        else:
          count = count + 1
          a[i] = v
    if filter:
        n = 101
        time_idx, h = cp.rcosfilter(n, 1.0, 1/fb, fs)
        a = signal.lfilter(h, 1, a) 
    return a
if __name__ == '__main__':
    main()
