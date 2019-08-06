import math
from tkinter import *
from TIGr import AbstractDrawer

class TKDrawer(AbstractDrawer):

    def __init__(self):
        self.x = 0
        self.y = 0
        master = Tk()
        self.w = Canvas(master, width=500, height=500)
        self.w.pack()
        self.pen = "black"
        self.penDown = True

    def select_pen(self, pen_num):
        self.pen = pen_num
        
    def pen_down(self):
        self.penDown = True

    def pen_up(self):
        self.penDown = False

    def go_along(self, along):
        self.x += int(along)

    def go_down(self, down):
        self.y += int(down)

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        if (self.penDown):
            newCoords = self.getDestination(self.x,self.y,direction,distance)
            print(newCoords)
            self.w.create_line(self.x, self.y, newCoords[0], newCoords[1], fill=self.pen)
            mainloop()

    def getDestination(self, currentX, currentY, direction, distance):
        direction = float(direction)
        # Compute the change in position
        delta_y = distance * math.cos(math.radians(direction))
        delta_x = distance * math.sin(math.radians(direction))
        # Add that to the existing position
        new_x = currentX + delta_x
        new_y = currentY + delta_y
        return new_x, new_y
