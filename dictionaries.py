#!/usr/bin/env python)
# session 03 task 8 sequences
import sys

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
print "#        Write 4 questions for dictionaries               #"
print "# --------------------------------------------------------#"
print "\n"
print "*" * 25
print("\nQuestion 1\n")
print "*" * 25

animal = {
    "\tducks": 2,
    "\tchickens": 3,
    "\tpigs": 4,
    "\tcows": 5,
    "\thorses": 1,
    "\tgoats": 7,
    }
#  Dictionaries and Sets (4 questions)


def dict_ques1(animal):  # Question 1
    """Question 1 - Can I lookup animal in old macdonald
    and get error that it doesn't exist?

    Args:
        animal (parameter passed in for animal run function).

    Returns:
        Condition if animal exists then confirmation is displayed,
        otherwise message stating animal doesn't exist.

    """

    old_macdonald = {  # dictionary for animals
        "animal1": "duck",
        "animal2": "chicken",
        "animal3": "sheep",
        "animal4": "horse",
        }
    animal = old_macdonald
    print("\nLet's check to see if animal is in Old Macdonald's farm.")
    # x = old_macdonald
    if animal in old_macdonald.values():  # condition to check if animal exist
        print("\nOld Macdonald has that animal")

    else:
        print("\nThat animal is not in Old Macdonald's farm")

dict_ques1(animal)

# if __name__ == "__main__":

#     """Tests function for animals that exist in farm"""
#     assert(old_macdonald["sheep"])
#     assert(old_macdonald["pig"])


# old_macdonald = {(3, 2, 3)}

# can I print how many animals old macdonald has

print "*" * 25
print "\nQuestion 2\n"
print "*" * 25


def dict_ques2():  # Question 2
    """Question 2 - can I create a dictionary list
    of tuples that shows how many animals are for each animal?

    Args:
        No arguments or parameters to pass

    Returns:
        Returns a list of tuples that display animals and how many

    """
    old_macdonald = {  # dictionary of animals
        "duck": 2,
        "chicken": 3,
        "pig": 4
        }
    print("\nHere is are tuples displayed of the animals")
    print("in in the dictionary: ")
    for x in old_macdonald.items():  # for loop to iterate through animals
        print(x)  # prints each item in dictionary
dict_ques2()

old_macdonald = {
    "ducks": 2,
    "chickens": 3,
    "pigs": 4,
    "cows": 5,
    "horses": 1,
    "goats": 7,
    }

print "\n"
print "*" * 25
print "\nQuestion 3\n"
print "*" * 25


def dict_ques3(animals):  # Question 3

    """Question 3 - can I access dictionary items outside of function?

    Args:
        Dictionary items are passed into function from outside scope

    Returns:
        Execution of function is ended; no return

    """
    print("\nHere is a list of animals in dictionary accessed")
    print("outside this function: ")
    for i in old_macdonald.items():
        print(i)
    return

dict_ques3(old_macdonald)


old_macdonald = {
    "\tducks": 2,
    "\tchickens": 3,
    "\tpigs": 4,
    "\tcows": 5,
    "\thorses": 1,
    "\tgoats": 7,
    }

# def dict_ques3_1():
#     print "%s has the following animals:" % ("Old Macdonald")
#     for k, v in old_macdonald.items():
#         print ": ".join((k, str(v)))
# dict_ques3_1()


# def animals():  # Question
#     print "\n %s has the following animals:" % (s)
#     for k, v in old_macdonald.items():
#         print ": ".join((k, str(v)))
# animals()

print "*" * 25
print "\nQuestion 4\n"
print "*" * 25


def dict_ques4(animals):  # Question 4
    """Question 4 - can I remove items from a dictionary
    and display to user what was removed

    Args:
        Dictionary list of animals are passed into function

    Returns:
        Callback to function to end execution
    """
    print("\nHere are Old Macdonald's animals: ")
    print animals
    print("\nNow let's remove some of %s animals:" % ("Old Macdonald's"))
    item_removed = animals.popitem()  # remove first item from dictionary
    item_removed_2 = animals.popitem()  # remove second item from dictionary
    print("\t{}: {}".format(*item_removed))  # display first item removed
    print("\t{}: {}".format(*item_removed_2))  # display second item removed
    print("\nNow let's display the updated list of Old Macdonald's farm: ")
    print animals
    return  # end of function

animals = {  # list of animals
    "ducks": 2,
    "chickens": 3,
    "pigs": 4,
    "cows": 5,
    "horses": 1,
    "goats": 7,
    }

dict_ques4(animals)
