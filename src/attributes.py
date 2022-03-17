#!/usr/bin/python

import re
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class Attributes:
    """
    Attributes class represents an attribute with binary options
    """

    def addAttribute(self, attribute, option1, option2):
        self.count += 1
        self.attributes[attribute] = (option1, option2)
        self.attr.insert(parent='',index='end',iid=self.count-1,text='',
                         values=(self.count, attribute, option1, option2))

    def inputAttribute(self):
        """
        Get attribute input from user via GUI
        """
        if self.attribute_entry.get() == "":
            mb.showerror("Error", "Attribute value is required")
            return

        if self.option1_entry.get() == "":
            mb.showerror("Error", "Option 1 value is required")
            return

        if self.option2_entry.get() == "":
            mb.showerror("Error", "Option 2 value is required")
            return

        self.addAttribute(self.attribute_entry.get(),
                          self.option1_entry.get(),
                          self.option2_entry.get())

        self.attribute_entry.delete(0,END)
        self.option1_entry.delete(0,END)
        self.option2_entry.delete(0,END)


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
            values = re.split(r'[:,]', line[:-1])
            self.addAttribute(values[0], values[1].lstrip(), values[2].lstrip())


    def __init__(self, root):
        """
        Creates an initial GUI to display attributes and instantiates the class

        :param root tk root window
        """
        self.count = 0
        self.attributes = {}

        # Attribute Frame and Scrollbars
        attr_frame = Frame(root)
        attr_frame.pack()
        
        Label(attr_frame, text="Binary Attributes").pack()

        attr_table_frame = Frame(attr_frame)
        attr_table_frame.pack()

        attr_scroll = Scrollbar(attr_table_frame)
        attr_scroll.pack(side=RIGHT, fill=Y)

        attr_scroll = Scrollbar(attr_table_frame,orient='horizontal')
        attr_scroll.pack(side= BOTTOM,fill=X)

        attr = ttk.Treeview(attr_table_frame, height=7,
                            yscrollcommand=attr_scroll.set,
                            xscrollcommand =attr_scroll.set)
        attr.pack(fill='x')

        attr_scroll.config(command=attr.yview)
        attr_scroll.config(command=attr.xview)

        # Attribute Columns
        attr['columns']= ('number', 'attribute','option_1', 'option_2')
        attr.column("#0", width=0,  stretch=NO)
        attr.column("number",anchor=CENTER, width=40)
        attr.column("attribute",anchor=CENTER, width=130)
        attr.column("option_1",anchor=CENTER, width=130)
        attr.column("option_2",anchor=CENTER, width=130)

        # Atribute Headings
        attr.heading("#0",text="",anchor=CENTER)
        attr.heading("number",text="Attr #",anchor=CENTER)
        attr.heading("attribute",text="Attribute",anchor=CENTER)
        attr.heading("option_1",text="Option 1",anchor=CENTER)
        attr.heading("option_2",text="Option 2",anchor=CENTER)

        self.attr = attr

        input_frame = Frame(attr_frame)
        input_frame.pack()

        attribute = Label(input_frame,text="Attribute")
        attribute.grid(row=0,column=0)

        option1 = Label(input_frame,text="Option 1")
        option1.grid(row=0,column=1)

        option2 = Label(input_frame,text="Option 2")
        option2.grid(row=0,column=2)

        self.attribute_entry = Entry(input_frame)
        self.attribute_entry.grid(row=1,column=0)

        self.option1_entry = Entry(input_frame)
        self.option1_entry.grid(row=1,column=1)

        self.option2_entry = Entry(input_frame)
        self.option2_entry.grid(row=1,column=2)

        input_button = Button(attr_frame,
                              text = "Add Attribute",
                              command = self.inputAttribute)
        input_button.pack(side=LEFT, padx=5, pady=5)

        open_file = Button(attr_frame, text='Open File', command=self.openFileCallback)
        open_file.pack(side=LEFT, padx=5, pady=5)
