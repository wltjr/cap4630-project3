0#!/usr/bin/python

from table import Table
from tkinter import *

class PreferencesDisplay:
    """
    Preferences Display class displays the preference values for penalty logic,
    possibilistic logic, and qualitative choice logic
    """

    columnWidth = 50

    def __init__(self, root):
        """
        Creates an initial GUI to display preference values and totals

        :param root tk root window or frame
        """
        self.pen_count = 0
        self.poss_count = 0
        self.qual_count = 0
        self.penalties = []
        self.possibilistics = []
        self.qualitatives = []

        # Preferences Frame
        pref_frame = Frame(root)
        pref_frame.pack(side=LEFT, padx=(0,5), pady=5, fill=X, expand=1)

        # Penalty Frame and Scrollbars
        pen_frame = Frame(pref_frame)
        pen_frame.pack(fill=X)

        Label(pen_frame, text="Penalty Logic").pack()

        pen_table_frame = Frame(pen_frame)
        pen_table_frame.pack(fill=X)

        pen_scroll_y = Scrollbar(pen_table_frame)
        pen_scroll_y.pack(side=RIGHT, fill=Y)

        pen_scroll_x = Scrollbar(pen_table_frame,orient='horizontal')
        pen_scroll_x.pack(side=BOTTOM, fill=X)

        pen = Table(pen_table_frame, height=5,
                    yscrollcommand=pen_scroll_y.set,
                    xscrollcommand=pen_scroll_x.set,)
        pen.pack(fill='x')

        pen_scroll_y.config(command=pen.yview)
        pen_scroll_x.config(command=pen.xview)

        self.pen = pen
        self.addPenaltyColumn(0)

        # Possibilistic Frame and Scrollbars
        poss_frame = Frame(pref_frame)
        poss_frame.pack(fill=X)

        Label(poss_frame, text="Possibilistic Logic").pack()

        poss_table_frame = Frame(poss_frame)
        poss_table_frame.pack(fill=X)

        poss_scroll_y = Scrollbar(poss_table_frame)
        poss_scroll_y.pack(side=RIGHT, fill=Y)

        poss_scroll_x = Scrollbar(poss_table_frame,orient='horizontal')
        poss_scroll_x.pack(side=BOTTOM, fill=X)

        poss = Table(poss_table_frame, height=5,
                    yscrollcommand=poss_scroll_y.set,
                    xscrollcommand=poss_scroll_x.set,)
        poss.pack(fill='x')

        poss_scroll_y.config(command=poss.yview)
        poss_scroll_x.config(command=poss.xview)

        self.poss = poss
        self.addPossibiliticColumn(0)

        # Qualitative Frame and Scrollbars
        qual_frame = Frame(pref_frame)
        qual_frame.pack(fill=X)

        Label(qual_frame, text="Qualitative Logic").pack()

        qual_table_frame = Frame(qual_frame)
        qual_table_frame.pack(fill=X)

        qual_scroll_y = Scrollbar(qual_table_frame)
        qual_scroll_y.pack(side=RIGHT, fill=Y)

        qual_scroll_x = Scrollbar(qual_table_frame,orient='horizontal')
        qual_scroll_x.pack(side=BOTTOM, fill=X)

        qual = Table(qual_table_frame, height=5,
                    yscrollcommand=qual_scroll_y.set,
                    xscrollcommand=qual_scroll_x.set,)
        qual.pack(fill='x')

        qual_scroll_y.config(command=qual.yview)
        qual_scroll_x.config(command=qual.xview)

        self.qual = qual
        self.addQualitativeColumn(0)

    def clear(self):
        """
        Clear all tables and reset count variables
        """
        self.pen_count = 0
        self.poss_count = 0
        self.qual_count = 0
        self.pen.clear()
        self.poss.clear()
        self.qual.clear()

    def reset(self):
        self.clear()
        self.addPenaltyColumn(0)
        self.addPossibiliticColumn(0)
        self.addQualitativeColumn(0)

    def addPenaltyColumn(self, number):
        self.addColumn(self.pen, True, number)

    def addPossibiliticColumn(self, number):
        self.addColumn(self.poss, True, number)

    def addQualitativeColumn(self, number):
        self.addColumn(self.qual, False, number)

    def addColumn(self, table, hasTotal, number):
        if number > 0:
            prefNumber = "pref" + str(number)
            table['columns'] = tuple(sorted(list(table['columns']) + [prefNumber]))
        else:
            if hasTotal:
                table['columns'] = ('objectNumber', 'total')
            else:
                table['columns'] = ('objectNumber')

        table.column("#0", width=0,  stretch=NO)
        table.column("objectNumber", anchor=CENTER, width=self.columnWidth)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("objectNumber",text="Obj #",anchor=CENTER)

        for i in range(1, number+1):
            prefNumber = "pref" + str(i)
            table.column(prefNumber, anchor=CENTER, width=self.columnWidth)
            table.heading(prefNumber, text="Pref " + str(i), anchor=CENTER)

        if hasTotal:
            table.column("total", anchor=CENTER, width=self.columnWidth)
            table.heading("total",text="Total",anchor=CENTER)


    def addPenalty(self, valuesList):
        self.pen_count += 1
        self.penalties.append(valuesList)
        self.pen.insert(parent='',index='end',iid=self.pen_count-1,text='',
                        values=valuesList)


    def addPossibilistic(self, valuesList):
        self.poss_count += 1
        self.possibilistics.append(valuesList)
        self.poss.insert(parent='',index='end',iid=self.poss_count-1,text='',
                        values=valuesList)
                        

    def addQualititative(self, valuesList):
        self.qual_count += 1
        self.qualitatives.append(valuesList)
        self.qual.insert(parent='',index='end',iid=self.qual_count-1,text='',
                        values=valuesList)
