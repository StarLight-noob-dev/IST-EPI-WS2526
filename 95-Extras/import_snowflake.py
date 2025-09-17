import turtle

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)
        turtle.right(120)
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)

def draw_snowflake(iterations=3):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    for _ in range(3):
        koch_snowflake(300, iterations)
        turtle.right(120)
    turtle.done()

# Example usage:
draw_snowflake(iterations=4)