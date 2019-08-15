from inspect import *
from TIGr import AbstractParser
from argparse import ArgumentParser
from TDrawer import *
from TKDrawer import *
from TXTDrawer import *


class LookupArgParser(AbstractParser):
#Made this as a test with using argeparser dynamically, abandoned
    def __init__(self, drawer):
        AbstractParser.__init__(self, drawer)
        self.lookup = {
            '--P': [lambda: self.drawer.select_pen(self.data), "Selects the Pen Color that the Output will use, the default color is black, use words like \"red\" or \"blue\" to select a new color"],
            '--D': [lambda: self.drawer.pen_down(), "Puts the pen down which allows it to draw, the pen is down by default"],
            '--N': [lambda: self.drawer.draw_line(90, self.data[0]), "Moves the pen north up the screen"],
            '--E': [lambda: self.drawer.draw_line(0, self.data[0]), "Moves the pen east across the screen"],
            '--W': [lambda: self.drawer.draw_line(180, self.data[0]), "Moves the pen west across the screen"],
            '--S': [lambda: self.drawer.draw_line(270, self.data[0]), "Moves the pen south down the screen"],
            '--X': [lambda: self.drawer.go_along(self.data[0]), "Moves the pen along the screen, different from east and west becuase it shouldn't draw while moving"],
            '--Y': [lambda: self.drawer.go_down(self.data[0]), "Moves the pen along the screen, different from north and south becuase it shoudn't draw while moving"],
            '--U': [lambda: self.drawer.pen_up(), "Puts the pen up which prevents drawing, the pen is up by default"],
            '--C': [lambda: self.drawer.draw_circle(self.data[0]), "draws a cricle"],
            '--R': [lambda: self.drawer.draw_rectangle(self.data[0], self.data[1]), "draws a rectangle"],
            '--T': [lambda: self.drawer.draw_triangle(self.data[0]), "draws a triangle"]
        }
        self.drawers = {
            '-TKinter': [lambda: self._set_drawer("TK"),"Outputs to TKinter"],
            '-TXT': [lambda: self._set_drawer("TXT"),"Outputs to Plain-Text"],
            '-Turtle': [lambda: self._set_drawer("T"),"Outputs to Turtle"],
            #'-PG': [lambda: self.drawer = TKDrawer(),"Outputs to PyGame"] TODO ADD THIS IN
        }
        self.parser = ArgumentParser(description="Processes input and return Graphical Output.")
        subparsers = self.parser.add_subparsers(help='sub-command help')
        parser_dr = subparsers.add_parser('drawer', help='Select Which Drawer you would like to Output to, by default the output is TXT.')
        for key in self.lookup:
                    self.parser.add_argument(key, help=self.lookup[key][1], default=0)
        for key in self.drawers:
                    parser_dr.add_argument(key, help=self.drawers[key][1], action="store_true",default=False)
##        self.parser.add_argument("parameters", help="stored parameters", nargs='*', type=int)
##        self.parser.add_argument("-dr", "--drawer", dest='drawer', help="Select drawer", choices=['turtle', 'tkinter'],default='turtle')

    def parse(self, raw_source):
        self.source = raw_source  # a line
        print(self.source.split())
        args = self.parser.parse_args(self.source.split())
        for arg in vars(args):
             print (arg, getattr(args, arg))
             full = ("-" + arg)
             if full in self.drawers and getattr(args, arg):
                 self.drawers[full][0]()
        for arg in vars(args):
            full = ("--"+arg)
            if full in self.lookup and getattr(args,arg) != 0:
                print(full,"IS IN")
                print("value",getattr(args,arg))
                print("data",self.data)
                print("function",self.lookup[full][0])
                self.data = [int(getattr(args,arg)),0]
                print("newData",self.data)
                self.lookup[full][0]()
        # for each parsed arge
            # if in lookup
            # do command
##        if parsedargs.command in self.lookup:  # if the command is in the dictionary
##            self.data = parsedargs.parameters
##            self.data.extend(['0', '0'])  # insert default to prevent insufficient parameters
##            func = self.lookup[parsedargs.command][0]()
##            # func()
##            # TODO: drawer will close after the task finished
        

    def _set_drawer(self, which):
        if which == 'T':
            self.drawer = TDrawer()
            print('Use turtle drawer')
        elif which == 'TK':
            self.drawer = TKDrawer()
            print('Use Tkinter drawer')
        elif which == 'TXT':
            self.drawer = TXTDrawer()
            print('Use TXT drawer')
            
