import sys
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TDrawer import *
from TKCmd import *
from ParserMike import *
from LookupArgParser import *

def main():
    outputs = []
    if len(sys.argv) == 1:
        print("You need to specify a CMD loop to enter, -TOM or -M... or you can specify a TEXT file and declare outputs with -TK -T -TXT...GOOD LUCK!")
    else:
        for arg in sys.argv:
            if arg == '-M':
                main_marcus(LookupArgParser(TDrawer()))
                sys.exit()
            if arg == '-TOM':
                TKInterShell().cmdloop()
                sys.exit()
            if arg == '-TK':
                outputs.append(Reader(Parser(TKDrawer())))
            if arg == '-T':
                outputs.append(Reader(ParserMike(TDrawer())))
            if arg == '-TXT':
                outputs.append(Reader(Parser(TXTDrawer())))
        if len(outputs) == 0:
            outputs.append(Reader(Parser(TXTDrawer())))
        for output in outputs:
            output.go()
        sys.exit()

def main_marcus(aparser):
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

if __name__ == "__main__":
    main()




    
