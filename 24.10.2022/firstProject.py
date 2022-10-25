import turtle

# Створюємо першу черепашку
t1 = turtle.Turtle() 
t1.color("green")
t1.width(5)
t1.shape("square")
t1.turtlesize(1)
t1.penup()
# Створюємо нову черепашку
t2 = turtle.Turtle()
t2.color("red")
t2.turtlesize(1)
t2.shape("circle")
t2.penup()
t2.goto(0,-100)

step = int(input("Введіть кількість кроків"))

if step > 5:
    t1.right(90)
else:
    t1.left(90)
t1.forward(step)

if t1.ycor() == t2.ycor():
    t2.hideturtle()
    t1.color("red")
    t1.turtlesize(2)
    t2.goto(0,100)
    t2.showturtle()


turtle.done()
















