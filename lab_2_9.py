# крпажнение 9

import numpy as np
turtle.shape('turtle')
def r_ang(n,r):
	turtle.forward(10)
	turtle.pendown()
	turtle.left(90)
	for j in range(n):
		turtle.left(360 / n)
		turtle.forward(2 * r * np.sin(np.pi / n))
	turtle.left(90)
	turtle.penup()
	turtle.forward(20)
	turtle.left(180)
	turtle.penup()	
		
for i in range(1, 8):
	
	r_ang(i, 20 * i)