import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([4, 6, 7, 8, 10])

 
x_data = x_data.reshape(-1, 1)


model = LinearRegression()


model.fit(x_data, y_data)


slope = model.coef_[0]
intercept = model.intercept_

print(f'Slope (coefficient): {slope}')
print(f'Intercept: {intercept}')


y_pred = model.predict(x_data)


plt.scatter(x_data, y_data, color='blue', label='Data points')


plt.plot(x_data, y_pred, color='red', label='Fitted line')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()