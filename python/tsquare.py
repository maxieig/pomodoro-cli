import turtle
t = turtle.Turtle()
t.pencolor("blue")
t.fillcolor("gold")
t.begin_fill()
for i in range(4):
    t.fd(150)
    t.lt(90)
t.end_fill()
turtle.done()