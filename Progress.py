import sys
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader

"""These implementations should be replaced,
by more flexible, portable and extensible solutions.
"""


class Drawer(AbstractDrawer):
    """ Responsible for printing as text what the drawing commands are"""

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


class Parser(AbstractParser):

    def parse(self, raw_source):
        print(raw_source)
        for row in raw_source:
                if row[0] == 'pen':
                    self.drawer.select_pen(row[1])
                if row[0] == 'pen_down':
                    self.drawer.pen_down()
                if row[0] == 'pen_up':
                    self.drawer.pen_up()
                if row[0] == 'draw':
                    self.drawer.draw_line(row[1],row[2])
                if row[0] == 'X':
                    self.drawer.go_along(row[1])
                if row[0] == 'Y':
                    self.drawer.go_down(row[1])



class SourceReader(AbstractSourceReader):
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def go(self):
        # self.parser.parse(sys.stdin)
        content = []
        with open(sys.argv[1],"r") as f:
                    for line in f.readlines():
                        content.append(line.strip().split(' '))
        self.parser.parse(content)


if __name__ == '__main__':
    s = SourceReader(Parser(Drawer()))
    s.go()
