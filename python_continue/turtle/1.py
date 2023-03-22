import turtle

#def rectangle(a, b):
#     turtle.forward(a)
#     turtle.setheading(90)
#     turtle.forward(b)
#     turtle.setheading(180)
#     turtle.forward(a)
#     turtle.setheading(270)
#     turtle.forward(b)
#
#
# w = int(input())
# h = int(input())
# rectangle(w, h)   # rect

# def rec(a):
#     forward(a)
#     setheading(120)
#     forward(a)
#     setheading(-120)
#     forward(a)
#
# a = int(input())
# rec(a)    # trian

# def sq(side):
#     for i in range(30, 121, 30):
#         turtle.setheading(i)
#         turtle.forward(side)
#         turtle.setheading(i + 90)
#         turtle.forward(side)
#         turtle.setheading(i + 180)
#         turtle.forward(side)
#         turtle.setheading(i + 270)
#         turtle.forward(side)
#
#
# a = int(input())
# sq(a)    # rects with angles

def rects(side):
    for i in range(0, 46, 45):
        turtle.setheading(i + 90)
        turtle.forward(side)
        turtle.setheading(i + 0)
        turtle.forward(side)
        turtle.setheading(270 + i)
        turtle.forward(side)
        turtle.setheading(180 + i)
        turtle.forward(2 * side)
        turtle.setheading(i + 90)
        turtle.forward(side)
        turtle.setheading(i + 0)
        turtle.forward(side)
        turtle.setheading(270 + i)
        turtle.forward(2 * side)
        turtle.setheading(180 + i)
        turtle.forward(side)
        turtle.setheading(90 + i)
        turtle.forward(side)
        turtle.setheading(i + 0)
        turtle.forward(2 * side)
        turtle.setheading(270 + i)
        turtle.forward(side)
        turtle.setheading(180 + i)
        turtle.forward(side)
        turtle.setheading(90 + i)
        turtle.forward(side)
n = int(input())
rects(n)
