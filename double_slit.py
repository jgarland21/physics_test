import numpy as np
import matplotlib.pyplot as plt

#test values
#l = 700 * (10**(-9))
#d = 20 * (10**(-6))
#a = 5 * (10**(-6))

#init values
l = float(input("Wavelength (nm): ")) * (10**(-9))
d = float(input("Distance between slits (um): ")) * (10**(-6))
a = float(input("Slit width (um): ")) * (10**(-6))
I0 = float(input("Intensity: "))

#create empty value array
IVals = np.zeros([1920])

#calculate intensity (step of 1/16)
for theta in range(-960, 960):
    #convert to radians and scale from 1920 -> 60
    t = np.radians(theta/16)
    I = I0 * ((np.sin(np.pi * a/l * np.sin(t))/(np.pi * a/l * np.sin(t)))**2) * ((np.cos(np.pi * d/l * np.sin(t)))**2)
    #place points in correct index
    IVals[theta-960] = I

#plot setup
plt.margins(x=0.001) #this is weird
plt.xlabel(r"$\theta$")
plt.ylabel("Intensity")
plt.xticks(np.arange(-90, 90, 15))
xRange = np.arange(-60, 60, 1/16)

#plot intensity vs theta
plt.plot(xRange, IVals)
plt.show()
