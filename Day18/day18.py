from turtle import Turtle, Screen, colormode
import colorgram
import random
tim = Turtle()
colormode(255)
tim.shape(name='circle')
# tim.color('red')
tim.penup()
# tim.goto(-100,200)
tim.pendown()
# tim.pensize(15)
tim.speed(200)
tim.hideturtle()
# tim.setfillopacity(50)

# Draw a square
# for i in range(40):
#     tim.forward(4)
#     tim.penup()
#     tim.forward(4)
#     tim.pendown()

# color_list = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "purple"]

# angle_list = [90, 180, 270, 360]
# for side in range(3,40):
#     tim.color(random.choice(color_list))
#     sum_interior = (side - 2) * 180
#     for turn in range(side):
#         tim.forward(100)
#         tim.right(180 - sum_interior/side)
# def walk(color, angle):
#     tim.pencolor(color)
#     tim.setheading(angle)
#     tim.forward(50)


# def get_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b)
# n = int(360 / 5)
# print(f'n is {n}')
# c_hreading = tim.heading()
# for angle in range(n):
#     tim.pencolor(get_color())
#     tim.circle(150)
#     c_hreading += 5
#     tim.setheading(c_hreading)

# tim.circle(150)
# tim.right(5)
# tim.circle(150)
# for i in range(200):
#     color = get_color()
#     angle = random.choice(angle_list)
#     walk(color, angle)

#----------------------------------------------------------------------------------------------------------------
def draw_spot(n,rgb_panel):
    angle = 90
    tim.penup()
    for i in range(n):
        for j in range(n+1):
            tim.dot(10, random.choice(rgb_panel))
            tim.forward(20)
        if i % 2 == 0:
            tim.left(90)
            tim.forward(20)
            tim.left(90)
            tim.forward(20)
        else:
            tim.right(90)
            tim.forward(20)
            tim.right(90)
            tim.forward(20)

    

color_list = colorgram.extract(r'C:\Users\m_j21\Desktop\Python\100 Days Python\Day18\spot_painting.jpg', 200)
rgb_panel = [color_list[i].rgb for i in range(len(color_list))]
rgbCopy = rgb_panel.copy()
pop = []
i = 0
for rgb in rgbCopy:
    r = rgb.r
    g = rgb.g
    b = rgb.b
    if r > 230 and g > 230 and b > 230:
        pop.append(i)
    i += 1

pop = pop[::-1]
for i in pop:
    rgb_panel.pop(i)

# a = rgb_panel.pop(0)
# b = rgb_panel.pop(0)
# c = rgb_panel.pop(0)
# d = rgb_panel.pop(10)
# print('the white color dot rgb are {} \n {} \n {} \n {}'.format(a, b, c, d))


draw_spot(20,rgb_panel)




























screen = Screen()
screen.exitonclick()