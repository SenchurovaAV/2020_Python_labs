import turtle as tt
import math

l=30
l2=l*math.sqrt(2)
num = [
	(0, 0, l, 90, 2 * l, 90, l, 90, 2 * l, 90), # 0
	(l, 90, 2 * l,135, l2, 135), 				# 1
	(l, 180, l,-135, l2, 45, l, 90, l, 180),	# 2
	(0, 45, l2, 135, l, -135, l2, 135, l, 180),	# 3
	(l,90, 2*l, 180, l, -90, l, -90, l, -90),	# 4
	(0, 0, l, 90, l, 90, l, -90, l, -90, l), 	# 5
	(0, 0, l, 90, l, 90, l, 90, l, 180, l, -45, l2, -45),	# 6
	(0, 90, l, -45, l2, 135, l, 180),			# 7
	(0, 0, l, 90, 2*l, 90, l, 90, 2*l, 180, l, -90, l),		# 8
	(0, 45, l2, 45, l, 90, l, 90, l, 90, l) 	# 9
]

number = input()

for k, digit in enumerate(number):
	tt.penup()
	tt.goto((k-len(number)/2)*(l+10),0)
	tt.pendown();
	n = num[int(digit)]
	tt.penup()
	tt.forward(n[0])
	tt.left(n[1])
	tt.pendown()
	for j in range(2, len(n), 3):
		if (j%2==0):
			t.forward(n[j])
		else:
			t.left(n[j])
tt.exitonclick()
	