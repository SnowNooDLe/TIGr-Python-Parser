from inspect import *
from TIGr import AbstractParser
from argparse import ArgumentParser
from TDrawer import *
from TKDrawer import *
from TXTDrawer import *


class LookupArgParser(AbstractParser):
    def __init__(self, drawer):
        AbstractParser.__init__(self, drawer)
        self.lookup = {  # Marcus and Josiah
            'P': lambda: self.drawer.select_pen(self.data),
            'D': lambda: self.drawer.pen_down(),
            'N': lambda: self.drawer.draw_line(0, self.data[0]),
            'E': lambda: self.drawer.draw_line(90, self.data[0]),
            'W': lambda: self.drawer.draw_line(270, self.data[0]),
            'S': lambda: self.drawer.draw_line(180, self.data[0]),
            'X': lambda: self.drawer.go_along(self.data[0]),
            'Y': lambda: self.drawer.go_down(self.data[0]),
            'U': lambda: self.drawer.pen_up(),
            'C': lambda: self.drawer.draw_circle(self.data[0]),
            'R': lambda: self.drawer.draw_rectangle(self.data[0]),
            'T': lambda: self.drawer.draw_triangle(self.data[0]),
        }
        # Clever Solution combining lookup table and argparse!
        # https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
        self.parser = ArgumentParser()
        self.parser.add_argument("command", help="command argument", choices=self.lookup.keys())
        # narg:
        # ? means 0~1
        # * means 0~many
        # + means 1~many
        # nargs accepts multiple parameters
        self.parser.add_argument("parameters", help="stored parameters", nargs='*',
                                 type=int)
        self.parser.add_argument("-dr", "--drawer", dest='drawer', help="Select drawer",
                                 choices=['turtle', 'tkinter', 'TXT'],
                                 default='turtle'
                                 )  # Default drawer is turtle

    def parse(self, raw_source):
        self.source = raw_source  # a line
        # print(self.source.split())
        parsedargs = self.parser.parse_args(self.source.split())
        self._set_drawer(parsedargs)  # Set the drawer depending on the switch

        if parsedargs.command in self.lookup:  # if the command is in the dictionary
            self.data = parsedargs.parameters
            self.data.extend(['0', '0'])  # insert default to prevent insufficient parameters

            func = self.lookup[parsedargs.command]()

    def _set_drawer(self, args):
        drawer = args.drawer
        if drawer == 'turtle':
            self.drawer = TDrawer()
            print('Use turtle drawer')
        elif drawer == 'tkinter':
            self.drawer = TKDrawer()
            print('Use Tkinter drawer')
        elif drawer == 'TXT':
            self.drawer = TXTDrawer()
            print('Use TXT drawer')


if __name__ == '__main__':
    parser = LookupArgParser(TDrawer())
    args = parser.parse("R ")  # No given value, so the radius would be default value 0

    parser.parse("T 50 --dr tkinter")
    parser.parse("C         100 ")
    args = parser.parse("dr -dr tkinter")
