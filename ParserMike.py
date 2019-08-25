from TIGr import AbstractParser


class ParserMike(AbstractParser):

    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0
        self.lookup = {  # M
            'P': lambda: self.drawer.select_pen(self.data),
            'D': lambda: self.drawer.pen_down(),
            'N': lambda: self.drawer.draw_line(0, self.data),
            'E': lambda: self.drawer.draw_line(90, self.data),
            'S': lambda: self.drawer.draw_line(180, self.data),
            'W': lambda: self.drawer.draw_line(270, self.data),
            'X': lambda: self.drawer.go_along(self.data),
            'Y': lambda: self.drawer.go_down(self.data),
            'U': lambda: self.drawer.pen_up(),
            'C': lambda: self.drawer.draw_circle(self.data),
            'R': lambda: self.drawer.draw_rectangle(self.data),
            'T': lambda: self.drawer.draw_triangle(self.data)}

    def parse(self, raw_source):
        self.source = raw_source
        for line in self.source:
            self.command = line[0]
            if len(line) > 1:
                self.data = line[1]
            else:
                self.data = 0
            print(self.data)
            if self.command in self.lookup:
                self.lookup[self.command]()
        try:
            self.drawer.end()
        except:
            print("Completed")


if __name__ == '__main__':
    from TDrawer import *

    p = ParserMike(TDrawer())
    p.parse("E")
