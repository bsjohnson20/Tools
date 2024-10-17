import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a new turtle object
t = turtle.Turtle()
t.speed(1)


# Draw the airplane
t.penup()
t.goto(0, 50)
t.pendown()
t.color("gray")
t.begin_fill()
for i in range(2):
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0, 30)
t.pendown()
t.color("gray")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(0, 40)
t.pendown()
t.color("gray")
t.begin_fill()
t.circle(5)
t.end_fill()

# Keep the window open
turtle.done()