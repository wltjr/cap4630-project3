#!/usr/bin/python

import os
import subprocess

class Clasp:
    """
    Clasp class wraps clasp binary
    """

    def __init__(self):
        self.process

    def getClasp():
        """
        Get the clasp binary based on the OS

        :return clasp binary either clasp.exe for windows or clasp linux/unix
        """
        if os.name == "nt":
            return "clasp.exe"
        return "clasp"

    def write(self, string):
        """
        Write a string to a process using stdin

        :param process a process to write the string to
        :param string a string to write to stdin
        """
        self.process.stdin.write(string + '\n')

    def writeHeader(self, objs_num, clauses_num):
        """
        Write a header for clasp to stdin

        :param process a process to write the clasp header to
        :param objs_num the number of objects
        :param clauses_num the number of clauses
        """
        self.write(self.process, "p cnf " + str(objs_num) + " " + str(clauses_num))

    def writeRule(self, clause):
        """
        Write a clause to a clasp process using stdin, zero auto added to the end

        :param process a process to write the string to
        :param clause a clause to write to stdin
        """
        self.write(self.process, clause + " 0")

    def solve(self, num, objs_num, clauses):
        """
        Solve a problem using clasp

        :param num the number of models to solve
        :param objs_num the number of objects
        :param clauses a list of string clauses to be written to clasp via stdin
        """
        self.process = subprocess.Popen((self.getClasp() + str(num)).split(),
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, text=True)
        solution = []
        self.writeHeader(self.process, objs_num, len(clauses))
        for c in clauses:
            self.writeRule(self.process, c)
        self.process.stdin.close()
        for line in self.process.stdout.readlines():
            if line[0] == 'v':
                solution.append(list(map(int, line[2:-2].split())))
        return solution
