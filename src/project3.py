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
import random

class ui:
    """
    User Interface class displays GUI for the project and is the main class
    """

    penalties = {}
    possibilistic = {}
    qualitative = {}
    solutions = []

    opt_qualit = []

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

        self.clasp = clasp
        self.solutions = solutions

        self.notebook.select(self.tab2)


    def exemplify(self):
        """
        Wraps the existence method and is used to compare two random objects
        to determine strict preference or equivalence among the two.
        """
        if self.preferences.pen_count == 0 or \
           self.preferences.poss_count == 0 or \
           self.preferences.qual_count == 0:
            mb.showerror("Empty Preferences Error",
                         "Please load or enter preferences")
            self.notebook.select(self.tab1)
            return

        self.existence()
        self.prefDisplay.clear()
        self.valueLogic(self.preferences.penalties, False)
        self.valueLogic(self.preferences.possibilistics, True)

        self.exmpDisplay.reset()

        obj1 = random.randint(1,self.tasks.count)
        obj2 = random.randint(1,self.tasks.count)
        while obj1 == obj2:
            obj2 = random.randint(1,self.tasks.count)

        preferences1 = [obj1]
        preferences2 = [obj2]
        if self.penalties[obj1] == self.penalties[obj2]:
            preferences1.append("equivalent")
            preferences2.append("equivalent")
        elif self.penalties[obj1] < self.penalties[obj2]:
            preferences1.append("preferred")
            preferences2.append("")
        else:
            preferences1.append("")
            preferences2.append("preferred")

        if self.possibilistic[obj1] == self.possibilistic[obj2]:
            preferences1.append("equivalent")
            preferences2.append("equivalent")
        elif self.possibilistic[obj1] > self.possibilistic[obj2]:
            preferences1.append("preferred")
            preferences2.append("")
        else:
            preferences1.append("")
            preferences2.append("preferred")

        self.exmpDisplay.add(preferences1)
        self.exmpDisplay.add(preferences2)

        self.qualLogic()

        self.penalties = dict(sorted(self.penalties.items(),
                                     key=lambda x:x[1]))
        self.possibilistic = dict(sorted(self.possibilistic.items(),
                                         key=lambda x:x[1],
                                         reverse=True))


    def omni_optimize(self):
        """
        Wraps the exemplify method and is used to list all optimal objects
        already found as part of exemplify operation
        """
        if len(self.penalties) == 0:
            self.exemplify()

        self.optimal.reset()

        value = -1
        for key, val in self.penalties.items():
            if value == -1:
                value = val
            if val != value:
                break
            self.optimal.addPenalty(self.tasks.objects[key])

        value = -1
        for key, val in self.possibilistic.items():
            if value == -1:
                value = val
            if val != value:
                break
            self.optimal.addPossibilistic(self.tasks.objects[key])

        for key in self.opt_qualit:
            self.optimal.addQualititative(self.tasks.objects[key])


    def optimize(self):
        """
        Wraps the exemplify method and is used to list the first optimal
        object already found as part of exemplify operation
        """
        if len(self.penalties) == 0:
            self.exemplify()

        if self.prefDisplay.pen_count == 0 or \
           self.prefDisplay.poss_count == 0:
            return

        self.optimal.reset()

        key = list(self.penalties.keys())[0]
        self.optimal.addPenalty(self.tasks.objects[key])

        key = list(self.possibilistic.keys())[0]
        self.optimal.addPossibilistic(self.tasks.objects[key])

        key = self.opt_qualit[0]
        self.optimal.addQualititative(self.tasks.objects[key])


    def valueLogic(self, pref_logic, bool):
        """
        Performs preference logic for penalty and possibilistic logics and
        displays the results in tables on the output tab.

        :param pref_logic a list of the preferences in english to be converted
                          to CNF in clasp numeric format
        :param bool       a boolean toggle variable to switch preferences
                          between penalty and possibilistic logic
        """
        prefs = []
        constrs = self.solutions

        for item in pref_logic:
            clauses = self.clauses + self.getClause(item[0])
            prefs.append(self.clasp.solve(0, self.attributes.count, clauses))

        for objNum, x in enumerate(constrs):
            points = []
            if bool:
                total = 1
            else:
                total = 0
            for count, y in enumerate(prefs):
                if bool:
                    pref = float(pref_logic[count][1])
                else:
                    pref = int(pref_logic[count][1])
                if x in y:
                    if bool:
                        points.append(1)
                        total = min(total, 1)
                    else:
                        points.append(0)
                else:
                    if bool:
                        value = round((1 - pref),1)
                        points.append(value)
                        total = min(total, value)
                    else:
                        points.append(pref)
                        total = total + pref
            objNum += 1
            if bool:
                self.prefDisplay.addPossibilistic([objNum] + points + [total])
                self.possibilistic[objNum] = total
            else:
                self.prefDisplay.addPenalty([objNum] + points + [total])
                self.penalties[objNum] = total

    def qualLogic(self):
        attr = self.attributes.attributes

        qual_table = []
        self.opt_qualit = []

        for item in self.preferences.qualitatives:
            item = re.split(' ', item)

            qual_temp = []
            pref_const = []
            pref_const2 = []

            for count, x in enumerate(item):
                if item[count - 1] == "NOT":
                    try:
                        index = -(list(attr.keys())
                                  [list(attr.values()).index(x)])
                    except ValueError:
                        continue
                    pref_const.append(index)
                elif(x == "AND"):
                    pref_const2.append(pref_const)
                    pref_const = []
                elif(x == "BT"):
                    pref_const2.append(pref_const)
                    pref_const = []
                    pref_const2.append("BT")
                elif(x == "IF"):
                    pref_const2.append(pref_const)
                    pref_const = []
                    pref_const2.append("IF")
                elif(x != "OR") and (x != "NOT"):
                    try:
                        index = list(attr.keys())[list(attr.values()).index(x)]
                    except ValueError:
                        continue
                    pref_const.append(index)

            pref_const2.append(pref_const)

            for x in self.solutions:
                qual_countr = 1
                qual_bool = True

                for y in reversed(pref_const2):
                    if y == "IF":
                        if qual_bool == False:
                            qual_temp.append(float('inf'))
                        break
                    if qual_bool == False or len(y) == 0:
                        continue

                    qual_bool = any(z in x for z in y)

                if qual_bool == False:
                    continue

                for y in pref_const2:
                    if y == "IF":
                        if qual_bool == False:
                            qual_temp.append(float('inf'))
                        else:
                            qual_temp.append(qual_countr)
                        break
                    elif y == "BT":
                        if qual_bool == False:
                            qual_countr += 1
                            qual_bool = True
                            continue
                        else:
                            qual_temp.append(qual_countr)
                            break
                    if qual_bool == False:
                        continue

                    qual_bool = any(z in x for z in y)
            qual_table.append(qual_temp)

        # transposes qualitative list
        qual_table = list(zip(*qual_table))

        # next three function blocks handles qualitative optimization
        for objNum in range(1, len(qual_table) + 1):
            self.prefDisplay.addQualititative([objNum] + list(qual_table[objNum-1]))
            self.qualitative[objNum] = qual_table[objNum-1]
            self.opt_qualit.append(objNum)

        for x_idx, x in enumerate(qual_table):
            for y_idx, y in enumerate(qual_table):
                if x == y:
                    continue
                else:
                    ob1_count = 0
                    ob2_count = 0
                    for z, degree in enumerate(qual_table[x_idx]):
                        if degree == qual_table[y_idx][z]:
                            continue
                        if degree < qual_table[y_idx][z]:
                            ob1_count += 1
                        else:
                            ob2_count += 1
                    if ob1_count > 0 and ob2_count > 0:  # incomparable
                        continue
                    elif ob1_count > ob2_count:
                        if y_idx + 1 in self.opt_qualit:
                            self.opt_qualit.remove(y_idx + 1)
                    elif ob2_count < ob2_count:
                        if x_idx + 1 in self.opt_qualit:
                            self.opt_qualit.remove(x_idx + 1)


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
        notebook.pack(expand = 1, fill ="both")

        # wrapper frames
        frame = Frame(tab1)

        objects_frame = Frame(tab2)
        self.tasks = TasksDisplay(objects_frame)
        self.optimal = OptimalDisplay(objects_frame)
        objects_frame.pack(side=LEFT, padx=5)
        preferences_frame = Frame(tab2)
        self.prefDisplay = PreferencesDisplay(preferences_frame)
        self.exmpDisplay = ExemplifyDisplay(preferences_frame)
        preferences_frame.pack(side=LEFT, padx=(0,5))

        # main UI, tables and forms
        group_frame = Frame(frame)
        self.attributes = Attributes(group_frame)
        self.constraints = HardConstraints(group_frame)
        group_frame.pack(side=LEFT, padx=5)
        self.preferences = Preferences(frame, self.prefDisplay)
        frame.pack(padx=(0,5))

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
        omni_optimize = Button(root, text='Omni-optimize', command=self.omni_optimize)
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