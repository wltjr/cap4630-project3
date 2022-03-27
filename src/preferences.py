0#!/usr/bin/python

import re
from input_ui import InputUI
from preferences_display import *
from table import Table
from tkinter import *
from tkinter import messagebox as mb

class Preferences(InputUI):
    """
    Preferences class represents user preferences for penalty logic,
    possibilistic logic, and qualitative choice logic
    """

    def __init__(self, root, prefDisplay):
        """
        Creates an initial GUI to display attributes and instantiates the class

        :param root tk root window or frame
        :param prefDisplay an instances of the PreferenceDisplay class
        """
        self.pen_count = 0
        self.poss_count = 0
        self.qual_count = 0
        self.penalties = []
        self.possibilistics = []
        self.qualitatives = []
        self.prefDisplay = prefDisplay

        # Preferences Frame
        pref_frame = Frame(root)
        pref_frame.pack()

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
        pen['columns']= ('number', 'reference', 'penalty')
        pen.column("#0", width=0,  stretch=NO)
        pen.column("number", anchor=CENTER, width=80)
        pen.column("reference", anchor=CENTER, width=240)
        pen.column("penalty", anchor=CENTER, width=80)

        # Penality Headings
        pen.heading("#0",text="",anchor=CENTER)
        pen.heading("number",text="Pref #",anchor=CENTER)
        pen.heading("reference",text="Preference",anchor=CENTER)
        pen.heading("penalty",text="Penalty",anchor=CENTER)

        self.pen = pen

        # Possibilistic Frame and Scrollbars
        poss_frame = Frame(pref_frame)
        poss_frame.pack(pady=5)

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
        poss['columns']= ('number', 'reference', 'tolerance')
        poss.column("#0", width=0,  stretch=NO)
        poss.column("number", anchor=CENTER, width=80)
        poss.column("reference", anchor=CENTER, width=240)
        poss.column("tolerance", anchor=CENTER, width=80)

        # Possibilistic Headings
        poss.heading("#0",text="",anchor=CENTER)
        poss.heading("number",text="Pref #",anchor=CENTER)
        poss.heading("reference",text="Preference",anchor=CENTER)
        poss.heading("tolerance",text="Tolerance",anchor=CENTER)

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
        qual['columns']= ('number', 'reference')
        qual.column("#0", width=0,  stretch=NO)
        qual.column("number", anchor=CENTER, width=80)
        qual.column("reference", anchor=CENTER, width=320)

        # Qualitative Headings
        qual.heading("#0",text="",anchor=CENTER)
        qual.heading("number",text="Pref #",anchor=CENTER)
        qual.heading("reference",text="Preference",anchor=CENTER)

        self.qual = qual

        input_frame = Frame(pref_frame)
        input_frame.pack()

        Label(input_frame,text="Preference").grid(row=0,column=0)
        Label(input_frame,text="Value").grid(row=0,column=1)

        self.preference_entry = Entry(input_frame)
        self.preference_entry.grid(row=1,column=0)

        self.penalty_entry = Entry(input_frame)
        self.penalty_entry.grid(row=1,column=1)

        input_button = Button(pref_frame,
                              text = "Add Preference",
                              command = self.getInput)
        input_button.pack(side=LEFT, padx=5, pady=5)

        open_file = Button(pref_frame,
                           text='Open File',
                           command=self.openFileCallback)
        open_file.pack(side=LEFT, padx=5, pady=5)


    def add(self, preference, value):
        # no value, qualitative logic
        if value == "":
            self.qual_count += 1
            self.qualitatives.append(preference)
            self.qual.insert(parent='',index='end',iid=self.qual_count-1,text='',
                             values=(self.qual_count, preference, ""))
            self.prefDisplay.addQualitativeColumn(self.qual_count)
        # value with decimal, possibilistic logic
        elif value.find('.') != -1:
            self.poss_count += 1
            self.possibilistics.append((preference,value))
            self.poss.insert(parent='',index='end',iid=self.poss_count-1,text='',
                             values=(self.poss_count, preference, value))
            self.prefDisplay.addPossibiliticColumn(self.poss_count)
        # otherwise penalty logic
        else:
            self.pen_count += 1
            self.penalties.append((preference,value))
            self.pen.insert(parent='',index='end',iid=self.pen_count-1,text='',
                            values=(self.pen_count, preference, value))
            self.prefDisplay.addPenaltyColumn(self.pen_count)

    def clear(self):
        """
        Clear all tables and reset count variables
        """
        self.qual_count = 0
        self.poss_count = 0
        self.pen_count = 0
        self.poss.clear()
        self.qual.clear()
        self.pen.clear()


    def getInput(self):
        """
        Get preferences input from user via GUI
        """
        if self.preference_entry.get() == "":
            mb.showerror("Error", "Preference value is required")
            return

        self.add(self.preference_entry.get(),
                 self.penalty_entry.get())

        self.preference_entry.delete(0,END)
        self.penalty_entry.delete(0,END)


    def openFileCallback(self):
        file = super().openFile()

        if file == None:
            return

        self.clear()

        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue
            elif line.find(',') != -1:
                values = re.split(r'[:,]', line[:-1])
                self.add(values[0],values[1])
            else:
                self.add(line,"")


    def reset(self):
        self.clear()
        self.penalties = []
        self.possibilistics = []
        self.qualitatives = []
