from random import*
from  math import*
from  time import*
DARTS = 2**22
hits = 0
clock()
for i in range(1,DARTS):
	x,y = random(),random()
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits / DARTS)
print("pi 值是%f" %pi)
print("程序运行 的时间是 %-5.5f" %clock())