import json
import datetime
import random
from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

def enter_goals():
    entry_check = "1"

    while entry_check != "0":
        x = input("Enter your goal: (press 0 to end)")
        if x == "0":
            break
        else:
            y = input("Start Date (MM-DD-YY): ")
            month, day, year = map(int, y.split('-'))
            ydatecalc = (datetime.date(year, month, day))
            ydate = str(datetime.date(year, month, day))
            z = input("End Date (MM-DD-YY: ")
            month, day, year = map(int, z.split('-'))
            zdatecalc = (datetime.date(year, month, day))
            zdate = str(datetime.date(year, month, day))
            daystoaccomplish = str(zdatecalc - ydatecalc)
            cat_entry = input("Which category would this be?\n"
                              "Options are:\n"
                              "1: Financial\n"
                              "2: Spiritual\n"
                              "3: Family\n"
                              "4: Work-Career\n"
                              "5: Social\n"
                              "6: Physical-Health\n"
                              "7: Mind-Intellect\n"
                              "8: Personal Development\n")
            if cat_entry == "1":
                cat = "Financial"
            elif cat_entry == "2":
                cat = "Spiritual"
            elif cat_entry == "3":
                cat = "Family"
            elif cat_entry == "4":
                cat = "Work-Career"
            elif cat_entry == "5":
                cat = "Social"
            elif cat_entry == "6":
                cat = "Physical-Health"
            elif cat_entry == "7":
                cat = "Mind-Intellect"
            elif cat_entry == "8":
                cat = "Personal Development"

            goallist.append([x, ydate, zdate, daystoaccomplish, cat])


def print_goals():
    for item in goallist:
        print(item[0], ', '.join(map(str, item[1:])))


def write_goals():
    with open("ie_data.txt", "a+", encoding="utf8") as f:
        json.dump(goallist, f, ensure_ascii=False)


def motivation():
    quotes = {}
    quotes[0] = "Only one can change my life - no one can do it for me. - Carol Burnett"
    quotes[1] = "Life is 10% what happens to you and 90% how you react to it - Charles Swindoll"
    quotes[
        2] = "Optimism is the faith that leads to acheivement. Nothing can be done without hope and confidence - Helen Keller"
    quotes[3] = "Failure will never overtake me if my determination to succeed is strong enough - Og Mandino"
    print(quotes[random.randrange(len(quotes) - 1)])


goallist = []
fieldnames = ['goal', 'start date', 'end date']

motivation()
enter_goals()
print_goals()
write_goals()
