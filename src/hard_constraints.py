#!/usr/bin/python

from input_ui import InputUI
from table import Table
from tkinter import *
from tkinter import messagebox as mb

class HardConstraints(InputUI):
    """
    HardConstraints class represents hard constraint
    """

    def __init__(self, root):
        """
        Creates an initial GUI to display hard constraints and instantiates the class

        :param root tk root window or frame
        """
        self.count = 0
        self.constraints = []

        # Hard Constraints Frame and Scrollbars
        hc_frame = Frame(root)
        hc_frame.pack()

        Label(hc_frame, text="Hard Constraints").pack()

        hc_table_frame = Frame(hc_frame)
        hc_table_frame.pack()

        hc_scroll_y = Scrollbar(hc_table_frame)
        hc_scroll_y.pack(side=RIGHT, fill=Y)

        hc_scroll_x = Scrollbar(hc_table_frame,orient='horizontal')
        hc_scroll_x.pack(side=BOTTOM, fill=X)

        hc = Table(hc_table_frame, height=7,
                   yscrollcommand=hc_scroll_y.set,
                   xscrollcommand=hc_scroll_x.set)
        hc.pack(fill='x')

        hc_scroll_y.config(command=hc.yview)
        hc_scroll_x.config(command=hc.xview)

        # Hard Constraints Columns
        hc['columns']= ('number', 'constraint')
        hc.column("#0", width=0,  stretch=NO)
        hc.column("number",anchor=CENTER, width=50)
        hc.column("constraint",anchor=CENTER, width=380)

        # Hard Contraints Headings
        hc.heading("#0",text="",anchor=CENTER)
        hc.heading("number",text="Const #",anchor=CENTER)
        hc.heading("constraint",text="Constraint",anchor=CENTER)

        input_frame = Frame(hc_frame)
        input_frame.pack()

        self.hc = hc

        Label(input_frame,text="Constraint").grid(row=0,column=0)

        self.constraint_entry = Entry(input_frame)
        self.constraint_entry.grid(row=0,column=1)

        input_button = Button(hc_frame,
                              text = "Add Constraint",
                              command = self.getInput)
        input_button.pack(side=LEFT, padx=5, pady=5)

        open_file = Button(hc_frame, text='Open File', command=self.openFileCallback)
        open_file.pack(side=LEFT, padx=5, pady=5)

    def add(self, constraint):
        """
        Add a hard constraint to data structure and table

        :param constraint the hard constraint
        """
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
        """
        Method called from button to open file from dialog
        """
        file = super().openFile()

        if file == None:
            return

        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue
            self.add(line)


    def reset(self):
        """
        Reset table, count variable and data structure
        """
        self.count = 0
        self.hc.clear()
        self.constraints = []
