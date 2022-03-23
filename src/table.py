#!/usr/bin/python

from tkinter import ttk

class Table(ttk.Treeview):
    """
    Tree class extends tkinter TreeView class to add missing functionality
    """

    def clear(self):
        """
        Removes all rows from a TreeView, tkinter table
        """
        x = self.get_children()
        for item in x:
            self.delete(item)
