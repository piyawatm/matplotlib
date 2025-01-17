"""
========================
barbs([X, Y], U, V, ...)
========================
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('mpl_plot_gallery')

# make data:
np.random.seed(1)
X = [[2, 4, 6]]
Y = [[1.5, 3, 2]]
U = -np.ones((1, 3)) * 0
V = -np.ones((1, 3)) * np.linspace(50, 100, 3)

# plot:
fig, ax = plt.subplots()

ax.barbs(X, Y, U, V, barbcolor="C0", flagcolor="C0",
            length=10, linewidth=1.5)

ax.set_xlim(0, 8)
ax.set_xticks(np.arange(1, 8))
ax.set_ylim(0, 8)
ax.set_yticks(np.arange(1, 8))

plt.show()
