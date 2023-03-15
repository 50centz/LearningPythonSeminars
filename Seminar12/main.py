import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01


def func(x):
    f = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return f

x = np.arange(-limit, limit, step)



plt.plot(x, func(x), 'b-')
plt.grid()
plt.show()

