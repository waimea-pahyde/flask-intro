from flask import Flask
from flask import redirect
from random import randint
from flask import render_template
from flask import request

#Create the app
app = Flask(__name__)

# Getting the home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# Getting a random number and passing a value into the template
@app.get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template('pages/random.jinja' , number=randNum)
#----------------------------------------------------------------------------------

#LOading the about page - another static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')
#----------------------------------------------------------------------------------


#Retrieving a value from the user, then displaying it. (getting num from root)
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"you entered: {num}")
    return render_template('pages/number.jinja' , number=num)
#----------------------------------------------------------------------------------


#form page - static page w/ form
@app.get("/form")
def form():
    return render_template('pages/form.jinja')
#----------------------------------------------------------------------------------

# error handler 404 page
@app.errorhandler(404)
def notFound(e):
    return render_template('pages/404.jinja')
#----------------------------------------------------------------------------------

#handle data posted from the form
@app.post("/processForm")
def processForm():
    print(f"Form Data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"])