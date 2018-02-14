import numpy as nu
from matplotlib.pyplot import *

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(X * X), np.sin(X)
plot(X, C, label = "$sin(x)$")
plot(X, S, label = "$cos(x ^ 2)$")
xlabel("x")
ylabel("y")
#legend()
title("This is Title")
show()