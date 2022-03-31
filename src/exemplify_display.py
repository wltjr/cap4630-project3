#!/usr/bin/python

from tkinter import *
from table import Table

class ExemplifyDisplay:
    """
    ExemplifyDisplay class to display exemplification of objects
    """

    count = 0

    def __init__(self, root):
        """
        Creates an initial GUI to display exemplification of objects and
        instantiates the class

        :param root tk root window or frame
        """

        # Exemplification Display Frame and Scrollbars
        exp_frame = Frame(root)
        exp_frame.pack()

        Label(exp_frame, text="Exemplification").pack()

        exp_table_frame = Frame(exp_frame)
        exp_table_frame.pack()

        exp_scroll_y = Scrollbar(exp_table_frame)
        exp_scroll_y.pack(side=RIGHT, fill=Y)

        exp_scroll_x = Scrollbar(exp_table_frame,orient='horizontal')
        exp_scroll_x.pack(side=BOTTOM,fill=X)

        exp = Table(exp_table_frame, height=5,
                   yscrollcommand=exp_scroll_y.set,
                   xscrollcommand =exp_scroll_x.set)
        exp.pack(fill='x')

        exp_scroll_y.config(command=exp.yview)
        exp_scroll_x.config(command=exp.xview)

        # Exemplified Objects Columns
        exp['columns']= ('number', 'penalty', 'possibilistic', 'qualitative')
        exp.column("#0", width=0,  stretch=NO)
        exp.column("number",anchor=CENTER, width=40)
        exp.column("penalty",anchor=CENTER, width=120)
        exp.column("possibilistic",anchor=CENTER, width=120)
        exp.column("qualitative",anchor=CENTER, width=120)

        # Exemplified Objects Headings
        exp.heading("#0",text="",anchor=CENTER)
        exp.heading("number",text="Obj #",anchor=CENTER)
        exp.heading("penalty",text="Penalty",anchor=CENTER)
        exp.heading("possibilistic",text="Possibilistic",anchor=CENTER)
        exp.heading("qualitative",text="Qualitative",anchor=CENTER)

        self.exp = exp

    def add(self, valuesList):
        """
        Add an attribute to table from a list of values, one for each column
        in the table

        :param valuesList a list of values one for each column in the table
        """
        self.count += 1
        self.exp.insert(parent='',index='end',iid=self.count-1,text='',
                       values=(valuesList))

    def reset(self):
        """
        Reset table and count variable
        """
        self.count = 0
        self.exp.clear()

