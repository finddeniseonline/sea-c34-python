#!/usr/bin/env python)
# session 03 task 8 exceptions

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
import sys


print "\n"
print "# --------------------------------------------------------#"
print "#             Session 03 Task 8                           #"
print "#                                                         #"
print "#        Write 3 questions for exceptions                 #"
print "# --------------------------------------------------------#"
print("\n")
print "*" * 25
print("\nQuestion 1\n")
print "*" * 25

# can I print file doesn't exist? or no such file?
filename = raw_input(u"\nEnter a file name to open: ")


def exceptions_ques1(filename):
    """Question 1 - Can I not break out of program
    so that user can enter a different name to check?

    Args:
        Filename user enters

    Returns:
        No return statement
    """
    try:
        f = open(filename)
        print(u"\nWell the files exist...but we don't need to open it.")
        f.close()
    except:
        print(u"There is no such file named", filename)

exceptions_ques1(filename)

print("\n")
print "*" * 25
print("\nQuestion 2\n")
print "*" * 25


def exceptions_ques2():
    """Question 2 - Can I create exception for numbers being string
    not integer? "2" or 2.

    Args:
        No arguments are passed

    Returns:
        No return statement
    """
    print("\nLet's create an exception when input is not a number.")
    while True:
        try:
            x = int(raw_input("\nPlease enter a number: "))
            break
        except ValueError:
            print("\nOops! That was no valid number. Try again...")

exceptions_ques2()
