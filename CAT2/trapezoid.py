import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**7 - x - 3


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


a = 1
b = 2 
n = 3
 


result = trapezoidal_rule(f, a, b, n)
print(f'Estimated integral using trapezoidal rule: {result}')


x = np.linspace(a, b, 1000)
y = f(x)
x_trapezoids = np.linspace(a, b, n+1)
y_trapezoids = f(x_trapezoids)

plt.plot(x, y, label='f(x)')
plt.fill_between(x_trapezoids, y_trapezoids, alpha=0.4, step='mid', label='Trapezoids')
plt.scatter(x_trapezoids, y_trapezoids, color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoidal Rule of Integration')
plt.legend()
plt.show()