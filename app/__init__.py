from flask import Flask
from random import randint
from flask import render_template

#Create the app
app = Flask(__name__)

@app.get("/")

def home():
    return render_template('pages/home.jinja')

@app.get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template('pages/random.jinja' , number=randNum)

@app.get("/about/")
def about():
    return render_template('pages/about.jinja')