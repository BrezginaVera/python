%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 20, 21)
k = 1
plt.plot(x, np.cos(k*x), marker = "o") #график функции обозначен синим цветом
l = 4
plt.plot(x, np.cos(l*x), marker = "o") #график функции обозначен оранжевым цветом