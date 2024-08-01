import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data = np.array([1, 3, 5, 7, 9])
y_data = np.array([1, 5, 7, 9, 10])


def model(x, a, b):
    return a * x + b


params, covariance = curve_fit(model, x_data, y_data)
a, b = params


plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, a, b), label='Fit', color='red')
plt.legend()
plt.show()