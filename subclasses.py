
# !/usr/bin/env python
# Task 16:  Session 5

print "\n"  # Header
print "# --------------------------------------------------------#"  # Header
print "#             Session 05 Task 16                          #"  # Header
print "#                                                         #"  # Header
print "#     Write 4 questions for subclasses                    #"  # Header
print "# --------------------------------------------------------#"  # Header

raw_input("\nPress [ENTER] to continue")

print "\n"  # Section divider
print "*" * 10  # Section divider
print(u"\nQuestion 1 - Can I override an attributes of parent class?")
print "\n"  # Section divider
print "*" * 10  # Section divider
print "\n"  # Section divider


class Chicken:  # create a parent class
    """Question 1 - Can I demonstrate creating a class that is derived
    from parent class then override attributes of parent

    Args:
        None.

    Returns:
        None.
    """
    sound = "cluck cluck"  # parent sound attribute
    color = "brown"  # parent color attribute
    behavior = "peck"  # parent class behavior attribute

    def __init__(self, sound, color, behavior):  # constructor for parent class
        """Constructor object for parent class

        Args:
            Self refers to target instance class object
            sound will be passed to each class instance
            color will be passed to each class instgance
            behavior will be passed to each class instance

        Returns:
            None.
        """
        self.sound = sound
        self.color = color
        self.behavior = behavior


class Horse(Chicken):  # create child class of Chicken
    #  def __init__(self, sound, color, behavior):
        sound = "neigh neigh"  # override parent sound attribute
        color = "black"  # override parent color attribute
        behavior = "gallop"  # override parent behavior attribute

print(u"The parent object sound is - " + Chicken.sound)  # display parent sound
print(u"The parent object color is - " + Chicken.color)  # display parent color
print(u"The parent object behavior is - " + Chicken.behavior)  # parent attrib
print(u"This is the child class overriding the attributes of")
print(u"  parent class.")
print(u"The child attribute for sound now overrides parent - " + Horse.sound)
print(u"The child attribute for color now overrides parent - " + Horse.color)
print(u"Now overriding parent behavior - " + Horse.behavior)

print "\n"  # Section divider
print "*" * 10  # Section divider
print(u"\nQuestion 2 - Let's see if we can add an attribute to super class?")
print "\n"  # Section divider
print "*" * 10  # Section divider
print "\n"  # Section divider

raw_input("\nPress [ENTER] to continue")


class Duck(Chicken):  # subclass for new class based off super
    """Question 2 - Let's see if we can add an attribute to super class?"

    Args:
        Parent object.

    Returns:
        None.
    """
    def __init__(self, reproduce):  # constructor for subclass
        """Question 2 - Let's see if we can add attribute to super class?"

        Args:
            Self refers to target instance class object.
            reproduce will add additional attribute to instance of class

        Returns:
            None.
        """
        self.reproduce = reproduce * 4  # add new attribute to sub class
        # Chicken.__init__(self, sound, color, behavior)

duck = Duck(2)  # instance of subclass

print(u"\nThe subclass will inherit the sound of the superclass:")
print(duck.sound)  # subclass inherits sound of super
print(u"\nThe subclass will now add an attribute called behavior:")
print(duck.reproduce)  # subclass adds attribute "behavior" to superclass

raw_input("\nPress [ENTER] to continue")

print "\n"    # Section divider
print "*" * 10   # Section divider
print(u"\nQuestion 3 - Can I create subclass then delete it?")
print "\n"    # Section divider
print "*" * 10    # Section divider
print "\n"    # Section divider

raw_input("Press [ENTER] to continue")

horse = Horse("neigh neigh", "white", "trots")  # new instance of class
print (u"Subclass attributes are: " + horse.color + " and " + horse.behavior)
print "\n"    # Section divider
print(u"** Now deleting horse subclass...")
del horse  # deletes sublcass
print(u"\n")    # Section divider

print "*" * 10   # Section divider
print(u"\nQuestion 4 - Can I demonstrate decendants of subclasses?")
print "\n"   # Section divider
print "*" * 10   # Section divider
print "\n"   # Section divider

raw_input("\nPress [ENTER] to continue")


class Grandpa(object):  # superclass object for ancestor
    """Question 4 - Can I demonstrate subclasses of decendants?"

    Args:
        Parent object.

    Returns:
        None.
    """
    def getName(self):  # method to obtain class name
        """Constructor for parent object"

        Args:
            Self refers to target instance class object.

        Returns:
            None.
        """
        raise NotImplementedError  # raise error if parent doesn't provide

# raw_input("\nPress [ENTER] to continue")


class Dad(Grandpa):  # decendant class of parent object
    """New class derived from Ancestor Object"

    Args:
        Parent object

    Returns:
        None.
    """
    def getName(self):  # method for obtaining name of object instance
        a = "\t* Daddy Barnes"
        return a  # returns name of specific decendant

# raw_input("\nPress [ENTER] to continue")


class Myself(Dad):  # decendant class of direct parent object
    """New class derived from parent Object"

    Args:
        Parent object

    Returns:
        None.
    """
    def getName(self):  # method for obtaining name of object instance
        return "\t* Myself"  # returns name of specific decendant


if __name__ == "__main__":
    dd = Dad()
    print(u"\nHere is a name of a subclass of a decendant from super class:")
    print dd.getName()
    me = Myself()
    print(u"\nHere is another name of a decendant of super class object:")
    print me.getName()
