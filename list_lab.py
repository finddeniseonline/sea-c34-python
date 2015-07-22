#!/usr/bin/env python
# Session 03 Task 6


def series_one(fruit_list):
    # Create a list
    print "\nFirst series steps 1 - 8"
    # fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    # display the list
    print fruit_list
    # ask user for additional fruit
    # for fruit in fruit_list:
    #    new_fruit = fruit_list[:]
    add = raw_input("Choose an additional fruit to add: ")
    fruit_list.append(add)
    print "This is the updated fruit list" + str(fruit_list)

    # Display all fruits with "P" using for a loop
    print "*" * 15
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    new_list = []

    # Add another fruit to the beginning of the list using
    # and display the list.
    a = fruit_list[:]  # making copy of initial fruit list
    b = ["Strawberries", "Grapes", "Melons"]  # adding more fruit

    c = b + a
    print c

    for i in fruit_list:
        if i[0] == "P":
            new_list.append(i)
    new_list

    print "*" * 15

    # because the other steps say to use the list from series 1:
    return fruit_list


def series_two(fruit_list):
    print "\nThis is the series 2 steps 1 - 2"
    copy_fruit = fruit_list[:]

    # Ask the user for a number and display the number back
    # to the user and the fruit corresponding to that number
    # (on a 1-is-first basis).

    print "*" * 15

    # Add another fruit to the beginning of the list using insert()
    # and display the list.

    # fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    # # display the list
    # print fruit_list
    # # ask user for additional fruit
    # #for fruit in fruit_list:
    #     add = raw_input("Choose an additional fruit to add: ")
    #     fruit_list.insert(0, add)
    # print (fruit_list)
    # print "*" * 15
    # # Display the list.
    # # Remove the last fruit from the list.
    # # Display the list.
    # print "*" * 15

    # l = fruit_list[:]

    print copy_fruit
    del copy_fruit[-1]
    print copy_fruit

    print "*" * 15
    # create def to encapsulate
    # add .lower()


def series_three(fruit_list):
    print "\nThis is the series 3 steps 1 - 5 with bonus item"
    # Ask the user for a fruit to delete and find it and delete it.
    fruits = fruit_list[:]
    print fruits
    for fruit in fruits:
        d = raw_input("Delete a fruit: Apples, Pears, Orange, Peaches ")
        fruits.remove(d)
    print (fruits)
    print "*" * 15

    # (Bonus: Multiply the list times two. Keep asking until a match is
    # found. Once found, delete all occurrences.)????


def series_four(fruit_list):
    print "\nThis is the series 4 steps 1 - 2"
    fruits = fruit_list[:]
    doubled_fruits = fruits * 2

    def restart():

        c_fruits = doubled_fruits
        c_fruits.reverse()
        d = raw_input("Choose a fruit to delete: {}".format(fruits))

        def delete_items(a, d):
            while d in a:
                a.remove(d)
                break
            else:
                if d not in c_fruits:
                    print "Invalid input."
                    restart()
                else:
                    print "Goodbye"
        delete_items(c_fruits, d)
        print c_fruits
        restart()
    print "*" * 15

    #    Ask the user for input displaying a line like "Do you like apples?"
    #    for each fruit in the list (making the fruit all lowercase).
    #    For each "no", delete that fruit from the list.
    #    For any answer that is not "yes" or "no", prompt the user to answer
    #    with one of those two values (a while loop is good here):
    #    Display the list.
    #    hmmm add while loop for out of bound answer
    a = ["Apples", "Pears", "Oranges", "Peaches"]
    b = []
    print "Here a list of fruit... "
    print ' \n'.join(a)

    restart_loop = True
    while restart_loop:
        restart_loop = False
        for i in a:
            d = raw_input("Do you like " + i + " y/n? ")
            if d != "y" and d != "n":
                print "Please answer y/n only"
                restart_loop = True
                break
            elif d == "y":
                b.append(i)
            else:
                print "too bad for you"

    print "You like the following fruit..."
    print " \n".join(b)
    print "*" * 15
    # Make a copy of the list and reverse the letters
    # in each fruit in the copy.
    # global fruit_list
    # s = fruit_list[:]
    rev = fruits[::-1]
    # fruits[0]
    for i in range(len(fruits) - 1, -1, -1):
        rev += fruits[i]
        rev
    print('\n\n\n' + str(rev))
    fruit_list = rev.split(' ')

    print "*" * 15

    # Delete the last item of the original list. Display the original
    # list and the copy.

    fruits = fruit_list[:]
    t = fruits[:]
    del t[-1:]
    print t
    print fruits

s = ["apples", "pears", "oranges", "peaches"]
print s[::-1]
rev = s[::-1]
# s[0]
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
    rev
yikes = rev.split(' ')


def wait_for_enter():
    raw_input('\nPress [ENTER] to continue . . .\n> ')


if __name__ == "__main__":
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

    # fruit_list = series_one(fruit_list)
    # wait_for_enter()
    # series_two(fruit_list)
    # wait_for_enter()
    # series_three(fruit_list)
    # wait_for_enter()
    series_four(fruit_list)
