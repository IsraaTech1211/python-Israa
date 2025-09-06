import turtle

turtle.bgcolor('black')
t=turtle.Turtle()
colors=['red','dark red']
for number in range(1000):
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])
    t.speed(500)
turtle.done()
