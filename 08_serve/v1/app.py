# Whole Lotta Coding: Prattay, Aden, Emerson
# SoftDev
# Oct 2022

# Prediction: Will show a blank webpage, as we have not printed __name__ first
# Outcome: It still prints the return line, even without printing __name__ first. 

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
Footer
