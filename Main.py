import sys
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TDrawer import *
from TKCmd import *
from ParserMike import *  # TODO Make this a package


def main():
    outputs = []
    if len(sys.argv) == 1:
        TKInterShell().cmdloop()  # NEED TO REMOVE THIS IF YOU ADD IN SECOND CMD LINE
    for arg in sys.argv:
        if arg == '-TK':
            outputs.append(Reader(Parser(TKDrawer())))
        if arg == '-T':
            outputs.append(Reader(Parser(TDrawer())))
        if arg == '-TXT':
            outputs.append(Reader(Parser(TXTDrawer())))
    if len(outputs) == 0:
        outputs.append(Reader(Parser(TXTDrawer())))
    for output in outputs:
        output.go()


if __name__ == "__main__":
    main()
