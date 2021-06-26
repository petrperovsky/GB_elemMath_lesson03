'''полярные координаты в декартовы'''

import math


def polartodecart(r, phi):
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return x, y


polartodecart(2, 15)

"""график окружности в полярных координатах"""

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 2, 1 / 180) * np.pi
plt.polar(X, [10] * len(X))
plt.show()

"""график отрезка прямой линии в полярных координатах"""

X = np.arange(2, 8, 1)
print(X)
Y = np.arange(2, 8, 1)
print(Y)
plt.polar(X, Y)
plt.show()
