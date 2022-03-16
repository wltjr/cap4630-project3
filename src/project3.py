#!/usr/bin/python

from attributes import *
from hard_constraints import *
from preferences import *
from tkinter import *

global attr

def openFileCallback():
    name = fd.askopenfilename()
    print(name)

if __name__ == '__main__':
    root = Tk()
    root.title('Project 3')

    # wrapper frames
    frame = Frame(root)
    table_frame = Frame(frame)

    # main UI, tables and forms
    group_frame = Frame(table_frame)
    attributes = Attributes(group_frame)
    group_frame.pack(side=LEFT, padx=5, pady=5)
    constraints = HardConstraints(group_frame)
    group_frame.pack(side=LEFT, padx=5, pady=5)
    table_frame.grid(row=0,column=0)
    preferences = Preferences(table_frame)
    table_frame.grid(row=0,column=1)
    frame.pack()

    # quit button
    quit = Button(root, text='Quit', command=root.quit)
    quit.pack()
    root.mainloop()

    # data structures from classes
#    attributes.attributes
#    constraints.constraints
#    preferences.penalties
#    preferences.possibilistics
#    preferences.qualitatives
