import sys
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TDrawer import *
from TKCmd import *
from ParserMike import *
from LookupArgParser import *
from PyGameDrawer import *
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader


def main():
    outputs = []
    if len(sys.argv) == 1:
        print(
            "You need to specify a CMD loop to enter, -TKCMD or -TCMD... or you can specify a TEXT file and declare outputs with -TK -T -P and -TXT ...GOOD LUCK!")
    else:
        for arg in sys.argv:
            if arg == '-TCMD':
                main_marcus(LookupArgParser(TDrawer()))
                sys.exit()
            if arg == '-TKCMD':
                TKInterShell().cmdloop()
                sys.exit()
            if arg == '-TK':
                outputs.append(Reader(Parser(TKDrawer())))
            if arg == '-T':
                outputs.append(Reader(ParserMike(TDrawer())))
            if arg == '-TXT':
                outputs.append(Reader(Parser(TXTDrawer())))
            if arg == '-P':
                outputs.append(Reader(Parser(PyGameDrawer())))
        if len(outputs) == 0:
            outputs.append(Reader(Parser(TXTDrawer())))
        for output in outputs:
            output.go()
        sys.exit()


def main_marcus(aparser):  # Marcus and Josiah
    parser = aparser
    print('Welcome to Argeparse by Marcus and Josiah: ')
    while True:
        argv = input("ArgeparseCMD: ")
        if argv == "end":
            print("Bye!")
            break
        else:
            try:
                # print(argument)
                parser.parse(argv)
            except:
                print("")


if __name__ == '__main__':
    main()
