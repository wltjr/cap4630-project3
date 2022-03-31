#!/usr/bin/python

from table import Table
from tkinter import *

class OptimalDisplay:
    """
    Optimal Display class displays the optimal objects for each of the
    preferencs for penalty logic, possibilistic logic, and qualitative
    choice logic
    """

    defaultPenaltyLabel = "0 Optimal Penalty Objects"
    defaultPossibilisticLabel = "0 Optimal Possibilistic Objects"
    defaultQualitativeLabel = "0 Optimal Qualitative Objects"
    pen_count = 0
    poss_count = 0
    qual_count = 0
    tableHeight = 4

    def __init__(self, root):
        """
        Creates an initial GUI to display optimal objects

        :param root tk root window or frame
        """

        # Optimal Objects Frame
        opt_frame = Frame(root)
        opt_frame.pack()

        # Penalty Frame and Scrollbars
        pen_frame = Frame(opt_frame)
        pen_frame.pack()

        pen_label = Label(pen_frame, text=self.defaultPenaltyLabel)
        pen_label.pack()
        self.pen_label = pen_label

        pen_table_frame = Frame(pen_frame)
        pen_table_frame.pack()

        pen_scroll_y = Scrollbar(pen_table_frame)
        pen_scroll_y.pack(side=RIGHT, fill=Y)

        pen_scroll_x = Scrollbar(pen_table_frame,orient='horizontal')
        pen_scroll_x.pack(side=BOTTOM, fill=X)

        pen = Table(pen_table_frame, height=self.tableHeight,
                    yscrollcommand=pen_scroll_y.set,
                    xscrollcommand=pen_scroll_x.set,)
        pen.pack(fill='x')

        pen_scroll_y.config(command=pen.yview)
        pen_scroll_x.config(command=pen.xview)

        # Optimal Penalty Objects Columns
        pen['columns']= ('number', 'clasp', 'object')
        pen.column("#0", width=0,  stretch=NO)
        pen.column("number",anchor=CENTER, width=40)
        pen.column("clasp",anchor=CENTER, width=110)
        pen.column("object",anchor=CENTER, width=280)

        # Optimal Penalty Objects Headings
        pen.heading("#0",text="",anchor=CENTER)
        pen.heading("number",text="Obj #",anchor=CENTER)
        pen.heading("clasp",text="Clasp",anchor=CENTER)
        pen.heading("object",text="Object",anchor=CENTER)

        self.pen = pen

        # Possibilistic Frame and Scrollbars
        poss_frame = Frame(opt_frame)
        poss_frame.pack()

        poss_label = Label(poss_frame, text=self.defaultPossibilisticLabel)
        poss_label.pack()
        self.poss_label = poss_label

        poss_table_frame = Frame(poss_frame)
        poss_table_frame.pack()

        poss_scroll_y = Scrollbar(poss_table_frame)
        poss_scroll_y.pack(side=RIGHT, fill=Y)

        poss_scroll_x = Scrollbar(poss_table_frame,orient='horizontal')
        poss_scroll_x.pack(side=BOTTOM, fill=X)

        poss = Table(poss_table_frame, height=self.tableHeight,
                    yscrollcommand=poss_scroll_y.set,
                    xscrollcommand=poss_scroll_x.set,)
        poss.pack(fill='x')

        poss_scroll_y.config(command=poss.yview)
        poss_scroll_x.config(command=poss.xview)

        # Optimal Possibilistic Objects Columns
        poss['columns']= ('number', 'clasp', 'object')
        poss.column("#0", width=0,  stretch=NO)
        poss.column("number",anchor=CENTER, width=40)
        poss.column("clasp",anchor=CENTER, width=110)
        poss.column("object",anchor=CENTER, width=280)

        # Optimal Possibilistic Objects Headings
        poss.heading("#0",text="",anchor=CENTER)
        poss.heading("number",text="Obj #",anchor=CENTER)
        poss.heading("clasp",text="Clasp",anchor=CENTER)
        poss.heading("object",text="Object",anchor=CENTER)

        self.poss = poss

        # Qualitative Frame and Scrollbars
        qual_frame = Frame(opt_frame)
        qual_frame.pack()

        qual_label = Label(qual_frame, text=self.defaultQualitativeLabel)
        qual_label.pack()
        self.qual_label = qual_label

        qual_table_frame = Frame(qual_frame)
        qual_table_frame.pack()

        qual_scroll_y = Scrollbar(qual_table_frame)
        qual_scroll_y.pack(side=RIGHT, fill=Y)

        qual_scroll_x = Scrollbar(qual_table_frame,orient='horizontal')
        qual_scroll_x.pack(side=BOTTOM, fill=X)

        qual = Table(qual_table_frame, height=self.tableHeight,
                    yscrollcommand=qual_scroll_y.set,
                    xscrollcommand=qual_scroll_x.set,)
        qual.pack(fill='x')

        qual_scroll_y.config(command=qual.yview)
        qual_scroll_x.config(command=qual.xview)


        # Optimal Qualitative Objects Columns
        qual['columns']= ('number', 'clasp', 'object')
        qual.column("#0", width=0,  stretch=NO)
        qual.column("number",anchor=CENTER, width=40)
        qual.column("clasp",anchor=CENTER, width=110)
        qual.column("object",anchor=CENTER, width=280)

        # Optimal Qualitative Objects Headings
        qual.heading("#0",text="",anchor=CENTER)
        qual.heading("number",text="Obj #",anchor=CENTER)
        qual.heading("clasp",text="Clasp",anchor=CENTER)
        qual.heading("object",text="Object",anchor=CENTER)

        self.qual = qual


    def reset(self):
        """
        Reset all tables, count variables and reset labels in the GUI
        """
        self.pen_count = 0
        self.poss_count = 0
        self.qual_count = 0
        self.pen.clear()
        self.poss.clear()
        self.qual.clear()
        self.pen_label.config(text=self.defaultPenaltyLabel)
        self.poss_label.config(text=self.defaultPossibilisticLabel)
        self.qual_label.config(text=self.defaultQualitativeLabel)


    def addPenalty(self, valuesList):
        """
        Add row to optimal penalty table

        :param valuesList a list of values one for each column in the table
        """
        self.pen_count += 1
        self.pen.insert(parent='',index='end',iid=self.pen_count-1,text='',
                        values=valuesList)
        self.pen_label.config(text=str(self.pen_count)+self.defaultPenaltyLabel[1:])


    def addPossibilistic(self, valuesList):
        """
        Add row to optimal possibilistic table

        :param valuesList a list of values one for each column in the table
        """
        self.poss_count += 1
        self.poss.insert(parent='',index='end',iid=self.poss_count-1,text='',
                        values=valuesList)
        self.poss_label.config(text=str(self.poss_count)+self.defaultPossibilisticLabel[1:])
                        

    def addQualititative(self, valuesList):
        """
        Add row to optimal qualititative table

        :param valuesList a list of values one for each column in the table
        """
        self.qual_count += 1
        self.qual.insert(parent='',index='end',iid=self.qual_count-1,text='',
                        values=valuesList)
        self.qual_label.config(text=str(self.qual_count)+self.defaultQualitativeLabel[1:])
