# TBD's Adventures: Samantha Hua, Anjini Katari, and Emerson Gelobter
# SoftDev
# K12 -- Take and Give
# 2022-10-17
# time spent: 1hrs

import os
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html', msg="")


@app.route("/auth", methods =['GET', 'POST'])
def authenticate():
    msg = ""

    session['username'] = "x" #hard coded username and password
    session['password'] = "y"

    if 'username' in request.form: # error otherwise because request.form could be empty
        if session['username'] == request.form['username']: # assumes username exists within session (it does rn because we hard code it)
            if session['password'] == request.form['password']:
                msg = "you're logged in"
                return render_template( 'response.html', user=(request.form['username']), msg=msg, type=request)  # response to a form submission
            else:
                msg = "you're not logged in because your password was wrong"
                return render_template( 'login.html', msg=msg)
        else:
            if session['password'] == request.form['password']:
                msg = "you're not logged in because your username was wrong"
            else:
                msg = "you're not logged in because your username and password were wrong"
            return render_template( 'login.html', msg=msg)

    return render_template( 'login.html', msg="Sorry, an error occured. Try again.") # should not ever get to this point but just in case it does


@app.route('/logout',  methods =['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.pop('username') # these are the fields within session that we want to remove
        session.pop('password')
        return render_template('login.html', msg="You have been successfully logged out")
    return "wrong page buddy" # user is not meant to navigate to this site

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
