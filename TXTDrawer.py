from TIGr import AbstractDrawer


class TXTDrawer(AbstractDrawer):
    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('pen down')

    def pen_up(self):
        print('pen up')

    def go_along(self, along):
        print(f'GOTO X={along}')

    def go_down(self, down):
        print(f'GOTO Y={down}')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')

    def draw_circle(self, size):
        # Need to fix the comment
        print(f'drawing a circle of something {size}')

    def draw_rectangle(self, size):
        print(f'Drawing a rectangle with size of {size}')

    def draw_triangle(self, size):
        print(f'Drawing a triangle with size of {size}')
