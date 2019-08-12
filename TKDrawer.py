import math
from tkinter import *
from TIGr import AbstractDrawer


class TKDrawer(AbstractDrawer):

    def __init__(self):
        self.x = 250
        self.y = 250
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.pen = "black"
        self.penDown = True

    def select_pen(self, pen):
        self.pen = pen

    def pen_down(self):
        self.penDown = True

    def pen_up(self):
        self.penDown = False

    def go_along(self, along):
        self.x = int(along)

    def go_down(self, down):
        self.y = int(down)

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        if (self.penDown):
            newCoords = self.getDestination(self.x, self.y, direction, distance)
            self.w.create_line(self.x, self.y, newCoords[0], newCoords[1], fill=self.pen)
        self.x = newCoords[0]
        self.y = newCoords[1]

    def getDestination(self, currentX, currentY, direction, distance):
        direction = float(direction)
        # Compute the change in position
        delta_y = distance * math.cos(math.radians(direction))
        delta_x = distance * math.sin(math.radians(direction))
        # Add that to the existing position
        new_x = currentX + delta_x
        new_y = currentY + delta_y
        return new_x, new_y

    def draw_circle(self, size):
        ourDirection = 0
        for i in range(360):
            self.draw_line(ourDirection, size)
            ourDirection += 1

    def draw_rectangle(self, size):  # J
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection += 90

    def draw_triangle(self, size):  # M
        ourDirection = 0
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection += 120

    def end(self):
        print("tkinter is sleeping now")
        mainloop()
