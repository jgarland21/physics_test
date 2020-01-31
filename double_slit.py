import numpy as np
import matplotlib.pyplot as plt

#init values
l = float(input("Wavelength (nm): ")) * (10**(-9))
#D = 10
d = float(input("Distance between slits (um): ")) * (10**(-6))
a = float(input("Slit width (um): ")) * (10**(-6))
I0 = 1
#create empty value array
IVals = np.zeros([1440])

#def intensity(t):
#    I = 4 * I0 * ((np.sin(np.pi * a/l * np.sin(t))/(np.pi * a/l * np.sin(t)))**2) * (np.cos(np.pi * d/l * np.sin(t)))**2
#    return I

#calculate intensity (step of 0.25)
for theta in range(1440):
    #convert to radians and scale from 1440 -> 360
    t = np.radians(theta/4)
    print(theta, t)
    I = 4 * I0 * ((np.sin(np.pi * a/l * np.sin(t))/(np.pi * a/l * np.sin(t)))**2) * ((np.cos(np.pi * d/l * np.sin(t)))**2)
    #print(I)
    IVals[theta] = I

#print(IVals)

#plot intensity vs theta
plt.xlim(360,1080)
plt.plot(IVals)
plt.show()
