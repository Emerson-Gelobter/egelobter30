from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
import requests


@app.route("/", methods =['GET', 'POST'])
def show():
    print("hello")
    key = open("key_nasa.txt").read
    print("hell")
    url = "https://api.nasa.gov/planetary/apod?api_key=" + key
    print("hel")
    x = requests.get(url)
    print("he")
    return render_template('main.html', data = x)
