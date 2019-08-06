import sys
from TIGr import AbstractSourceReader

class Reader(AbstractSourceReader):
    def go(self):
        content = []
        if not sys.stdin.isatty():  #self.file_name = None && << TODO ADD IN FILE NAME CHECKING >>POSITION INDEPENDANT<<
            for line in sys.stdin.readlines():
                        content.append(line.strip().split(' '))
        else:
            with open(sys.argv[1],"r") as f:
                for line in f.readlines():
                    content.append(line.strip().split(' '))
        self.parser.parse(content)
