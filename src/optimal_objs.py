from clasp import *
from tkinter import messagebox as mb


class Objects:

    def __init__(self, tasks, notebook, tab1, tab2, attr, constrs):
        self.attributeCount = attr.count
        self.attributes = attr
        self.notebook = notebook
        self.tab1 = tab1
        self.tasks = tasks
        self.constraints = constrs
        self.tab2 = tab2

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
        if self.attributeCount == 0:
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

        clasp = Clasp()
        solutions = clasp.solve(0, self.attributeCount, clauses)
        for solution in solutions:
            text = ""
            for key in solution:
                text += self.attributes.getValueByKey(key) + " "
            text = text[:-1]
            self.tasks.add(solution, text)

        self.notebook.select(self.tab2)
