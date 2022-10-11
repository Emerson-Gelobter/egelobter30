# Whole Lotta Coding: Prattay, Aden, Emerson
# SoftDev
# Oct 2022

# Prediction: We think it will go on the title of the taskbar
# Outcome: We were wrong, it doesn't seem to appear anywhere
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? This will be printed on the terminal.
    return "No hablo queso!"

app.run()
