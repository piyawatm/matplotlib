'''
Rotation Bug without the box

'''

'''
import matplotlib.pyplot as plt
plt.plot([0, 1], lw=0)
plt.axvline(.5, linewidth=.5, color='.5')
plt.axhline(.5, linewidth=.5, color='.5')

N = 4

for r in range(N):
    plt.text(.5, .5, 'p', color=plt.get_cmap('jet')(r/N), size=100, rotation=r/N*360, va='center_baseline', rotation_mode='anchor')


plt.text(.5, .5, 'p', color=plt.get_cmap('jet')(1/4), size=100, rotation=180, va='center_baseline', rotation_mode='anchor')
plt.text(.5, .5, 'p', color=plt.get_cmap('jet')(2/4), size=100, rotation=0, va='center_baseline', rotation_mode='anchor')

plt.show()
'''

'''
Rotation Bug with the box

'''

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)
for idx, ax in enumerate(axes.flatten()):
      ax.axvline(.5, linewidth=.5, color='.5')
      ax.axhline(.5, linewidth=.5, color='.5')
      ax.text(
          .5, .5, 'p', size=50,
          bbox=dict(facecolor='None', edgecolor='red', pad=0),
          rotation=idx*90,
          va='center_baseline',
          rotation_mode='anchor'
      )

plt.show()