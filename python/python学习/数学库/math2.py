import numpy as np
from matplotlib.pyplot import *

def f(t):
	return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
subplot(221)
plot(t1, f(t1), "bo", t2, f(t2), 'k')
subplot(212)
plot(t2, np.cos(2 * np.pi * t2), "r--")
show()