#!/usr/bin/python

from attributes import *
from hard_constraints import *
from preferences import *
from tkinter import *

global attr
class ui:
    def openFileCallback():
        name = fd.askopenfilename()
        print(name)

    def getClause(self, string):
        clause = []
        stringlist = string.split()
        newstring = ""
        negate = False
        for i in stringlist:
            if i == "AND":
                clause.append(newstring)
                newstring = ""
            elif i == "OR":
                newstring = newstring + " "
            elif i == "NOT":
                negate = True
            else:
                value = self.attributes.getKeyByValue(i)
                if negate:
                    value = -value
                    negate = False
                newstring = newstring + str(value)
        clause.append(newstring)
        return clause


    def printAttributes(self):
        clauses = []
        # this would wrap another function passing attributes as arg
        for a in self.constraints.constraints:
            for clause in self.getClause(a):
                clauses.append(clause)
        print(clauses)

    def run(self):
        root = Tk()
        root.title('Project 3')

        # wrapper frames
        frame = Frame(root)
        table_frame = Frame(frame)

        # main UI, tables and forms
        group_frame = Frame(table_frame)
        self.attributes = Attributes(group_frame)
        group_frame.pack(side=LEFT, padx=5, pady=5)
        self.constraints = HardConstraints(group_frame)
        group_frame.pack(side=LEFT, padx=5, pady=5)
        table_frame.grid(row=0,column=0)
        self.preferences = Preferences(table_frame)
        table_frame.grid(row=0,column=1)
        frame.pack()

        # quit button
        quit = Button(root, text='Quit', command=root.quit)
        quit.pack(side=LEFT, padx=5, pady=5)


        # print button
        print = Button(root, text='Print Attributes', command=self.printAttributes)
        print.pack(side=LEFT, padx=5, pady=5)
        root.mainloop()

        # data structures from classes
    #    attributes.attributes
    #    constraints.constraints
    #    preferences.penalties
    #    preferences.possibilistics
    #    preferences.qualitatives

if __name__ == '__main__':
    ui = ui()
    ui.run()