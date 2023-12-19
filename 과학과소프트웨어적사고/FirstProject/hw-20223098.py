import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)


t.penup()
t.goto(-35, 220)
t.pendown()

t.dot(27)

t.penup()
t.goto(35, 220)
t.pendown()

t.dot(27)

x = 0
y = 100
t.penup()
t.goto(x, y)
t.pendown()

t.circle(100)

t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)

t.up()
t.color("blue")
t.goto(-65, 20)
t.write("학번 : 20223098", font=("궁서", 20))

t.up()
t.color("blue")
t.goto(-65, -10)
t.write("이름 : 신진욱", font=("궁서", 20), move=True)

t.hideturtle()

turtle.done()