import sys
import os
import math
import pygame
from pygame.locals import *
# http://programarcadegames.com/python_examples/f.php?file=snake.py
from TIGr import AbstractDrawer


class PyGameDrawer(AbstractDrawer):
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode(self.size)
        self.x = self.width // 2
        self.y = self.height // 2
        self.colours = {'white': (255, 255, 255),
                        'black': (0, 0, 0),
                        'red': (255, 0, 0),
                        'green': (0, 255, 0),
                        'blue': (0, 0, 255)}
        self.penColour = self.colours['black']
        self.screen.fill(self.colours['white'])
        self.penDown = True

    def select_pen(self, pen_num):
        self.pen = self.colours[pen_num.lower()]

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
            newCoords = self.getDestination(self.x, self.y, direction, distance)
            pygame.draw.line(self.screen, self.penColour, [self.x, self.y], newCoords, 1)
        
        self.x = newCoords[0]
        self.y = newCoords[1]
        pygame.display.flip()

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
        pygame.draw.circle(self.screen, self.penColour, [self.x, self.y], int(size))
        pygame.display.flip()

    def draw_rectangle(self, size):
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection += 90
            

    def draw_triangle(self, size):
        ourDirection = 0
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection += 120

    def end(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                pygame.display.flip()

