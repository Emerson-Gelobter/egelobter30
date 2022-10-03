'''
Prattay Dey, Emerson Gelobter
SoftDev
06_py-csv
2022-09-29
time spent: _______
DISCO:
- When reading csv files, we can use DictReader() instead of reader(). This function is like a regular reader but also maps each row to a key-value pair.
  (https://docs.python.org/3/library/csv.html)
-
QCC:
HOW THIS SCRIPT WORKS:
'''

import csv
import random

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)
    list_dict = []

    for row in reader:
        # print(row)
        # print(row["Job Class"])
        # compiles all the different key-value pairs into one dictionary
        list_dict.append(row)
        #print(row["Job Class"], row["Percentage"])

    # removes Total row
    list_dict.pop()


def weighted_pick(dict):
    randnum = random.random() * 100
    current_sum = 0
    row = 0
    for key in dict:
        if (row != 0):
            current_sum += float(key["Percentage"])
        if (current_sum >= randnum):
            return key["Job Class"]
        row += 1


print(weighted_pick(list_dict))
