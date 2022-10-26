# Timmy, Bobby, and Dini's Adventures: Samantha Hua, Emerson Gelobter and Anjini Katari
# SoftDev
# K12 -- Take and Give
# 2022-10-17
# time spent: 1hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.form ***")
    print(request.form)

    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'index.html' )

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
