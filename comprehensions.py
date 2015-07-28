#!/usr/bin/env python
# Task 12: Investigate Session 5

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 12                          #"
print "#                                                         #"
print "#        Write 3 questions for comprehensions             #"
print "# --------------------------------------------------------#"
print "\n"

print "*" * 10
print u"\nQuestion 1 - Can I create a comprehension to see if animals"
print u"in one variable exists is in another variable?"
print "*" * 10


def ques_1():  # Question 1
    """Question 1 - Can I create a comprehension to see if animals
     in one variable is in another variable?

    Args:
        None

    Returns:
        None
        # Returns comprehension result if item exists is in list

    """
    print u"\nHere is a list of old macdonald farm animals: "
    animals = ["pigs", "cows", "ducks", "chickens", "horses"]
    for animal in animals:
        print "\t* " + str(animal)
    check = set(["donkey", "pigs"])
    print u"\nHere is a set of two animals - ", check
    print u"\nLet's display animals from this set that exists in"
    print u"old macdonald's farm:"
    test = {i for i in animals if i in check}
    # return test
    print test
    print u"\nSuccessful!"
ques_1()

raw_input("\nPress Enter to continue...")

# def ques_1_test():
#     """Question"""
#     song = "Old macdonald had a farm"
#     verse = set("eieio")
#     sing = {i for i in verse}
#     print sing
# ques_1_test()

print "\n"
print "*" * 10
print u"\nQuestion 2 - Can I create a list comprehension to show?"
print u"a tuple of user choice"
print "*" * 10


def ques_2():
    """Question 2 - Can I create a list comprehension to show a
       tuple of user choice

    Args:
        None

    Returns:
        None

    """
    animals = ["pig", "cow", "chicken", "duck", "horse"]
    sounds = ["oink oink", "moo moo", "cluck cluck", "quack quack",
              "neigh neigh"]
    print(u"\nHere is a list of animals to choose from: ")
    print animals

    choice = (raw_input(u"\n  Choose an animal: > "))

    macdonald = [(animal, sound) for (animal, sound) in zip(animals, sounds)
                 if choice in (animal, sound)]
    print(u"\nHere is the sound for the animal you chose:")
    print macdonald
ques_2()

print "\n"
print "*" * 10
print u"\nQuestion 3 - Can I create a nested for loop in a comprehension?"
print "*" * 10

raw_input("\nPress Enter to continue...")


def ques_3():  # Can I create a nested for loop in a comprehension
    """Question 3 - Can I create a nested for loop in a comprehension

    Args:
        None

    Returns:
        None

    """
    # macdonald = {}
    animals = ("pigs", "cows", "chickens", "ducks", "horses")
    amounts = ("5", "11", "7", "9", "3")
    macdonald = [animal + ": " + amount for animal,
                 amount in zip(animals, amounts)]
    print(u"\nOld macdonald had a farm. He has: "), macdonald
ques_3()
