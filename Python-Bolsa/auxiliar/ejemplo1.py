import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,50)
y1 = np.sqrt(x * x) + np.sqrt(1 - x * x)
y2 = np.sqrt(x * x) - np.sqrt(1 - x * x)

plt.plot(x, y1, c='r', lw = 3)
plt.plot(x, y2, c='r', lw = 3)
plt.show()
