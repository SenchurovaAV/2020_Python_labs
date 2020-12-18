#упражнение 6
import turtle

turtle.shape('turtle')
n = 13
for i in range(n):
	turtle.forward(200)
	turtle.right(180)
	turtle.forward(200)
	turtle.left(180 - 360 / n)
	