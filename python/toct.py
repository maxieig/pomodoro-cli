import turtle
t = turtle.Turtle()
t.pencolor("blue")
t.fillcolor("gold")
t.begin_fill()
for i in range(8):      
    t.fd(100)           
    t.lt(45)            
t.end_fill()
turtle.done()