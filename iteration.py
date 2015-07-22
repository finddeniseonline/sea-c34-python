#!/usr/bin/env python)
# session 02 task 5 iterations

# write 3 questions for each area
# write a function for each question

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 02 Task 5                           #"
print "#                                                         #"
print "#        Write 3 questions for iterations                 #"
print "# --------------------------------------------------------#"


print "\nQuestion 1 - can i have old macdonald song displayed in reverse"
print "*" * 10
# can i have "old macdonald song displayed in reverse"


def verse():
    song = [u"old", u"macdonald", u"had", u"a", u"farm", u"eieio"]  # list
    song.reverse()  # function for reverse of items in list
    print song  # display verse in reverse
verse()

print "*" * 10
print "\nQuestion 2 - can I set a flag for an infinite loop"
print "*" * 10


def setFlag():  # function for flag
    keep_running = True  # function will keep running till condition is false
    while keep_running:
        s = "eieio"  # variable for old macdonald verse
        run = raw_input('Display infinite loop? (y/n) ')  # choice for loop
        print(s)
        if run == "n":  # set condition to false
            keep_running = False
setFlag()

print "*" * 10
print "\nQuestion 3 - can I use a for loop to iterate over a tuple?\n"
print "*" * 10


def song():
    animals = [("cow", "moo"), ("horse", "neigh"), ("chicken", "cluck"),
               ("duck", "quack")]  # tuples for animals and sounds
    for k, v in animals:  # for loop to iterate through list of tuples
        print "Old macdonald had a farm, eieiohh."
        print "And on that farm he had a %s, eieiohh" % (k)
        print "With a %s %s here." % (v, v)
        print "And a %s %s there, %s, here," % (v, v, v)
        print "%s there, %s here, and a %s %s everywhere." % (v, v, v, v)
song()
