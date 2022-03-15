#!/usr/bin/python

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class HardConstraints:
    """
    HardConstraints class represents hard constraint
    """

    def __init__(self, root):
        """
        Creates an initial GUI to display attributes and instantiates the class

        :param root tk root window
        """
        self.count = 0
        self.constraints = []

        # Hard Constraints Frame and Scrollbars
        hc_frame = Frame(root)
        hc_frame.pack()

        hc_scroll = Scrollbar(hc_frame)
        hc_scroll.pack(side=RIGHT, fill=Y)

        hc_scroll = Scrollbar(hc_frame,orient='horizontal')
        hc_scroll.pack(side= BOTTOM,fill=X)

        hc = ttk.Treeview(hc_frame, height=5,
                          yscrollcommand=hc_scroll.set,
                          xscrollcommand =hc_scroll.set)
        hc.pack(fill='x')

        hc_scroll.config(command=hc.yview)
        hc_scroll.config(command=hc.xview)

        # Hard Constraints Columns
        hc['columns']= ('number', 'constraint')
        hc.column("#0", width=0,  stretch=NO)
        hc.column("number",anchor=CENTER, width=80)
        hc.column("constraint",anchor=CENTER, width=240)

        # Hard Contraints Headings
        hc.heading("#0",text="",anchor=CENTER)
        hc.heading("number",text="Const #",anchor=CENTER)
        hc.heading("constraint",text="Constraint",anchor=CENTER)

        input_frame = Frame(root)
        input_frame.pack()

        self.hc = hc

        Label(input_frame,text="Constraint").grid(row=0,column=0)

        self.constraint_entry = Entry(input_frame)
        self.constraint_entry.grid(row=0,column=1)

        input_button = Button(root,
                              text = "Add Constraint",
                              command = self.getInput)
        input_button.pack()

        open_file = Button(root, text='Open File', command=self.openFileCallback)
#        open_file.pack(side=LEFT, padx=5, pady=5)
        open_file.pack()

    def add(self, constraint):
        self.count += 1
        self.constraints.append(constraint)
        self.hc.insert(parent='',index='end',iid=self.count-1,text='',
                       values=(self.count, constraint))


    def getInput(self):
        """
        Get constraint input from user via GUI
        """
        if self.constraint_entry.get() == "":
            mb.showerror("Error", "Constraint value is required")
            return

        self.add(self.constraint_entry.get())

        self.constraint_entry.delete(0,END)


    def openFileCallback(self):
        filename = fd.askopenfilename()

        try:
            file = open(filename, "r")
        except IOError:
            print ("The file %s was not found, aborting." % filename)
            exit()

        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue
            self.add(line)

