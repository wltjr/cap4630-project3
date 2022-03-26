#!/usr/bin/python

from abc import ABC, abstractmethod
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
        """
        filename = fd.askopenfilename(initialdir="../files/",
                                      title=("Select "+self.__class__.__name__+ " File"))

        if filename == () or filename == "":
            return

        try:
            file = open(filename, "r")
        except IOError:
            mb.showerror("Error File Not Found",
                         "The file %s was not found, aborting." % filename)
            return

        self.filename = filename
        return file

    @abstractmethod
    def openFileCallback(self):
        pass
