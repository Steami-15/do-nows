import turtle
screen = turtle.Screen()
screen.bgcolor("dark blue") 
donatello = turtle.Turtle() #donatello is mo's favorite TMNT

def square(x, y):
    donatello.pensize(5)
    donatello.pencolor("ghost white")
    donatello.penup()
    donatello.speed(1000)
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(4): 
        donatello.forward(100) 
        donatello.left(-90)
        
def square2(xx, yx):
    donatello.pensize(10)
    donatello.pencolor("dark green")
    donatello.fillcolor("sienna")
    donatello.penup()
    donatello.speed(10)
    donatello.goto(xx, yx)
    donatello.pendown()
    for i in range(4): 
        donatello.forward(1000) 
        donatello.left(-90)
        
def triangle(tx, ty):
    donatello.pensize(5)
    donatello.pencolor("ghost white")
    donatello.fillcolor("ghost white")
    donatello.penup()
    donatello.speed(1000)
    donatello.goto(tx, ty)
    donatello.pendown()
    donatello.begin_fill()
    for i in range(3): 
        donatello.forward(100) 
        donatello.right(-120)
    donatello.end_fill()

def hexagon(hx, hy):
    donatello.pensize(5)
    donatello.pencolor("misty rose")
    donatello.penup()
    donatello.goto(hx, hy)
    donatello.pendown()
    for i in range(6): 
        donatello.forward(80) 
        donatello.right(60)
        
def star(sx, sy):
    donatello.pensize(5)
    donatello.pencolor("white")
    donatello.fillcolor("yellow")
    donatello.penup()
    donatello.goto(sx, sy)
    donatello.pendown()
    donatello.begin_fill()
    for i in range(5): 
        donatello.forward(80) 
        donatello.right(144)
    donatello.end_fill()


def circle(cx, cy, radius):
    donatello.pensize(8)
    donatello.pencolor("light gray")
    donatello.fillcolor("white")
    donatello.penup()
    donatello.speed(1)
    donatello.goto(cx, cy)
    donatello.pendown()
    donatello.begin_fill()
    donatello.circle(radius)
    donatello.end_fill()
    
#call functions
triangle(-100, -155)
square (-100, -150)
square2 (-500, -300)
circle(110, -160, 10)
circle(-130, -190, 10)
star(-200, 10)
hexagon(100, 100)

turtle.done() 
