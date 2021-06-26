"""3х-мерный график 2х параллельных плоскостей"""
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X, Y = np.meshgrid((np.arange(-5, 5, 0.5)), (np.arange(-5, 5, 0.5)))
Z1 = X + 3 * Y + 200
Z2 = X + 3 * Y
ax.plot_wireframe(X, Y, Z1, linestyle='--', linewidth=1)
ax.plot_wireframe(X, Y, Z2, colors='blue')
ax.scatter(0, 0, 0, 'z', 50, 'red', label='0; 0')

show()

"""3х-мерный график двух любых поверхностей 2го порядка"""
fig = figure(figsize = (18, 18))
ax = Axes3D(fig)
a, b = 2, 7
X, Y = np.meshgrid((np.arange(-5, 5, 0.5)), (np.arange(-5, 5, 0.5)))
Z1 = b ** 2 + (b ** 2 * (X ** 2 / a ** 2))
Z2 = -(b ** 2 + (b ** 2 * (X ** 2 / a ** 2)))
ax.plot_surface(X, Y, Z1,  linewidth=1, color='blue')
ax.plot_surface(X, Y, Z2,  linewidth=1, color='green')

show()