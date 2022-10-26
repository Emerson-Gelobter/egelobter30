'''Timmy, Dini, and Bob's Adventures: Samantha Hua, Anjini Katari, Emerson Gelobter SoftDev K17: Shell Game 2022-10-24 time spent: 1.0hrs'''
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    list_dict = []


    for row in reader:
        # print(row)
        # compiles all the different key-value pairs into one dictionary
        list_dict.append(row)

##print(list_dict)
#==========================================================

c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
for i in list_dict:
    ##print(i)
    ##print(i['age'], i['name'], i['id'])
   
    # trying .format
    c.execute("INSERT INTO students VALUES('{}', '{}', '{}')".format(i['age'], i['name'], i['id']))

    # trying f strings
    # did not work and we were confused about why
    # c.execute(f"INSERT INTO students VALUES('{i['age']}', '{i['name']}', '{i['id']}')")
    

# SECOND FILE -> COURSES
with open("courses.csv", "r") as file2:
    reader = csv.DictReader(file2)
    list_dict2 = []


    for row in reader:
        # print(row)
        # compiles all the different key-value pairs into one dictionary
        list_dict2.append(row)

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

for i in list_dict2:
    c.execute("INSERT INTO courses VALUES('{}', '{}', '{}')".format(i['code'], i['mark'], i['id']))


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
