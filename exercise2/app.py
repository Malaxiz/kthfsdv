#!./kthfsdv/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import math

def lam(t):
    return 5 * np.sin(2 * math.pi * t)

def h(t):
    return 3 * math.pi * np.exp(-lam(t))

# plt.subplot(2, 1, 1)
plt.title('x')
plt.ylabel('y')

x = np.linspace(-15,15,100)
y = h(x)

plt.plot(x,y)
plt.show()