import numpy as np

def f(x, y):
    return x**4 - 3*x**3 + x*y + x - y + 1

def gradient_descent(x0, y0, learning_rate, max_iter):
    x = x0
    y = y0
    for i in range(max_iter):
        # Compute the gradient of f at (x, y)
        grad_x = 4*x**3 - 9*x**2 + y + 1
        grad_y = x - 1
        # Update x and y using the gradient descent update rule
        x -= learning_rate * grad_x
        y -= learning_rate * grad_y
        # Print the current values of x and y
        print(f"Iteration {i+1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {f(x, y):.4f}")
    return x, y

# Initial guesses
x0 = 0
y0 = 0
learning_rate = 0.1
max_iter = 100

# Run the gradient descent algorithm
x_min, y_min = gradient_descent(x0, y0, learning_rate, max_iter)

print(f"Minimum value of f(x, y) = {f(x_min, y_min):.4f} at x = {x_min:.4f}, y = {y_min:.4f}")