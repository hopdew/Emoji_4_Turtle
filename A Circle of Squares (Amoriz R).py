import turtle
turtle.speed(10)
turtle.bgcolor("grey")
turtle.color("pink")
def square(star):
    for q in range(4):
        turtle.forward(155)
        turtle.right(90)

for j in range(60):
    square(100)
    turtle.right(6)



turtle.exitonclick()