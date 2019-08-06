from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 100, 200, 0, fill="black", dash=(4, 4))

mainloop()
