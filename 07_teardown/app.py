'''
Team CertifiedCoderBoys: Emerson Gelobter, Aden Garbutt
SoftDev
Flask
2022-10-3
time spent:
'''

from flask import Flask



app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0.What is flask
1.To side page, away from route
2.
3.
4.
5. In netlogo?
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
