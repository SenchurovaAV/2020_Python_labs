# упражнение 7
import turtle
import numpy as np 

turtle.shape('turtle')
turtle.speed(0)

n = 1037
theta = 0

for i in range(n):
	turtle.forward(np.sqrt(1 + i * i) / 200)
	turtle.left(2)
	
turtle.exitonclick()