import numpy as np

import matplotlib.pyplot as plt
import fastdataing as fd
data = np.loadtxt("./01.train/train_pre.dat")
y1 = data[:,0]
y2 = data[:,1]

print(y1.shape,y2.shape)
ax = fd.add_ax(fd.add_fig(figsize=(8,6)))
plt.subplots_adjust(left=0.2)
ax.scatter(y1,y2)

x_range = np.linspace(plt.xlim()[0], plt.xlim()[1])

ax.plot(x_range, x_range, "r--", linewidth=1)
ax.set_xlabel("Energy of DFT")
ax.set_ylabel("Energy predicted by deep potential")

plt.show()