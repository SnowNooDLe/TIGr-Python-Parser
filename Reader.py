import sys
from TIGr import AbstractSourceReader


class Reader(AbstractSourceReader):
    def go(self):
        content = []
        if not sys.stdin.isatty():
            data = sys.stdin.readlines()
            if len(data) > 0:
                f = open("cache.txt", "w")
                for line in data:
                    content.append(line.strip().split(' '))
                    f.write(line)
                f.close()
        else:
            with open(sys.argv[1], "r") as f:
                for line in f.readlines():
                    content.append(line.strip().split(' '))
        if not content:
            with open("cache.txt", "r") as f:
                for line in f.readlines():
                    content.append(line.strip().split(' '))
        self.parser.parse(content)
