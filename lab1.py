import numpy as np
import matplotlib.pyplot as pl
#упражение 1
def f(x):
	y=(np.log(np.exp(1/(np.sin(x) + 1)) / (5/4 + 1/(x**15) )))/np.log(1 + x**2)
	return y
	
print(f(1))
print(f(10))
print(f(1000))


#упражнение 2
x_2 = np.arange(-4, 4, 0.01)
pl.plot(x_2, x_2*x_2 - x_2 - 6)
pl.grid(False)
pl.show()

#упражнение 3
x_3 = np.arange(-10, 10, 0.01)
pl.plot(x, np.log(x_3*x_3 + 1)/np.log(1 + np.tan(1/(1 + np.sin(x_3)**2)))*np.exp(-abs(x_3)/10))
pl.grid(False)
pl.show()

#упражнение 4
with pl.xkcd():
    pl.pie([70, 10, 10, 10], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
    pl.title('Где ведутся самые ожесточенные бои')
    pl.show()

#упражнение 5
x_5 = [1, 2, 3, 4, 5, 6]
y_5 = [1, 1.42, 1.76, 2, 2.24, 2.5]
p1, v1 = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)
p_f1 = np.poly1d(p1)
p_f2 = np.poly1d(p2)
pl.errorbar(x, y, xerr=0.05, yerr=0.1)
pl.plot(x,p_f1(x))
pl.plot(x,p_f2(x))
pl.show()

#упражнение 6
def W_func( x, a, b, n ):
    sum = 0
    for i in range(0, n):
        sum += (b**i) * np.cos((a**i) * np.pi * x)
    return sum

x = np.arange(-1, 1, 0.001)

pl.plot(x, W_func(x, 2, 0.3, 13))
pl.grid(False)
pl.show()