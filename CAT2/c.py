def linear_interpolation(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)


x0 = 2.00
y0 = 7.2
x1 = 4.25
y1 = 7.1


x = 4.0


y = linear_interpolation(x0, y0, x1, y1, x)
print(f'The value of y at x = {x} is {y}')