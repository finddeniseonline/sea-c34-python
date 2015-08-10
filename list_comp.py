#!/usr/bin/env python)
# -*- coding: utf-8 -*-
# session 05 task 13

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 13                          #"
print "#                                                         #"
print "#  1 line list comprehension to count even nums           #"
print "# --------------------------------------------------------#"


def count_evens(nums):  # function with argument for numbers passed in
    """Question 1 - Can I create 1 line list comprehension to count even nums?

    Args:
        None

    Returns:
        None

    """
    print len([num for num in nums if num % 2 == 0])
    return len([num for num in nums if num % 2 == 0])  # list comprehension

print "\nLet's test this..."

raw_input("\nPress Enter to continue...\n")
print "*" * 25

if __name__ == "__main__":
    # count evens test
    assert(count_evens([2, 1, 2, 3, 4]) == 3)
    assert(count_evens([2, 2, 0]) == 3)
    assert(count_evens([1, 3, 5]) == 0)

print "\ntests pass...\n"
