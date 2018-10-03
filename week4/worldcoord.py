import turtle

turtle = turtle.Turtle()

turtle.reset()
turtle.setworldcoordinates(-50,-7.5,50,7.5)

for _ in range(72):
	turtle.left(10)

for _ in range(8):
	turtle.left(45); turtle.fd(2)
