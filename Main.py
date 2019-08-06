import sys
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader

if len(sys.argv) == 1:
    print("no args > should launch console") #SHOULD LAUNCH CMD
else:
    outputs = []
    for arg in sys.argv:
        if arg == '-TK':
            outputs.append(Reader(Parser(TKDrawer())))
        if arg == '-T':
            pass
        if arg == '-PG':
            pass
        if arg == '-TXT':
            outputs.append(Reader(Parser(TXTDrawer())))
    if (len(outputs) == 0):
        outputs.append(Reader(Parser(TXTDrawer())))
    for output in outputs:
        output.go()
# ADD IN A CHECK FOR NO FILE GIVEN VIA PIPING OR WITH A GIVEN DIRECTORY, THEN LAUNCH THE CONSOLE WITH A MESSAGE
# TODO MOVE all classes to seperate files and move all interpreters to a sub folder called \parsers
