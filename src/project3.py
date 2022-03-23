#!/usr/bin/python

from attributes import *
from clasp import *
from hard_constraints import *
from preferences import *
from tasks_display import *
from tkinter import *

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

    def existence(self):
        clauses = []
        for constrant in self.constraints.constraints:
            for clause in self.getClause(constrant):
                clauses.append(clause)

        clasp = Clasp()
        solutions = clasp.solve(0, 4, clauses)

        for solution in solutions:
            self.tasks.add(solution)

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
        self.tasks = TasksDisplay(table_frame)
        table_frame.grid(row=0,column=2)
        frame.pack()

        # existence button
        existence = Button(root, text='Existence', command=self.existence)
        existence.pack(side=LEFT, padx=5, pady=5)

        # exemplify button
        exemplify = Button(root, text='Exemplify', command=None)
        exemplify.pack(side=LEFT, padx=5, pady=5)

        # optimize button
        optimize = Button(root, text='Optimize', command=None)
        optimize.pack(side=LEFT, padx=5, pady=5)

        # omni-optimize button
        omni_optimize = Button(root, text='Omni-optimize', command=None)
        omni_optimize.pack(side=LEFT, padx=5, pady=5)

        # quit button
        quit = Button(root, text='Quit', command=root.quit)
        quit.pack(side=RIGHT, padx=5, pady=5)

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