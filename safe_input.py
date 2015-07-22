#!/usr/bin/env python)
# -*- coding: utf-8 -*-
# session 04 task 10

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 04 Task 10                          #"
print "#                                                         #"
print "#            Exceptions/safe_input                        #"
print "# --------------------------------------------------------#"

print "\n"
print u"Step 1  - The raw_input() function can generate two exceptions: "
print u"\tEOFError or end-of-file (EOF)"
print u"\tKeyboardInterrupt or canceled input. - Create a wrapper function"
print u"* Perhaps safe_input() that returns 'None' rather  than raising these"
print u"exceptions."
print "\n"
#  wrapper function to catch EOF, KeyboardInterrupt, or canceled errors

print "test - click CTRL + C"
print "\n"


def safe_input(*prompt):
    try:
        if len(prompt) > 0:
            user_in = raw_input(prompt[0])
        else:
            user_in = raw_input()

    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return user_in
safe_input()

#  another example
try:
    date = input("Example: April 11 | What is the date? ")
except:
    print "not the date, something went wrong."
