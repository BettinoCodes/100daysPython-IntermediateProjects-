from turtle import Turtle, Screen
import random
import turtle
import colorgram

#Day 18 extracting data using colorgram.py tool on Python, to use the colors as random choosing to a dotted painting, for extra I allowed the users to choose the amount of rows and columns desired

# colors = colorgram.extract('img_sjpeg.jpg', 20)
# #viewing the data collection
# print(colors)
#
# rgb = first_color.rgb
#
# #test
# print(rgb)


# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     newtuple = (red, green, blue)
#     list_of_colors.append(newtuple)
#
# print(list_of_colors)

list_of_colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24),
                  (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
                  (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
                  (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
                  (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]


#Exersize 4
# sides = 3
# for i in range(10):
#     timmy.color(random_color())
#     n = 0
#     while n < sides:
#         timmy.forward(40)
#         timmy.left(360/sides)
#         n += 1
#     sides += 1

#Exersize 5
# directions = [90, 270]
# line_thick = 1
# timmy.pensize(10)
# while True:
#     timmy.pensize(line_thick)
#     timmy.color(random_color())
#     timmy.forward(70)
#     timmy.left(random.choice(directions))
#     line_thick += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_circle(timmy):
    timmy.color(random.choice(list_of_colors))
    timmy.begin_fill()
    timmy.circle(10)
    timmy.end_fill()


rows = int(turtle.textinput('Rows', "How many rows do you want: "))
cols = int(turtle.textinput('Columns', "How many columns do you want: "))
turtle.colormode(255)
timmy = Turtle()
timmy.shape('circle')
timmy.color("green")


timmy.speed("fastest")
directions = [90, 270]
timmy.pensize(10)

timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

#checking the position of the turtle
print(timmy.position())
height = -212.13


for i in range(rows):
    for x in range(cols):
        draw_circle(timmy)
        timmy.penup()
        timmy.forward(70)
        timmy.pendown()
    timmy.penup()
    height += 50
    timmy.goto(-212.13, height)
    timmy.pendown()
    if i == rows:
        timmy.penup()
        timmy.goto(-212.13, height-250)
        timmy.shape('turtle')
        timmy.color('black')


screen = turtle.Screen()
screen.exitonclick()
