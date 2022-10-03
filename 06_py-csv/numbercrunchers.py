
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

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Job Class"], row["Percentage"])
