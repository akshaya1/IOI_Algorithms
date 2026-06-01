import turtle

t = turtle.Turtle()

# Square house
for i in range(4):
    t.forward(100)
    t.left(90)

# Roof
t.left(45)
t.forward(70)
t.right(90)
t.forward(70)

turtle.done()