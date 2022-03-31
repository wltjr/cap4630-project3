#!/usr/bin/python

from tkinter import *
from table import Table

class TasksDisplay:
    """
    TaskDisplay class to display various tasks output, object table
    """

    count = 0
    defaultFeasibleLabel = "0 Feasible Objects"
    objects = {}

    def __init__(self, root):
        """
        Creates an initial GUI to display tasks output and instantiates the class

        :param root tk root window or frame
        """

        # Task Display Frame and Scrollbars
        td_frame = Frame(root)
        td_frame.pack()

        self.td_label = Label(td_frame, text=self.defaultFeasibleLabel)
        self.td_label.pack()

        td_table_frame = Frame(td_frame)
        td_table_frame.pack()

        td_scroll_y = Scrollbar(td_table_frame)
        td_scroll_y.pack(side=RIGHT, fill=Y)

        td_scroll_x = Scrollbar(td_table_frame,orient='horizontal')
        td_scroll_x.pack(side=BOTTOM,fill=X)

        td = Table(td_table_frame, height=5,
                   yscrollcommand=td_scroll_y.set,
                   xscrollcommand =td_scroll_x.set)
        td.pack(fill='x')

        td_scroll_y.config(command=td.yview)
        td_scroll_x.config(command=td.xview)

        # Feasible Objects Columns
        td['columns']= ('number', 'clasp', 'object')
        td.column("#0", width=0,  stretch=NO)
        td.column("number",anchor=CENTER, width=40)
        td.column("clasp",anchor=CENTER, width=110)
        td.column("object",anchor=CENTER, width=280)

        # Feasible Objects Headings
        td.heading("#0",text="",anchor=CENTER)
        td.heading("number",text="Obj #",anchor=CENTER)
        td.heading("clasp",text="Clasp",anchor=CENTER)
        td.heading("object",text="Object",anchor=CENTER)

        self.td = td

    def add(self, clasp, object):
        """
        Add an object to table and update label on count of objects

        :param clasp a representation of the object in clasp format
        :param object a representation of the object in human readable format
        """
        self.count += 1
        self.objects[self.count] = [self.count, clasp, object]
        self.td.insert(parent='',index='end',iid=self.count-1,text='',
                       values=(self.count, clasp, object))
        self.td_label.config(text=str(self.count)+self.defaultFeasibleLabel[1:])

    def clearTable(self):
        """
        Clear/reset table, count variable and label
        """
        self.td_label.config(text=self.defaultFeasibleLabel)
        self.count = 0
        self.td.clear()

