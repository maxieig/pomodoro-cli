import turtle
t = turtle.Turtle()
t.speed(11)
t.pencolor("blue")
t.fillcolor("purple")
t.begin_fill()
for i in range(40):
    t.fd(115)
    t.lt(130)
t.end_fill()
turtle.done()