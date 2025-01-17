"""
=================================
hexbin(x, y, [C], [gridsize],...)
=================================
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('mpl_plot_gallery')

# make data: correlated + noise
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000)/3

# plot:
fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)

ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)

plt.show()
