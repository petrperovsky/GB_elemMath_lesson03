"""Графики окружности, эллипса, гиперболы"""

import numpy as np
import matplotlib.pyplot as plt
import decimal

'''круг'''
circle = plt.Circle((0, 0), 4, fill=False)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.grid(True)
plt.show()

"""эллипс"""
t = np.linspace(0, 2 * np.pi, 100)
plt.plot(4 * np.cos(t), np.sin(t))
plt.grid(True)
plt.show()

"""гипербола"""
xmin = -20
xmax = 20
dx = 0.1
xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)
ylist = 1 / xlist
plt.plot(xlist, ylist)
plt.grid(True)
plt.show()

