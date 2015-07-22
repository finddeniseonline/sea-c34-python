#!/usr/bin/env python)
# session 02 task 5 sequences

# write 3 questions for each area
# write a function for each question

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 02 Task 5                           #"
print "#                                                         #"
print "#        Write 3 questions for sequences                  #"
print "# --------------------------------------------------------#"

print "*" * 10
print "\nQuestion 1"
print "*" * 10


def oldMacdonald():
    print (u"Old Mac had a farm %s %s %s") % ("EI", "EI", "OHH")

oldMacdonald()

print "*" * 10
print u"Question 2 - can I use index slicing to sing part of old macdonald?"
print "*" * 10


def eieiohh():
    b = u"Old Mac Donald had a farm, EIEIOHH"
    a = b[-5:]
    c = b[:-5] + a
    print c
eieiohh()

print "*" * 10
print u"\nQuestion 3 - what is the length of characters in the phrase old macdonald \
had a farm?"
print "*" * 10


def eieiohh():
    b = u"Old Mac Donald had a farm, EIEIOHH"
    print u"how many characters are in string old macdonald?"
    print u"There are", len(b)
eieiohh()

print "*" * 10
print u"\nQuestion 4 - (additional question)\n"
print u"what if a string is split on a new line\n"
print u"can I use slicing to print strings on new line from hip hip hooray"
print "*" * 10


def hipHooray():
    s = tuple(u"hiphiphooray")  # can I split string using slicing?
    # s = "hiphiphooray"
    print s[:3]
    print s[:3]
    print s[-6:]
hipHooray()
