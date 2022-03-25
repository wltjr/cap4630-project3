#!/usr/bin/python

from attributes import *
from clasp import *
from hard_constraints import *
from preferences import *
from preferences_display import *
from tasks_display import *
from tkinter import *
from tkinter import messagebox as mb

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
        attributeCount = self.attributes.count
        if attributeCount == 0:
            mb.showerror("Empty Attributes Error",
                         "Please load or enter attributes")
            self.notebook.select(self.tab1)
            return

        if self.constraints.count == 0:
            mb.showerror("Empty Contraints Error",
                         "Please load or enter contraints")
            self.notebook.select(self.tab1)
            return

        self.tasks.clearTable()

        clauses = []
        for constrant in self.constraints.constraints:
            for clause in self.getClause(constrant):
                clauses.append(clause)
        self.clauses = clauses

        clasp = Clasp()
        solutions = clasp.solve(0, attributeCount, clauses)
        for solution in solutions:
            text = ""
            for key in solution:
                text += self.attributes.getValueByKey(key) + " "
            text = text[:-1]
            self.tasks.add(solution, text)

        self.notebook.select(self.tab2)


    def exemplify(self):
        self.existence()


    def reset(self):
        self.attributes.count = 0
        self.attributes.attr.clear()
        self.constraints.count = 0
        self.constraints.hc.clear()
        self.preferences.qual_count = 0
        self.preferences.qual.clear()
        self.preferences.poss_count = 0
        self.preferences.poss.clear()
        self.preferences.pen_count = 0
        self.preferences.pen.clear()


    def run(self):
        root = Tk()
        root.title('Project 3')

        notebook = ttk.Notebook(root)
        
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)

        notebook.add(tab1, text="Input")
        notebook.add(tab2, text="Output")
        notebook.pack(expand = 1, fill ="both")

        # wrapper frames
        frame = Frame(tab1)

        # main UI, tables and forms
        group_frame = Frame(frame)
        self.attributes = Attributes(group_frame)
        self.constraints = HardConstraints(group_frame)
        group_frame.pack(side=LEFT, padx=5)
        self.preferences = Preferences(frame)
        frame.pack()

        self.tasks = TasksDisplay(tab2)
        self.prefDisplay = PreferencesDisplay(tab2)

        self.notebook = notebook
        self.tab1 = tab1
        self.tab2 = tab2

        # existence button
        existence = Button(root, text='Existence', command=self.existence)
        existence.pack(side=LEFT, padx=5, pady=5)

        # exemplify button
        exemplify = Button(root, text='Exemplify', command=self.exemplify)
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

        # reset button
        reset = Button(root, text='Reset', command=self.reset)
        reset.pack(side=RIGHT, padx=5, pady=5)

        root.mainloop()


if __name__ == '__main__':
    ui = ui()
    ui.run()