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

#set range to 5 minima (in radians) with step of 0.01 rad
thetaRange = 5 * l/a
t = np.arange(-thetaRange, thetaRange, 0.0001)

#calculate intensities
Idi = I0 * ((np.sin(np.pi * a/l * np.sin(t))/(np.pi * a/l * np.sin(t)))**2) * ((np.cos(np.pi * d/l * np.sin(t)))**2)
Id = I0 * ((np.sin(np.pi * a/l * np.sin(t))/(np.pi * a/l * np.sin(t)))**2)
Ii = I0 * ((np.cos(np.pi * d/l * np.sin(t)))**2)

#plot setup
plt.margins(x=0, y=0)
plt.ylim(-0.01, 1.01)
plt.title("Double Slit Intensity")
plt.xlabel(r"$\theta$ (Degrees)")
plt.ylabel("Intensity")

#plot intensities vs theta (in degrees)
plt.plot(np.degrees(t), Ii, ":", color="royalblue", label="Inteference", alpha=0.7)
plt.plot(np.degrees(t), Id, "--", color="indigo", label="Diffraction", alpha=0.7)
plt.plot(np.degrees(t), Idi, "", color="crimson", label="Inteference & Diffraction")

plt.legend(loc=1)

plt.show()
