import sympy as sp
x = sp.symbols('x')
f = x**7 - x - 11
df = sp.diff(f, x)
print(df)