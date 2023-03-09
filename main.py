# from colorgram import extract
# rgb_colors = []
# colors = extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
from random import choice, randint, shuffle

screen = Screen()
circle = Turtle()
circle.speed("fastest")
screen.bgcolor("white")
screen_size = screen.setup(500, 500)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
turtle.colormode(255)
circle.hideturtle()

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157),
              (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
              (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
              (184, 103, 113),
              (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


def hirst_colors(color_list):
    """Drawing Horst color"""
    r = color_list[randint(0,25)][0]
    g = color_list[randint(0,25)][1]
    b = color_list[randint(0,25)][2]
    return (r, g, b)
color = hirst_colors(color_list)




def circles_in_line():
    x = circle.xcor()
    y = circle.ycor()
    for _ in range(25):
        circle.color(hirst_colors(color_list))
        circle.dot(15)
        circle.penup()
        x += 20
        circle.setx(x)
        circle.pendown()
    circle.penup()
    circle.setx(0)
    y += 20
    circle.sety(y)
    circle.pendown()




for _ in range(25):
    circles_in_line()

screen.exitonclick()
