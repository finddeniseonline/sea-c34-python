
# !/usr/bin/env python
# Task 16: Session 5
import sys


print "\n"  # Header
print "# --------------------------------------------------------#"  # Header
print "#             Session 05 Task 16                          #"  # Header
print "#                                                         #"  # Header
print "#        Write 1 question(s) for classes                  #"  # Header
print "# --------------------------------------------------------#"  # Header
print "\n"


print(u"\n")
print "*" * 10  # Section divider
print(u"\nQuestion 1 - Can I create old macdonald animal")  # Section divider
print(u"parent class to display inheritance?")
print "*" * 10  # Section divider


class Animal:  # old macdonald animal parent class
    """Can I create an old macdonald animal parent class. This will
       create the parent class for the Animal object to
       display inheritance

    Args:
       None.

    Returns:
        None.
    """
    def __init__(self, animal, sound):
        """Constructor object within class

        Args:
            *Self refers to target instance class object.
            *Type of animal will be passed to all child classes
            *Sound for animal will be passed to all child classes

        Returns:
            None.
        """
        self.animal = animal
        self.sound = sound
        print(u"\nParent class is Animal")


class Chicken(Animal):  # Child object created
    """Constructor object within child class to inherit
       attributes of parent

    Args:
        Parent object is passed as argument

    Returns:
        None.
    """
    def __init__(self, animal, sound):
        """Constructor object within class

        Args:
            Self refers to target instance class object.
            Type of animal will be passed to into this child object
            Sound for animal will be passed to this child object

        Returns:
            None.
        """
        Animal.__init__(self, animal, sound)
        print(u"\nChild class is a Chicken")


def Main():
    """Main function to be executed to display object instances
       of both parent and child class

    Args:
        None.

    Returns:
        None.
    """
    # print(u"Creating a child object")
    horse = Animal("Toggles", "neigh neigh")  # create child instance
    # print horse
    # print(u"Now creating another child object")
    rooster = Chicken("Rooster", "peck peck")  # create child instance
    # print rooster
    print(u"Is horse decendant of chicken: " + str(isinstance(horse, Chicken)))
    print(u"Is rooster an animal: " + str(isinstance(rooster, Animal)))
    print(u"Is horse an animal: " + str(isinstance(horse, Animal)))
    print(u"Is rooster a chicken: " + str(isinstance(rooster, Chicken)))

    print(u"child class method is %s" % rooster.sound)  # child class method
    print(u"\n")

if __name__ == "__main__":
    Main()
