from TIGr import AbstractParser

class Parser(AbstractParser):
   def parse(self, raw_source):
        # Printing the Contents we found and Setting up the Drawer
        # TODO REMEMBER TO USE COMMAND AND DATA VALUES
        print(raw_source)
        for row in raw_source:
                if row[0] == 'pen':
                    self.drawer.select_pen(row[1])
                if row[0] == 'pen_down':
                    self.drawer.pen_down()
                if row[0] == 'pen_up':
                    self.drawer.pen_up()
                if row[0] == 'draw':
                    self.drawer.draw_line(row[1],row[2])
                if row[0] == 'X':
                    self.drawer.go_along(row[1])
                if row[0] == 'Y':
                    self.drawer.go_down(row[1])
