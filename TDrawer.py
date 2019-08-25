import math
from TIGr import AbstractDrawer
import turtle


# Turtle uses counter clockwise system and zero point starts from the left hand side

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
        x = turtle.xcor()
        if (turtle.isdown()):
            turtle.penup()
            turtle.setx(x + int(along))
            turtle.pendown()
        else:
            turtle.setx(x + int(along))

    def go_down(self, down):
        y = turtle.ycor()
        if (turtle.isdown()):
            turtle.penup()
            turtle.sety(y + int(down))
            turtle.pendown()
        else:
            turtle.goty(y + int(down))

    def draw_line(self, direction, distance):
        # IF YOU WANT TO HAVE DYNAMIC DIRECTIONS YOU NEED TO UPDATE THIS CODE
        direction = self._convert_direction(direction)
        distance = int(distance)
        turtle.seth(direction)
        if (turtle.isdown()):
            turtle.forward(distance)

    def _convert_direction(self, direction):
        # Turtle default direction:     convert
        # 90 - north                    0 -> 90        +90
        # 0 - east                      90-> 0         -90
        # 270 - south                   180 -> 270     +90
        # 180 - west                    270-> 180      -90
        newdirection =  (direction + 90) % 360
        return newdirection

    def draw_circle(self, size):
        turtle.circle(int(size))

    # for rectangle and triangle, unlike TKinter, they work based on where they are facing and remember previous move, not like TKinter resets where
    # they are facing everytime we move.
    def draw_rectangle(self, size):
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection -= 90

    def draw_triangle(self, size):
        ourDirection = 0
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection -= 120

    def end(self):
        turtle.exitonclick()


if __name__ == '__main__':
    d = TDrawer()
    # d.draw_circle(50)
    # d.go_along(50)
    d.draw_rectangle(50)
    # d.go_along(50)
    # d.draw_rectangle(50)
    d.go_along(50)
    d.draw_triangle(50)
    d.end()
