#!/usr/bin/python

from attributes import *
from clasp import *
from hard_constraints import *
from exemplify_display import *
from optimal_display import *
from preferences import *
from preferences_display import *
from tasks_display import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
import copy
import random
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> b2d0b3ee572c9ee1e9dc11d84c35ca258197c7b6
=======
>>>>>>> b2d0b3ee572c9ee1e9dc11d84c35ca258197c7b6
=======
>>>>>>> b2d0b3ee572c9ee1e9dc11d84c35ca258197c7b6

class ui:
    """
    User Interface class displays GUI for the project and is the main class
    """

    penalties = {}
    possibilistic = {}
    solutions = []

    penal = {}
    possy = {}
    qualit = {}
    opt_penal = {}
    opt_possy = {}
    opt_qualit = {}

    penal = {}
    possy = {}
    qualit = {}
    opt_penal = {}
    opt_possy = {}
    opt_qualit = {}


    penal = {}
    possy = {}
    qualit = {}
    opt_penal = {}
    opt_possy = {}
    opt_qualit = {}


    penal = {}
    possy = {}
    qualit = {}
    opt_penal = {}
    opt_possy = {}
    opt_qualit = {}


    def getClause(self, string):
        """
        Converts a string like this OR that AND something OR something_else
        into a numeric CNF clasp formatted for processing by clasp

        :param string a string to be converted to CNF in clasp format
        :return a list of clauses in clasp format
        """
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
        """
        Invokes clasp to find feasible objects among the attributes based on
        hard constraints and displays the results in a table on the output tab
        """
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

        for solution in self.prefClauses(self.constraints.constraints):
            text = ""
            for key in solution:
                text += self.attributes.getValueByKey(key) + " "
            text = text[:-1]
            self.tasks.add(solution, text)

        self.penaLogic(self.preferences.penalties)

        self.notebook.select(self.tab2)

    def prefClauses(self, pref):
        clauses = []
        for constrant in pref:
            for clause in self.getClause(constrant):
                clauses.append(clause)
        self.clauses = clauses

        clasp = Clasp()
        return clasp.solve(0, self.attributes.count, clauses)

    def penaLogic(self, pref_logic):
        prefs = []
        constrs = self.prefClauses(self.constraints.constraints)

        for item in pref_logic:
            constraints = copy.deepcopy(self.constraints.constraints)
            constraints.extend([item[0]])
            prefs.append(self.prefClauses(constraints))

        for x in prefs:
            print(x)

        for x in constrs:
            points = []
            for count, y in enumerate(prefs):
                pref = int(pref_logic[count][1])
                if x in y:
                    if pref < 1:
                        points.append(1)
                        print(x, 1)
                    else:
                        points.append(0)
                        print(x, 0)
                else:
                    if pref < 1:
                        points.append(1 - pref)
                        print(x, 1 - pref)
                    else:
                        points.append(pref)
                        print(x, pref)
            self.penal[tuple(x)] = points
            print()

        print(self.penal)

        libr = {}

        if(int(pref_logic[count][1]) >= 1):
            summ = float('inf')
            for item in self.penal.values():
                summ = min(summ, sum(item))

            for key, value in self.penal.items():
                if sum(value) == summ:
                    self.opt_penal[key] = value
            libr = self.opt_penal
        else:
            maxx = 0
            for item in self.penal.values():
                maxx = max(maxx, min(item))

            for key, value in self.penal.items():
                if min(value) == maxx:
                    self.opt_possy[key] = value
            libr = self.opt_possy

        print(libr)

    def exemplify(self):
        # self.existence()
        return

    def reset(self):
        """
        Reset all tables in the GUI
        """
        self.attributes.reset()
        self.constraints.reset()
        self.preferences.reset()
        self.tasks.clearTable()
        self.optimal.reset()
        self.prefDisplay.reset()

    def run(self):
        """
        Run the GUI create the root window, frames, and all GUI widgets
        """
        root = Tk()
        root.title('Project 3')

        notebook = Notebook(root)

        tab1 = Frame(notebook)
        tab2 = Frame(notebook)

        notebook.add(tab1, text="Input")
        notebook.add(tab2, text="Output")
        notebook.pack(expand=1, fill="both")

        # wrapper frames
        frame = Frame(tab1)

        objects_frame = Frame(tab2)
        self.tasks = TasksDisplay(objects_frame)
        self.optimal = OptimalDisplay(objects_frame)
        objects_frame.pack(side=LEFT, padx=5)
        preferences_frame = Frame(tab2)
        self.prefDisplay = PreferencesDisplay(preferences_frame)
        self.exmpDisplay = ExemplifyDisplay(preferences_frame)
        preferences_frame.pack(side=LEFT, padx=(0, 5))

        # main UI, tables and forms
        group_frame = Frame(frame)
        self.attributes = Attributes(group_frame)
        self.constraints = HardConstraints(group_frame)
        group_frame.pack(side=LEFT, padx=5)
        self.preferences = Preferences(frame, self.prefDisplay)
        frame.pack(padx=(0, 5))

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
        optimize = Button(root, text='Optimize', command=self.optimize)
        optimize.pack(side=LEFT, padx=5, pady=5)

        # omni-optimize button
        omni_optimize = Button(root, text='Omni-optimize',
                               command=self.omni_optimize)
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
