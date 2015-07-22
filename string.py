#!/usr/bin/env python)
# session 02 task 5 string formatting

# write 3 questions for each area
# write a function for each question

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 02 Task 5                           #"
print "#                                                         #"
print "#        Write 3 questions for strings                    #"
print "# --------------------------------------------------------#"


print "*" * 10
print u"\nQuestion 1 - can old macdonald print every other letter uppercase?"
print "*" * 10


def selective_uppercase(x):  # make every other letter uppercase
    string = ""
    i = True
    for word in x:
        if i:
            string += word.upper()
        else:
            string += word.lower()
        if word != " ":
            i = not i
    return string
print selective_uppercase(u"old macdonald had a farm eieiohh")

print u"*" * 10
print u"\nQuestion 2 - can I seperate every letter in song with a character?"
print "*" * 10


def sep():
    song = u"old macdonald had a farm eieiohh"
    new_song = song.replace(" ", "*")
    print new_song
sep()


print "*" * 10
print u"\nQuestion 3 - can I use named format for main verse in old macdonald?"
print "*" * 10


def named_strings():
    print u"Old {} had a farm, {}".format(u"old macdonald", u"eieiohh")
named_strings()
