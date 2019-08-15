from inspect import *
from TIGr import AbstractParser
from argparse import ArgumentParser
from TDrawer import *
from TKDrawer import *


class ArgParser(AbstractParser):

    def __init__(self, drawer):
        AbstractParser.__init__(self, drawer)
        self.parser = ArgumentParser()
        self.subparser = self.parser.add_subparsers()
        # Create parser for command R
        # Draw rectangle
        r_subparser = self.subparser.add_parser('R')
        r_subparser.add_argument('-x', help='set width', default=10)
        r_subparser.add_argument('-y', help='set height', default=10)
        r_subparser.set_defaults(func=self._draw_rectangle)

        # Create parser for command dr
        # change drawer permanently
        drawer_subparser = self.subparser.add_parser('dr')
        drawer_subparser.add_argument('-drawer', choices=['turtle', 'tkinter'], default='turtle')
        drawer_subparser.set_defaults(func=self._set_drawer)

    def parse(self, raw_source):
        self.source = raw_source  # a line
        args = self.parser.parse_args(self.source.split())

        args.func(args)

    def _set_drawer(self, args):
        drawer = args.drawer
        if drawer == 'turtle':
            self.drawer = TDrawer()
            print('Use turtle drawer')
        elif drawer == 'tkinter':
            self.drawer = TKDrawer()
            print('Use Tkinter drawer')

    def _draw_rectangle(self, args):
        x = args.x
        y = args.y
        drawer = self.drawer
        drawer.draw_rectangle(x, y)

    # TODO: more command functions needed


if __name__ == '__main__':
    parser = ArgParser(TDrawer())
    args = parser.parse("R")

    args = parser.parse("dr -dr tkinter")
