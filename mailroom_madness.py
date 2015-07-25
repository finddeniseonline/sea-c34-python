#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import os

#  Session 4 Task 11: Mailroom Madness


def today():  # get date for donation
    now = datetime.now()
    return str(now.month) + "/" + str(now.day) + "/" + str(now.year)

# initial donor list
donors = {
    "donor1": {
        "first": "Michael",
        "last": "Jones",
        "amount": [50.0, 25],
        "date": ["3/1/2015", "3/15/2015"],
    },
    "donor2": {
        "first": "Jeff",
        "last": "Bradshaw",
        "amount": [30.0, 25.0, 10.0],
        "date": ["2/28/2015", "1/17/2015", "2/1/2015"],
    },
    "donor3": {
        "first": "Lloyd",
        "last": "Johnson",
        "amount": [12.0, 80.0],
        "date": ["3/1/2015", "4/2/2015"],
    },
    "donor4": {
        "first": "Alice",
        "last": "Henry",
        "amount": [11.0],
        "date": ["2/15/2015"],
    },
    "donor5": {
        "first": "Tyler",
        "last": "Middleton",
        "amount": [40.0, 50.0, 45.0, 35.0, 30.0],
        "date": ["12/20/2014", "2/20/2015, 1/4/2015", "3/11/2015", "4/1/2015"],
    }
}


# Define actions/functions for mail room donations.

#  Get information to add new donor
def donor_info():
    first = raw_input("Enter donor's [FIRST] name: ")
    last = raw_input("Enter donor's [LAST] name: ")
    amount = float(raw_input('Enter donation [AMOUNT]: '))
    donation_day = today()
    add_new_donor(first, last, amount, donation_day)

    # Here, the program should add a donation with new_donor().
    # Since new_donor requires a dictionary as a parameter,
    # and donor_info does not have a dictionary as a parameter,
    # we need to either give donor_info a dictionary
    # or remove the donor_dictionary parameter from new_donor
    # and let it use the dictionary from the global scope.

#  search if donor is dictionary and if not then add


def add_new_donor(first, last, amount, donation_day):
    # while True:
    add_d = "donor" + str(len(donors) + 1)
    donors[add_d] = {"first": first,
                     "last": last,
                     "amount": [amount],
                     "date": donation_day}
    donor_confirmation(first, last, amount, donation_day)

#  new_donor(donors)

# Send thank you confirmation


def donor_confirmation(first, last, amount, donation_day):
    print '-'*50
    print "You entered the following: "
    print '-'*50
    print 'Donor Name: ' '\t', '\t', first.capitalize(), '\t', \
        last.capitalize(), "\n"
    print 'Donation Amount: ', '\t', "$", amount
    print 'To be posted:' '\t', '\t', donation_day
    print '-'*50
    print '*****Thank you for your donation!*****'
    print '-'*50

#  clear screen for report


def clear():
    os.system("clear")


def report():  # display report for all donors
    print (u"*****HERE IS AN ITEMIZATION OF ALL DONORS*****")
    #  iterate through donors
    for key, donor in donors.items():
        print(key)
        for attribute, value in donor.items():
            print ("{} : {}".format(attribute, value)).replace(",", "|")
        s = sum(donor["amount"])
        print u"-----------------------------------------"
        print u"Total donations for this donor: $%s" % (s)
        print u"-----------------------------------------"


def move_on():  # waits for input from user before clearing screen
    raw_input("\nPress [ENTER] to continue")


def search(donor_dictionary):  # search donor list
    print u"Search for a donor"
    last_name = raw_input(u"Enter a [LAST] name: ")
    for key, donor in donor_dictionary.items():
        if donor['last'] == last_name:

            for attribute, value in donor.items():
                print ("{} : {}".format(attribute, value)).replace(",", "|")
            s = sum(donor["amount"])
            print u"-----------------------------------------"
            print u"Total donations for this donor: $%s" % (s)
            return

        else:
            continue

    s = raw_input(u"Not in list. Would you like to add a donation? [Y] [N]")
    if s == u"Y":
        donor_info()
    elif s == "N":
        return
    elif s == "Y" and not "No":
        print u"Type [Y] or [N] only"
        search(donors)
    else:
        exit()


def main():  # start mailroom madness welcome madness menu
    while True:
        choice = welcome()

        if choice == "1":
            report()
        elif choice == "2":
            search(donors)
        elif choice == "3":
            donor_info()
        elif choice == "4":
            print u"\nThank you"
            break
        else:
            print('\033[93m\nPlease select from the menu provided.\n\033[0m')
        move_on()
        clear()


def welcome():  # display choices for welcome menu to user
    #  provide choices  for menu.
    print u"Welcome to the mail room donation Session 3 Task 3.\nWhat would \
        you like to do?"
    print u"[1] Create Report"
    print u"[2] Search for a donor"
    print u"[3] Add a donation"
    print u"[4] Quit"

    choice = raw_input(u"\nWhat would you like to do?\n> ")
    return choice


if __name__ == "__main__":
    main()
