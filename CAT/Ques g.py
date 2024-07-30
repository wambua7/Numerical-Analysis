import numpy as np

def f(x):
    return x**2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = h/2 * (y[0] + y[-1])
    for i in range(1, n):
        integral += h * y[i]
    return integral

# Define the limits of integration
a = 0
b = 2

# Define the number of subintervals
n = 1000

# Compute the integral using the Trapezoidal Rule
result = trapezoidal_rule(f, a, b, n)

print("Integral of f(x) = x^2 from", a, "to", b, "is approximately", result)

# Compute the exact value of the integral for comparison
exact_result = (b**3 - a**3) / 3
print("Exact value of the integral:", exact_result)