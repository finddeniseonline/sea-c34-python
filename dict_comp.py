#!/usr/bin/env python
# Session 05 Task 14 Dictionary and Set Comprehensions

print "\n"
print "# --------------------------------------------------------#"
print "#             Session 05 Task 14                          #"
print "#                                                         #"
print "#      Dictionary and Set Comprehenstions                 #"
print "# --------------------------------------------------------#"
print"\n"

# Create dictionary with my own items
food_prefs = {"name": u"Denise",
              u"city": u"Seattle",
              u"cake": u"Coconut",
              u"fruit": u"grapefruit",
              u"salad": u"Asian",
              u"pasta": u"macaroni"}


# Display dictionary items
print "\nHere is a dictionary items of food preferences: \n ", food_prefs
raw_input("\nPress Enter to continue...\n")
print "*" * 25
print "\n"
# Step 1 - items from dictionary passed into a string format
print "Here is [Step 1] items from a dictionary passed into string format\n"
print u"{name} lives in {city}, and absolute favorites are {cake} cake, \
fruit is {fruit}. Other items to like are {pasta} {salad} which are \
also great.".format(**food_prefs)

raw_input("\nPress Enter to continue...\n")
print "*" * 25
print "\nHere is [Step 2] to display dict of numbers 0-15 and their hex values"
# Step 2 - display dict of 0 - 15 numbers and hex value
numbers = range(0, 16)
hex_numbers = {hex(x) for x in numbers}

hw_hex = dict(zip(numbers, hex_numbers))
print "This is the list of numbers and their hex values:\n"
print hw_hex
raw_input("\nPress Enter to continue...\n")
print "*" * 25
print "\n"
# Step 3 - dict comprehension using one liner
hw_hex = {x: hex(x) for x in range(0, 16)}
print "[Step 3] Here is the list of numbers and hex value using one liner\
 dictionary comprehension."
print hw_hex
raw_input("\nPress Enter to continue...\n")
# OR
# hex_dict = {i: hex(i) for i in range(16)}
# print hex_dict

print "*" * 25
print "\n"
# Step 4 - dictionary displaying values of "a's" (not 'A's) in each value
print "Here is [Step 4] displaying # of a's for each value."
food2_prefs = food_prefs.copy()
for k, v in food2_prefs.items():
    food2_prefs[k] = v.count("a")
print food2_prefs
raw_input("\nPress Enter to continue...\n")
print "*" * 25
print "\n"
# Step 5 sets that contains numbers 1 - 20 divisible by 2, 3, 4
print "Here are sets 2, 3, and 4.\n"
s2 = range(21)
l2 = set(s2)
print "This is set 2: ", l2
print "*" * 10

s3 = range(21)
l3 = set(s3)
print "\nThis is set 3: ", l3
print "*" * 10

s4 = range(21)
l4 = set(s4)
print "\nThis is set 4: ", l4
print "\n"
raw_input("Press Enter to continue...")
print "*" * 25
print "\n"
print "[Step 5-a] Here are sets that contain numbers divisible by 2, 3, and 4 \
using dictionary comprehensions.\n"
print "This set is divisible by 2"
print "\n"
l2 = {i for i in range(21) if i % 2 == 0}
print l2
print "\n"
raw_input("Press Enter to continue...\n")
print "\n"
print "*" * 10
print "\nThis set is divisible by 3"
l3 = {i for i in range(21) if i % 3 == 0}
print l3
print "\n"
raw_input("Press Enter to continue...\n")
print "\n"
print "*" * 10
print "\nThis set is divisible by 4"
l4 = {i for i in range(21) if i % 4 == 0}
print l4
print "\n"
raw_input("Press Enter to continue...\n")
print "\n"
print "*" * 10
# here is a sequence that encompasses all three sets
print "\n[Step 5-b] (...and possibly extra credit - here is a"
print "sequence that encompasses all three sets)\n"
l2, l3, l4 = [{i for i in range(21) if not i % j} for j in range(2, 5)]
raw_input("Press Enter to continue...\n")
print "\n"
print "*" * 10
# Display if s3 is a subset of s2 (False)
print u"\nIs l3 a subset of l2 is (False)? "
print set(l3).issubset(l2)
raw_input("\nPress Enter to continue...\n")
print "\n"
print "*" * 10
# Display if s4 is a subset of s2 (True)
print u"\nIs l4 a subset of l2 (True)? \n"
print set(l4).issubset(l2)

# if __name__ == "__main__":
#    main()
