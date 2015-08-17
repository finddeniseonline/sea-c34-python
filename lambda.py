#!/usr/bin/env python
# Session 05 Task 15 Lambda and keyword argument magic


print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 15                          #"
print "#                                                         #"
print "#      lambda and keyword argument magic                  #"
print "# --------------------------------------------------------#"
print"\n"

raw_input("\nPress ENTER to continue...")


def func(incr):
    """Function that returns a list of n functions
    that returns the input value, incremented by a number

    Args:
        Argument will take a number to incremente

    Returns:
        Returns list of functions incremented by argument
    """

    list = []
    for i in range(incr):
        a = lambda j, i = i: i
        list.append(a)
        print "\nThe count is: ", i
    return list

func(8)


print u"\nHere is extra credit list comprehension"
# extra credit list comprehension
raw_input("\nPress ENTER to continue...")


def func(incr):
    """Function that returns a list of n functions
    that returns the input value, incremented by a number

    Args:
        Argument will take a number to incremente

    Returns:
        Returns list of functions incremented by argument
    """

    print '\nThe count is:', incr

a = lambda j: [func(i) for i in range(j)]
a(5)


if __name__ == "__main__":
    print func(8)
    print func(3)
