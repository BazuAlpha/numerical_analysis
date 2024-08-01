import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x_data = np.array([4.00, 6.25, 7.25, 9.81, 11.20, 12.60])
y_data = np.array([7.2, 7.1, 4.0, 3.0, 1.5, 6.0])


cs = CubicSpline(x_data, y_data)


x_new = np.linspace(2, 10.6, 100)
y_new = cs(x_new)


plt.scatter(x_data, y_data, label='Data')
plt.plot(x_new, y_new, label='Cubic Spline', color='red')
plt.legend()
plt.show()