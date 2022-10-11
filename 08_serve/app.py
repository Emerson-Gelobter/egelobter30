
'''
Team Whole Lotta Coding: Prattay Dey, Emerson Gelobter, Aden Garbutt
SoftDev
HW08: Serve
2022-10-7
time spent: 1.5 hr
'''
import csv
import random

from flask import Flask

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)
    list_dict = []

    for row in reader:
        # print(row)
        # print(row["Job Class"])
        # compiles all the different key-value pairs into one dictionary
        list_dict.append(row)
        #print(row["Job Class"], row["Percentage"])

    # removes last row, will use later for printing the table of job class and percentagfes
    last_line = list_dict.pop()

app = Flask(__name__)


def weighted_pick():
    randnum = random.uniform(0.0, 99.8)
    for occupation in list_dict:
        randnum -= float(occupation["Percentage"])
        if (randnum <= 0):
            return "Your randomly selected occupation is: " + occupation["Job Class"] + " with a percentage of " + occupation["Percentage"]

@app.route("/")
def output():
    str = "Team Whole Lotta Coding: Prattay Dey, Emerson Gelobter, Aden Garbutt <br> SoftDev Period 07 <br> K08 -- Serve <br> 2022-10-07 <br> time spent: 1.5 hr <br><br>"
    str += weighted_pick() + "<br><br>"

    str += "Job Class : Percentage <br>"
    for occupation in list_dict:
        str += occupation["Job Class"] + " : " + occupation["Percentage"] + "% <br>"

    str += last_line["Job Class"] + " : " + last_line["Percentage"] + "% <br>"
    return str

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
