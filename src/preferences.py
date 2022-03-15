0#!/usr/bin/python

import re
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class Preferences:
    """
    Preferences class represents user preferences for penalty logic,
    possibilistic logic, and qualitative choice logic
    """

    def __init__(self, root):
        """
        Creates an initial GUI to display attributes and instantiates the class

        :param root tk root window
        """
        self.pen_count = 0
        self.poss_count = 0
        self.qual_count = 0
        self.penalties = []
        self.possibilistics = []
        self.qualitatives = []

        # Preferences Frame
        pref_frame = Frame(root)
        pref_frame.pack()

        # Penalty Frame and Scrollbars
        pen_frame = Frame(pref_frame)
        pen_frame.pack()

        Label(pen_frame, text="Penalty Logic").pack()

        pen_table_frame = Frame(pen_frame)
        pen_table_frame.pack()

        pen_scroll = Scrollbar(pen_table_frame)
        pen_scroll.pack(side=RIGHT, fill=Y)

        pen_scroll = Scrollbar(pen_table_frame,orient='horizontal')
        pen_scroll.pack(side=BOTTOM, fill=X)

        pen = ttk.Treeview(pen_table_frame, height=5,
                           yscrollcommand=pen_scroll.set,
                           xscrollcommand=pen_scroll.set,)
        pen.pack(fill='x')

        pen_scroll.config(command=pen.yview)
        pen_scroll.config(command=pen.xview)

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
        poss_frame.pack()

        Label(poss_frame, text="Possibilistic Logic").pack()

        poss_table_frame = Frame(poss_frame)
        poss_table_frame.pack()

        poss_scroll = Scrollbar(poss_table_frame)
        poss_scroll.pack(side=RIGHT, fill=Y)

        poss_scroll = Scrollbar(poss_table_frame,orient='horizontal')
        poss_scroll.pack(side=BOTTOM, fill=X)

        poss = ttk.Treeview(poss_table_frame, height=5,
                            yscrollcommand=poss_scroll.set,
                            xscrollcommand=poss_scroll.set,)
        poss.pack(fill='x')

        poss_scroll.config(command=poss.yview)
        poss_scroll.config(command=poss.xview)

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

        qual_scroll = Scrollbar(qual_table_frame)
        qual_scroll.pack(side=RIGHT, fill=Y)

        qual_scroll = Scrollbar(qual_table_frame,orient='horizontal')
        qual_scroll.pack(side=BOTTOM, fill=X)

        qual = ttk.Treeview(qual_table_frame, height=5,
                            yscrollcommand=qual_scroll.set,
                            xscrollcommand=qual_scroll.set,)
        qual.pack(fill='x')

        qual_scroll.config(command=qual.yview)
        qual_scroll.config(command=qual.xview)

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
        # value with decimal, possibilistic logic
        elif value.find('.') != -1:
            self.poss_count += 1
            self.possibilistics.append((preference,value))
            self.poss.insert(parent='',index='end',iid=self.poss_count-1,text='',
                             values=(self.poss_count, preference, value))
        # otherwise penalty logic
        else:
            self.pen_count += 1
            self.penalties.append((preference,value))
            self.pen.insert(parent='',index='end',iid=self.pen_count-1,text='',
                            values=(self.pen_count, preference, value))


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
        filename = fd.askopenfilename()

        try:
            file = open(filename, "r")
        except IOError:
            print ("The file %s was not found, aborting." % filename)
            exit()

        for line in file:
            if line[0] == '\n' or line[0] == '#':
                continue
            elif line.find(',') != -1:
                values = re.split(r'[:,]', line[:-1])
                self.add(values[0],values[1])
            else:
                self.add(line,"")
