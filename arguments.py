#!/usr/bin/env python
# Task 12: Investigate Session 5

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 12                          #"
print "#                                                         #"
print "#        Write 3 questions for arguments                  #"
print "# --------------------------------------------------------#"
print "\n"

print "*" * 10
print u"\nQuestion 1 -"
print u"Can I have all of old macdonald animals set as variables"
print u"by default?"
print "*" * 10


def ques_1(r="cows", s="goats", t="ducks", u="chickens", v="horses", w="pigs"):
    """Question 1 - can I have all of old macdonald animals set as
       variables by default?

    Args:
        None

    Returns:
    """

    print (r, s, t, u, v, w)
ques_1()

print "\n"
print "*" * 10
print u"\nQuestion 2 - Can old macdonald have positional arguments for the"
print u"animals?"
print "*" * 10
print "\n"


def old_macdonald(x, y="chickens", z="cows"):
    """Question 2 - Can old macdonald have positional arguments for the animals?

    Args:
        None

    Returns:
    """
    print(u"x is: %s, y is: %s, and z is: %s") % (x, y, z)

old_macdonald(x="pigs")

print "\n"
print "*" * 10
print u"\nQuestion 3 - Can I display optional args for old macdonald's farm?"
print "*" * 10
print "\n"


def ques_3(*args, **kwargs):
    """Question 3 - Can I display optional arguments for old macdonald's farm?

    Args:
        None

    Returns:
    """
    print(u"This is how many animals are in old macdonald's\
        farm: %s" % unicode(kwargs))

ques_3(cows=3, pigs=5, chickens=7, horses=2)
