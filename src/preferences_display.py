0#!/usr/bin/python

import re
from input_ui import InputUI
from table import Table
from tkinter import *
from tkinter import messagebox as mb

class PreferencesDisplay:
    """
    Preferences Display class displays the preference values for penalty logic,
    possibilistic logic, and qualitative choice logic
    """

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
        pref_frame.pack(side=LEFT, padx=5, pady=5)

        # Penalty Frame and Scrollbars
        pen_frame = Frame(pref_frame)
        pen_frame.pack()

        Label(pen_frame, text="Penalty Logic").pack()

        pen_table_frame = Frame(pen_frame)
        pen_table_frame.pack()

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

        # Penality Columns
        pen['columns'] = ('number', 'object1', 'object2')
        pen.column("#0", width=0,  stretch=NO)
        pen.column("number", anchor=CENTER, width=60)
        pen.column("object1", anchor=CENTER, width=60)
        pen.column("object2", anchor=CENTER, width=60)

        # Penality Headings
        pen.heading("#0",text="",anchor=CENTER)
        pen.heading("number",text="Pref #",anchor=CENTER)
        pen.heading("object1",text="Object 1",anchor=CENTER)
        pen.heading("object2",text="Object 2",anchor=CENTER)

        pen_total_frame = Frame(pen_frame)
        pen_total_frame.pack(side=RIGHT, padx=(0,10))

        Label(pen_total_frame,text="Total").grid(row=0,column=0,padx=(0,5))

        self.pen_object1_total = Entry(pen_total_frame, state='disabled', width=11)
        self.pen_object1_total.grid(row=0,column=1)
        self.pen_object2_total = Entry(pen_total_frame, state='disabled', width=11)
        self.pen_object2_total.grid(row=0,column=2)

        self.pen = pen

        # Possibilistic Frame and Scrollbars
        poss_frame = Frame(pref_frame)
        poss_frame.pack()

        Label(poss_frame, text="Possibilistic Logic").pack()

        poss_table_frame = Frame(poss_frame)
        poss_table_frame.pack()

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

        # Possibilistic Columns
        poss['columns'] = ('number', 'object1', 'object2')
        poss.column("#0", width=0,  stretch=NO)
        poss.column("number", anchor=CENTER, width=60)
        poss.column("object1", anchor=CENTER, width=60)
        poss.column("object2", anchor=CENTER, width=60)

        # Possibilistic Headings
        poss.heading("#0",text="",anchor=CENTER)
        poss.heading("number",text="Pref #",anchor=CENTER)
        poss.heading("object1",text="Object 1",anchor=CENTER)
        poss.heading("object2",text="Object 2",anchor=CENTER)

        poss_total_frame = Frame(poss_frame)
        poss_total_frame.pack(side=RIGHT, padx=(0,10))

        Label(poss_total_frame,text="Total").grid(row=0,column=0,padx=(0,5))

        self.poss_object1_total = Entry(poss_total_frame, state='disabled', width=11)
        self.poss_object1_total.grid(row=0,column=1)
        self.poss_object2_total = Entry(poss_total_frame, state='disabled', width=11)
        self.poss_object2_total.grid(row=0,column=2)

        self.poss = poss

        # Qualitative Frame and Scrollbars
        qual_frame = Frame(pref_frame)
        qual_frame.pack()

        Label(qual_frame, text="Qualitative Logic").pack()

        qual_table_frame = Frame(qual_frame)
        qual_table_frame.pack()

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

        # Qualitative Columns
        qual['columns'] = ('number', 'object1', 'object2')
        qual.column("#0", width=0,  stretch=NO)
        qual.column("number", anchor=CENTER, width=60)
        qual.column("object1", anchor=CENTER, width=60)
        qual.column("object2", anchor=CENTER, width=60)

        # Qualitative Headings
        qual.heading("#0",text="",anchor=CENTER)
        qual.heading("number",text="Pref #",anchor=CENTER)
        qual.heading("object1",text="Object 1",anchor=CENTER)
        qual.heading("object2",text="Object 2",anchor=CENTER)

        self.qual = qual


    def addPenalty(self, number, value1, value2):
        self.pen_count += 1
        self.penalties.append((number, value1, value2))
        self.pen.insert(parent='',index='end',iid=self.pen_count-1,text='',
                        values=(number, value1, value2))


    def addPossibilistic(self, number, value1, value2):
        self.poss_count += 1
        self.possibilistics.append((number, value1, value2))
        self.poss.insert(parent='',index='end',iid=self.poss_count-1,text='',
                        values=(number, value1, value2))
                        

    def addQualititative(self, number, value1, value2):
        self.qual_count += 1
        self.qualitatives.append((number, value1, value2))
        self.qual.insert(parent='',index='end',iid=self.qual_count-1,text='',
                        values=(number, value1, value2))
