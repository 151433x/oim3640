import antigravity
from re import A
import turtle

leo = turtle.Turtle()

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)
# turtle.mainloop()

# def square(t):
#     """write a function called square that takes a paramter named t, which is a turltle that will use the turltle to draw a sqaure."""
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

# rapheal=turtle.Turtle()
# square(rapheal)

def square_length(t,length,edges,a):
    """write a function called square that takes a paramter named t, which is a turltle that will use the turltle to draw a sqaure."""
    t.setheading(a)
    for i in range(edges):
        t.fd(length)
        t.lt(360/edges)
square_length(leo,50,10,100)