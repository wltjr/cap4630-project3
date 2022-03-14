#!/usr/bin/python

from attributes import *
from hard_constraints import *
from tkinter import *

global attr

def openFileCallback():
    name = fd.askopenfilename()
    print(name)

if __name__ == '__main__':
    root = Tk()
    root.title('Project 3')

    attributes = Attributes(root)
    constraints = HardConstraints(root)

    quit = Button(root, text='Quit', command=root.quit)
    quit.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
