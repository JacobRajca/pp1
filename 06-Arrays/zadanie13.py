import matplotlib.pyplot as plt
import numpy as np

x = np.array(['car','public','bike','foot'])
y = np.array([25,19,32,7])

plt.bar(x,y)
plt.show()