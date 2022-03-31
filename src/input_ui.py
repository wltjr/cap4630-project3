#!/usr/bin/python

from abc import ABC, abstractmethod
from os import path
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class InputUI(ABC):
    """
    InputUI class is a base class with abstract methods for other class to
    extend and implement 
    """

    def openFile(self):
        """
        Open file selection dialog, base implementation to be called and
        extended by base classes

        :return the opened file handle, or None if an exception occurs
        """
        initialdir = "."
        if path.isdir("files"):
            initialdir = "files"
        elif path.isdir("../files"):
            initialdir = "../files"
        filename = fd.askopenfilename(filetypes=[("Text files","*.txt")],
                                      initialdir=initialdir,
                                      title=("Select "+self.__class__.__name__+ " File"))

        if filename == () or filename == "":
            return

        try:
            file = open(filename, "r")
        except IOError:
            mb.showerror("Error File Not Found",
                         "The file %s was not found, aborting." % filename)
            return

        self.reset()

        self.filename = filename
        return file

    @abstractmethod
    def openFileCallback(self):
        """
        Abstract file open callback method to be implemented and used by
        derived classes
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Abstract reset method to be implemented and used by derived classes
        """
        pass
