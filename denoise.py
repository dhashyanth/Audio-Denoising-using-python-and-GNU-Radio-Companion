# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:09:44 2022

@author: Greeshma
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sn


def downsampling(x,n):
    arr=[]
    for i in range(0,len(x),n):
        arr.append(x[i])
    return arr

def upsampling(x,n):
    arr = []
    temp = 0
    for i in range(0,n*len(x)):
        if i%n==0:
            arr.append(x[temp])
            temp =temp+1
        else:
            arr.append(0)
            
    return arr
 
#sound file read
[audio, Fs]=sn.read("D:/CCE/SEM_6/19CCE450(WAVELETS AND ITS APPLICATIONS/TERM_PROJECT(AUDIO DENOISING)/under.wav")
plt.plot(audio)
plt.title('Original Sound File')

print(Fs)
h = [1,1]
h1 = [1,1]
g = [0,0]
g1 = [0,0]
temp = 0
amp = int(input("enter the amplitude of the noise: "))
y = np.random.normal(0,0.2,np.size(audio)); # Additive Wired Gaussian Noise 
audio = list(audio)
y = y*amp
audio = np.add(audio, y)
print(audio)
sd.play(audio,Fs)
plt.plot(audio)
plt.title("time domain plotos initial noise audio")
plt.show()
dft = np.fft.fft(audio)#frequency domain of noised signal
plt.plot(dft)
plt.title("frequency domain of initial signal")
plt.show()

temp = 0
for i in range(len(h)):
    temp = temp + h[i]**2
    
temp = temp**0.5

for i in range(len(h)):
    h[i] = h[i]/temp
    
temp1 = 0
for i in range(len(h1)):
    temp1 = temp1 + h1[i]**2
    
temp1 = temp1**0.5

for i in range(len(h1)):
    h1[i] = h1[i]/temp1
    
temp2 = 0
for i in range(len(g)):
    temp2 = temp2 + g[i]**2
    
temp2 = temp2**0.5

for i in range(len(g)):
    g[i] = g[i]
    

temp3 = 0
for i in range(len(g1)):
    temp3 = temp3 + g1[i]**2
    
temp3 = temp3**0.5

for i in range(len(g1)):
    g1[i] = g1[i]
    
x = list(audio)
n = int(input("enter the level of decomposition: "))
for i in range(n): 
    convolution_arr = np.convolve(x,h)
    downsampling_arr = downsampling(convolution_arr , 2)
    upsampling_arr = upsampling(downsampling_arr , 2)
    convolution_arr = np.convolve(upsampling_arr,h1)

    convolution1_arr = np.convolve(x,g)
    downsampling_arr = downsampling(convolution1_arr , 2)
    upsampling_arr = upsampling(downsampling_arr , 2)
    convolution1_arr = np.convolve(upsampling_arr,g1)
    x = convolution_arr + convolution1_arr

print(x)

sd.play(x,Fs)
plt.plot(x)
plt.title("plot os denoised audio")
plt.show()

dft2 = np.fft.fft(x) # dft of denoised signal
plt.plot(dft2)
plt.title("frequency domain of denoised signal")
plt.show()


