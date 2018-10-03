import turtle
import random

erik = turtle.Turtle();
erik.penup()

erik.speed(5)

graphic_distance = 40
width = 8
height = 8




for z in range(height):
  for i in range(width):
    
    x = 100*i
    y = 100*-z
    
    xy = [x,y]
    coordinPossibility  = [[x+graphic_distance,y],[x,y-graphic_distance],[x+graphic_distance,y-graphic_distance]]
    x1y1 = random.choice(coordinPossibility)

    x1 = x1y1[0]
    y1 = x1y1[1]
    
    erik.goto(x,y);
    erik.pendown()
    erik.goto(x1,y1)
    coordinPossibility.remove(x1y1)

    x2y2 = random.choice(coordinPossibility)

   
    x2 = x2y2[0]
    y2 = x2y2[1]

    erik.goto(x2,y2)
    coordinPossibility.remove(x2y2)
    coordinPossibility.append(xy)

    x3y3 = random.choice(coordinPossibility)
    x3 = x3y3[0]
    y3 = x3y3[1]

    erik.goto(x3,y3)
    coordinPossibility.remove(x3y3)
    coordinPossibility.append(x1y1)

    erik.penup()

  erik.backward(100 * width)
  erik.right(90)
  erik.forward(100)
  erik.left(90)

turtle.done()     