import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt

#np.random.seed(9221999)
# El pollo, creamos un poco de datos aleatorios
data = randn(75)
plt.hist(data)

import sys
# plt.savefig("ejemplo1.png")
plt.show()
