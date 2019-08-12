from TIGr import AbstractDrawer
import turtle


class TDrawer(AbstractDrawer):  
    def select_pen(self, pen_num):
        turtle.color("black")

    def pen_down(self):
        turtle.pendown()

    def pen_up(self):
        turtle.penup()

    def go_along(self, along):
        turtle.setx(float(along))

    def go_down(self, down):
        turtle.sety(float(down))

    def draw_line(self, direction, distance):
        turtle.setheading(float(direction))
        turtle.forward(int(distance))
        
    def draw_circle(self, radius):
        turtle.circle(int(radius))

    def draw_rectangle(self, width, height=None):  # J
        if height == None:
            height = width
        for i in range(2):
            turtle.forward(int(width))
            turtle.right(90)
            turtle.forward(int(height))
            turtle.right(90)

    def draw_triangle(self, length):  # M
        for i in range(3):
            turtle.right(120)
            turtle.forward(int(length))

    def end(self):
        print("Turtle is sleeping now")
            


