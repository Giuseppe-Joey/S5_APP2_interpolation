




import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import UnivariateSpline


# creating a figure for the original example from scipy documentation
plt.figure()
plt.title("Original Example")

rng = np.random.default_rng()
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)
plt.plot(x, y, 'ro', ms=5)

#Use the default value for the smoothing parameter:
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)

#Manually change the amount of smoothing:
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw=3)


plt.xlabel("Distance in Meters (m)")
plt.ylabel("Height in Meters (m)")
plt.legend()
plt.show()










# creating a figure for the S5APP2 problematique
plt.figure()
plt.title("--- S5-APP2 Problematique Interpolation ---")


exit_y_position = 10
x, y = np.array([0, 5, 8, 15, 20, 25]), np.array([30, 19, 19.8, 20, 16, exit_y_position])
plt.plot(x, y, 'ro', ms=5)

#Use the default value for the smoothing parameter:
spl = UnivariateSpline(x, y)
xs = np.linspace(0, 25, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)

#Manually change the amount of smoothing:
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw=3)


plt.xlabel("Distance in Meters (m)")
plt.ylabel("Height in Meters (m)")
plt.legend()
plt.show()













# creating a figure for the S5APP2 smoothing the friction coeficients
plt.figure()
plt.title("--- S5-APP2 Friction Factor Interpolation ---")


x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([0.87, 0.78, 0.71, 0.61, 0.62, 0.51, 0.51, 0.49, 0.46, 0.48, 0.46])
plt.plot(x, y, 'ro', ms=5)

#Use the default value for the smoothing parameter:
spl = UnivariateSpline(x, y)
xs = np.linspace(0, 100, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)

#Manually change the amount of smoothing:
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw=3)


plt.xlabel("Ouverture Valve en %")
plt.ylabel("Coeficient")
plt.legend()
plt.show()

