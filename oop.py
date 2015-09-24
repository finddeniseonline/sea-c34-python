
# !/usr/bin/env python
# Task 16: Session 5

print(u"\n")  # Header
print "# --------------------------------------------------------#"  # Header
print "#             Session 05 Task 16                          #"  # Header
print "#                                                         #"  # Header
print "#        Write 2 questions for OOP                        #"  # Header
print "# --------------------------------------------------------#"  # Header

print(u"\n")
print "*" * 10  # Section divider
print(u"\nQuestion 1 - can I understand polymorphism?")  # Section divider
print "*" * 10  # Section divider

print(u"\n")
d = ["a", "b", "c", "d"]  # list to display polymorphism using integers
print(u"Here is a list:")
print d
print(u"Calling builtin __len__ of the list")
print len(d)  # calls builtin d.__len__()

print(u"\n")
print(u"Here is another list also using strings but, of numbers")
e = ["1", "2", "3", "4"]  # create list to call __len__()
print e
print(u"Calling builtin for __len__ for list of numbers")
print len(e)  # BUT if integers is used in a list polymorphism is displayed

#  uncomment this out to demonstrate!
# x = 5  # based on delegation this demonstrates if we try this with "int"
# # this expression using the "len" builtin will fail
# len(x)
print(u"\n")
print "*" * 10
print(u"\nQuestion 2 - Can I create a class that is derived from parent class")
print "*" * 10
print(u"\n")


class Rooster:  # creating parent class
    """Question 2 - Can I demonstrate creating a class that is derived
    from parent class

    Args:
        None.

    Returns:
        None.
    """
    parentAttr = "Too old to fry and perfect for stew"  # default attribute

    def __init__(self, sound, color):  # Calling parent constructor
        """Constructor object within class

        Args:
            Self refers to target instance class object.
            sound will be passed to each class instance
            color will be passed to each class instance

        Returns:
            None.
        """
        print(u"This is the Rooster (parent class) constructor")
        self.sound = sound  # parent class sound
        self.color = color  # parent class color

    def roosterMethod(self):  # method for rooster
        # self.sound = "Cukooo"
        # self.color = "Red"
        print(u"\tThis is the Rooster (parent) method %s" % self.roosterMethod)

    def setAttr(self, attr):  # set attribute method
        Rooster.parentAttr = attr

    def sounds(self):  # Class method for sounds
        print(u"\tI am a Rooster (parent) and my sound is %s" % self.sound)

    def getAttr(self):  # get method attribute
        # Chicken.parentAttr = attr
        # return self.attr
        # self.attr = "female"
        print(u"Class attribute is: %s" % self.parentAttr)


class Chicken(Rooster):  # child class
    """creating child class of Rooster

    Args:
        Rooster parent object passed as argument

    Returns:
        None.
    """

    def __init__(self):  # constructor for child object
        """contructor for Chicken child class

        Args:
            Self refers to target instance class object.

        Returns:
            None.
        """
        print(u"This is the child constructor")

    def chickenMethod(self):  # child method
        """placeholder for method of Chicken object

        Args:
            Self refers to target instance class object.

        Returns:
            None.
        """
        print(u"\tI am the child method")
        pass


bird = Rooster("loud", "white")  # creating an instance of the Rooster class
print(u"Now creating child class")
print(u"New child class sound is " + bird.sound)  # child class sound method
print(u"New child class color is " + bird.color)  # child class color method
print(u"Child accessing parent sound method is: ")
bird.sounds()  # child object sound method
print(u"Creating another child object of decendant object")
hen = Chicken()  # instance of child class
print(u"Now displaying child method")
hen.chickenMethod()  # child calling its method
print(u"Now calling parent's method")
hen.roosterMethod()  # calling parent method
hen.setAttr("Too young for stew, perfect for frying")  # call to parent method
hen.getAttr()  # obtain class attribute
