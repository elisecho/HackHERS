# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
# import WTForms
from flask_wtf import FlaskForm
from wtforms import StringField

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Covid-19 Vaccination Tracker"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'test123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


# Route to vaccination signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
