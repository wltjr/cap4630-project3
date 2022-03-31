# CAP4630 Intro to Artificial Intelligence Project 3 <br> A Knowledge-based Intelligent System

## About
Project3 is a knowledge-based intelligent system that collects user
preferences, attributes, and constraints, then computes the existence of all
feasible objects, exemplification of two random objects, optimization, and
omni-optimization for penalty, possiblistic, and qualitative logics.

## System Requirements
The following software is required for proper operation

  [Python >= 3.9](https://www.python.org/downloads/)  
  [Tkinter >= 8.6](https://docs.python.org/3/library/tkinter.html)  
  [Tcl/Tk >= 8.6](https://www.tcl.tk/software/tcltk/)  
  [clasp >= 3.3.2](https://github.com/potassco/clasp/releases)  

**Note**: clasp binary must be available via system `PATH` variable

## Directory Structure
The project has been split into the following folders

### doc/ 
contains project documentation, latex report.tex for the report.pdf and
description of the various test files in the files directory

### exp/
contains experiments conducted as part of the learning process for the
project, experimental python scripts/programs

### files/
contains various attribute, constraint, and preference test files to be
used within the program

### src/
contains the source code files for the project and the main program
`project3.py` for execution

## Installation
Installation is not required for usage and operation of the program,
simply download and unpack an archive of the project.

## Building
Building is not required for usage and operation of the program,
simply run `python project3.py` as instructed in the following section.

## Running
In order to run the program navigate to `cap4630-project3/`
(or the directory the project was unpacked into) in a terminal and run

```sh
python src/project3.py
```

Or navigate to `cap4630-project3/src/`
(the src directory in the unpacked archive directory) in a terminal and run

```sh
python project3.py
```

When that command is run the GUI should initialize and start the program.

## Test/Sample files
Test/sample files containing attributes, constraints, and preferences can be
found in the `files` directory. They are in sets with the same suffix such as
`*1.txt`, `*_hw.txt`, and `*_test.txt`.

### Note/Warning
**Only files with the same suffix should be loaded and used together!**

## Operation and Usage
Proper operation and usage requires attributes, constraints, and preference
logic. These can be loaded from files, and/or inputted manually using the
fields on the input tab. Output is provided on the output tab, which is
automatically focused on press of any of the task buttons. Basic operation
and usage is a follows:

1. On the input tab, open a attributes file using the open file button,
   or input one or more attribute(s) manually  
   (**Note:** test attributes files are in the `files` directory)

2. On the input tab, open a contstraints file using the open file button,
   or input one or more contstraint(s) manually  
   (**Note:** test contstraints files are in the `files` directory)

3. On the input tab, open a preferences file using the open file button,
   or input one or more preference(s) for each preference manually  
   (**Note:** test preferences files are in the `files` directory)

4. From any tab, press Existence button to generate the feasible
   objects displayed the output tab

5. From any tab, press Exemplify for exemplification of two random objects
   for each of the three preference logics  
   (**Note:** each button press generates a new random comparison)

6. From any tab, press Optimize for a single optimal object for each of the
   three preference logics

7. From any tab, press Omni-optimize for all optimal objects for each of the
   three preference logics

Each button can be pressed one or more times. A reset button is provided to
reset all fields and tables for multiple runs using different files/input.
A quit button is provided for convenience as an alternative to normal window
closure.

### Notes
Pressing omni-optimize button runs all other tasks, existence and exemplify;
a quick and easy way to see all functionality from a single button press.  
The only difference between optimize and omni-optimize buttons are one vs
all optimal objects.  
Files for attributes, constraints, and preferences are located in the `files`
directory

For additional information on operation and usage please refer to
`docs/report.pdf` for detailed instructions with screenshots on program
operation and usage.

## Credits
This project was collaboratively developed by the following team:

Toby Dault  
Eyob Tekle  
William L. Thomson Jr.  




