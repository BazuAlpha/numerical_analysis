from scipy.integrate import quad

def integrand(x):
    return x**4 - x - 2

result, error = quad(integrand, 1, 3)
print(result)