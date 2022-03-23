#!/usr/bin/python

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from table import Table

class TasksDisplay:
    """
    TaskDisplay class to display various tasks output, object table
    """

    def __init__(self, root):
        """
        Creates an initial GUI to display tasks output and instantiates the class

        :param root tk root window or frame
        """
        self.count = 0
        self.objects = []

        # Task Display Frame and Scrollbars
        td_frame = Frame(root)
        td_frame.pack()

        self.td_label = Label(td_frame, text="Objects").pack()

        td_table_frame = Frame(td_frame)
        td_table_frame.pack()

        td_scroll_y = Scrollbar(td_table_frame)
        td_scroll_y.pack(side=RIGHT, fill=Y)

        td_scroll_x = Scrollbar(td_table_frame,orient='horizontal')
        td_scroll_x.pack(side=BOTTOM,fill=X)

        td = Table(td_table_frame, height=7,
                   yscrollcommand=td_scroll_y.set,
                   xscrollcommand =td_scroll_x.set)
        td.pack(fill='x')

        td_scroll_y.config(command=td.yview)
        td_scroll_x.config(command=td.xview)

        # Feasible Objects Columns
        td['columns']= ('number', 'object')
        td.column("#0", width=0,  stretch=NO)
        td.column("number",anchor=CENTER, width=40)
        td.column("object",anchor=CENTER, width=390)

        # Feasible Objects Headings
        td.heading("#0",text="",anchor=CENTER)
        td.heading("number",text="Obj #",anchor=CENTER)
        td.heading("object",text="Object",anchor=CENTER)

        self.td = td

    def add(self, object):
        self.count += 1
        self.objects.append(object)
        self.td.insert(parent='',index='end',iid=self.count-1,text='',
                       values=(self.count, object))

    def clearTable(self):
        self.count = 0
        self.td.clear()

