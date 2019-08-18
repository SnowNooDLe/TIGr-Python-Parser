import math
from TIGr import AbstractDrawer
import turtle


class TDrawer(AbstractDrawer):
    def __init__(self):
        self.penlist = ["black", "red", "blue"]

    def select_pen(self, pen_num):
        turtle.pencolor(self.penlist[int(pen_num) - 1])

    def pen_down(self):
        turtle.pendown()

    def pen_up(self):
        turtle.penup()

    # Because for along and down, we dont wanna draw line while we are moving
    def go_along(self, along):
        if (turtle.isdown()):
            turtle.penup()
            turtle.setx(int(along))
            turtle.pendown()
        else:
            turtle.setx(int(along))

    def go_down(self, down):
        if (turtle.isdown()):
            turtle.penup()
            turtle.sety(int(down))
            turtle.pendown()
        else:
            turtle.sety(int(down))

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        # based on TKinter, when angles increasing, turning left, so approach same way, turning left.
        turtle.left(direction)
        if (turtle.isdown()):
            turtle.forward(distance)

    def draw_circle(self, size):
        turtle.circle(int(size))

    # for rectangle and triangle, unlike TKinter, they work based on where they are facing and remember previous move, not like TKinter resets where
    # they are facing everytime we move.
    def draw_rectangle(self, size):
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection = 90

    def draw_triangle(self, size):
        ourDirection = 0
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection = 120

    def end(self):
        turtle.exitonclick()
