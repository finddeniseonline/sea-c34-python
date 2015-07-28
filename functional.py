#!/usr/bin/env python
# Task 12: Investigate Session 5
import re

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 12                          #"
print "#                                                         #"
print "#        Write 3 questions for lambdas                    #"
print "#         and functional programming                      #"
print "# --------------------------------------------------------#"
print "\n"

print "*" * 10
print u"\nQuestion 1 - Can I add 2 different lists of old macdonald together"
print u"\n            using map and lambda functions?"
raw_input("\nPress Enter to continue...")
print "*" * 10
print "\n"


def ques_1():
    """Question 1 - Can I add 2 different lists of old macdonald together
    using map and lambda functions?

    Args:
        None

    Returns:
        None

    """
    pigs = [2, 4, 6]
    print u"Here is a list of number of pigs " + str(pigs)
    cows = [1, 3, 5]
    print u"Here is a list of number of cows " + str(cows)
    ducks = [10, 20, 30]
    print u"Here is a list of number of ducks " + str(ducks)
    print u"\nLet's add items from each list together."
    print map(lambda x, y, z: x + y + z, pigs, cows, ducks)
    print "\n"
ques_1()

print "*" * 10
print u"\nQuestion 2 - Can I use lambda filter function to extract"
print u"\n             ducks from macdonald's list?"
raw_input("\nPress Enter to continue...")
print "*" * 10


def ques_2():
    """Question 2 - Can I use lambda filter function to extract
    ducks from macdonald's list?

    Args:
        None

    Returns:
        None

    """
    macdonald = ["pigs", "ducks", "cows", "horses", "chickens"]
    print u"\nHere is list of old macdonald farm animals:"
    for i in macdonald:
        print "\t* " + str(i)
    # print str(macdonald)
    print u"\nLet's see if we can extract the ducks from this list..."
    print filter((lambda x: re.match(r"ducks", x)), macdonald)
    print u"\nSuccessful!"
ques_2()


print "*" * 10
print u"\nQuestion 3 - Can we display the largest number in macdonald's farm?"
raw_input("\nPress Enter to continue...")
print "*" * 10


def ques_3():
    """Question 3 - What is the largest number in old macdonald's farm?

    Args:
        None

    Returns:
        None

    """
    print u"\nMacdonald has the following list of number of animals:"
    animals = [100, 200, 301, 22, 101, 500]
    print animals
    print u"\nLet's print the largest number in this list using a lambda"
    macdonald = lambda a, b: a if (a > b) else b
    print reduce(macdonald, [100, 200, 301, 22, 101, 500])
ques_3()
