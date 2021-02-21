# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
# import SQLALchemy to hold patient data
# from flask_sqlalchemy import SQLAlchemy

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
            return redirect(url_for('portal'))
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
@app.route('/providerportal')
def portal():
    return render_template('providerportal.html', signups=all_signups)


# # Create Database
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# # Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# # Create Table
# class Patient(db.Model):
#     name = db.Column(db.String(250), primary_key=True)
#     dob = db.Column(db.String(250), nullable=False)
#     gender = db.Column(db.String(250), nullable=False)
#     occupation = db.Column(db.String(250), primary_key=True)
#     address = db.Column(db.String(250), nullable=False)
#     dose = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#
#     # Optional: this will allow each object to be identified by its name when printed.
#     def __repr__(self):
#         return f'<Patient {self.name}>'
#
#
# db.create_all()
#
# # Create record
# new_patient = Patient(name="Elise", dob="08/07/1990", gender="female", occupation="software engineer", address="123 Test St", dose="first", date="02/25/2021")
# db.session.add(new_patient)
# db.session.commit()


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
