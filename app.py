# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# # import WTForms
# from flask_wtf import FlaskForm
# from wtforms import StringField
# import

# create the application object
app = Flask(__name__)

# Create a dictionary where we will house vaccination signups
all_signups = []


# use decorators to link the function to a url
# Bring user to the welcome page
@app.route('/')
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
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        new_signup = {
            "name": request.form["name"],
            "dob": request.form["dob"],
            "gender": request.form["gender"],
            "occupation": request.form["occupation"],
            "address": request.form["address"],
            "dose": request.form["dose"],
            "date": request.form["date"]
        }
        all_signups.append(new_signup)
        # Once form is submitted send the user back to the homepage
        # TODO Change this to another redirect (Like a page that displays "Form has been submitted!")
        return redirect(url_for('portal'))
    return render_template('signup.html')


# Provider portal houses all the vaccination signups
# TODO Vaccine signups should be protected so only the Providers can access
@app.route('/providerportal')
def portal():
    return render_template('providerportal.html', signups=all_signups)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# To run app, in terminal type:
# set FLASK_APP=app.py
# set FLASK_ENV=development
# Flask run

# For Unix/Linux:
# export FLASK_APP=app.py
# export FLASK_ENV=development
# Flask run
