#!/usr/bin/env python)
# session 03 task 8 files
import sys
import glob
import os
from sys import argv

"""
Session 03 task 8.

The specifications for the assignments states to write a function
for each question for the following sections:

Sections
    Dictionaries and Sets (4 questions)
    Exceptions (2 questions)
    File Reading and Writing (2 questions)
    Paths (1 question)
    Write some Python code to help you answer them, one function per question.


Put the functions in four separate modules (files) called dictionaries.py,
exceptions.py, files.py, paths.py in the session04 subdirectory of your
student directory, just as you did for list_lab.py up above.

"""

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 03 Task 8                           #"
print "#                                                         #"
print "#        Write 2 questions for files                      #"
print "# --------------------------------------------------------#"
print "\n"
print("*" * 25)
print("\nQuestion 1")
print("\nNOTE: To see this in action place this file in a directory")
print("that has many files in it.")
print "\n"
print("*" * 25)


# File Reading and Writing (2 questions)


FILE_EXTS = {  # Dictionary of file extensions to choose from
    "1": "*.txt",
    "2": "*.rtf",
    "3": "*.png",
    "4": "*.pdf",
    "5": "*.doc"
}

PROMPT = (  # list of file ext choices to present to user
    "\nWhat kind of files do you want to search for?"
    "\n1) .txt"
    "\n2) .rtf"
    "\n3) .png"
    "\n4) .pdf"
    "\n5) .doc"
    "\nChoose a number: "
    "\n\t> "
)


def files_ques1():
    """Question 1 - Can I present files to user based on their choice

    Args:
        None.

    Returns:
        Results of files found

    """
    try:
        choice = raw_input(PROMPT)
        chosen_ext = FILE_EXTS[choice]
        results = glob.glob(chosen_ext)

        print("\x1b[5m *** Here is results of the list of files: ***\x1b[0m\n")
        for i, each_file in enumerate(results, start=1):
            print("\t{}] {}".format(str(i), each_file))

    except KeyError:
        print(u"\nPlease select a number from the list!")

found_files = files_ques1()


print("\n")
print("*" * 25)
print("\nQuestion 2\n")
print("*" * 25)


def file_ques2():

    """Question 1 - Can I create a file based on what
    user enters a name for then write to that file
    using data a user provides?

    Args:
        No arguments necessary for this exercise

    Returns:
        Execution of function is ended; no return

    """

    filename = raw_input("\nEnter a name of a text file to create: ") + ".txt"
    print("\n\tThis will create a file called " + filename)

    # print "Opening the file..."
    target = open(filename, "w")

    # print "Truncating the file. Goodbye!"
    # target.truncate()

    print(u"\nNow I'm going to ask you for three lines of text")
    print(u"to save to the file you just named.")

    lines = [raw_input("line {i}: ".format(i=i)) for i in range(1, 4)]

    print "\nI'm going to write these these lines to the file:"

    for line in lines:
        target.write(line + '\n')

    print "\nAnd finally, we close the file."
    print "\n\033[94m View " + filename + " to see the contents.\033[0m"
    print "\n"
    target.close()
    return
file_ques2()
