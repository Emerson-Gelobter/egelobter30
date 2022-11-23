'''
Nada Hameed and Emerson Gelobter
SoftDev pd07
K20 - A RESTful Journey Skyward
2022-11-21
time spent: 0.7 hrs
'''

#imports
from flask import Flask, render_template
from urllib import request
import json
app = Flask(__name__)

#key
with open("key_nasa.txt", "r") as file:
    key = file.read()

#img
@app.route("/")
def img():
    #f string, it doesn't work if it's not an f string
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    #opening the image
    openimg = request.urlopen(url)

    #we need a dictionary? how come we need to turn a json object to a python dict object?
    dictionary = json.loads(openimg.read()) #can't do .text bc: the JSON object must be str, bytes or bytearray, not HTTPResponse

    #HOW WE GET THE IMAGE TO DISPLAY:
    return render_template('main.html',a=dictionary['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
