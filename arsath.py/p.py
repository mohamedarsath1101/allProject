import turtle
import colorsys
turtle.speed(1)
turtle.color('green','yellow')
turtle.begin_fill()
while True:
    turtle.forward(500)
    turtle.left(200)
    if abs(turtle.pos())<1:
        break
turtle.end_poly
turtle.done()