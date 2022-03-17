#!/bin/bash

import subprocess

def write(process, string):
    """
    Write a string to a process using stdin

    :param process a process to write the string to
    :param string a string to write to stdin
    """
#    process.stdin.write(bytes(string + '\n', "utf-8")) # legacy byte
#    process.stdin.write((string + '\n').encode()) # current byte
    process.stdin.write(string + '\n') # current

def writeHeader(process, objs_num, clauses_num):
    """
    Write a header for clasp to stdin

    :param process a process to write the clasp header to
    :param objs_num the number of objects
    :param clauses_num the number of clauses
    """
    write(process, "p cnf " + str(objs_num) + " " + str(clauses_num))

def writeRule(process, clause):
    """
    Write a clause to a clasp process using stdin, zero auto added to the end

    :param process a process to write the string to
    :param clause a clause to write to stdin
    """
    write(process, clause + " 0")

def stdoutParse(process):
    """
    Parse/handle the output in stdout from a clasp instance

    :param process a process to parse stdout from
    """
    for line in process.stdout.readlines():
        if line.startswith("c Answer:"):
            solution = set()
        if line[0] == 'v':
            solution = set(map(int, line[2:-2].split()))
            print(solution)
#        else:
#            print(line.rstrip())

def solve(num, objs_num, clauses):
    """
    Solve a problem using clasp

    :param num the number of models to solve
    :param objs_num the number of objects
    :param clauses a list of string clauses to be written to clasp via stdin
    """
    process = subprocess.Popen(("clasp " + str(num)).split(),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, text=True)
# uncomment for debug
#                              stdout=subprocess.PIPE) # requires byte return str

    writeHeader(process, objs_num, len(clauses))
    for c in clauses:
        writeRule(process, c)
    process.stdin.close()

    stdoutParse(process)


# beer AND beer OR beef AND salad (not soup)
clauses = ["-3", "-2 -3", "-1"]

solve(0,4, clauses)
