import turtle
t = turtle.Turtle()
t.pencolor("red")

def figure(edges, length):
    a = round(length/edges)
    b = 5
    c = round(a/(2*b))
    degree = round(360/edges)
    for i in range(edges):
        for j in range(c):
            t.forward(b)
            t.penup()
            t.forward(b)
            t.pendown()
        t.right(degree)

figure(7, 1000)
