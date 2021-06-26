"""exp(x) + x∙(1 – y) = 1
   y = x2 – 1"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 100)
plt.figure()
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('scaled')
plt.show()

from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, np.exp(x) + x * (1 - y) - 1)

x1, y1 = fsolve(equations, (2, 5))
x2, y2 = fsolve(equations, (-2, 1))
print(x1, y1)
print(x2, y2)

"""y = x2 – 1
   exp(x) + x∙(1 – y)  - 1 > 0"""


