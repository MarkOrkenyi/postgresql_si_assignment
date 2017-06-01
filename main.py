import sql_queries
import os
import string
import functions
from flask import Flask, render_template, request, redirect
from flask_navigation import Navigation
app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('Mentors', 'mentors'),
    nav.Item('All Schools', 'all_school'),
    nav.Item('Mentors by country', 'mentors_by_country'),
    nav.Item('Contacts', 'contacts'),
    nav.Item('Applicants', 'applicants'),
    nav.Item('Applicants and mentors', 'applicants_and_mentors')
])


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/mentors")
def mentors():
    data = sql_queries.mentors()
    column_names = ["Name", "School", "Country"]
    return render_template("display_query.html", data=data, column_names=column_names)


@app.route("/all-school")
def all_school():
    data = sql_queries.all_school()
    column_names = ["Name", "School", "Country"]
    return render_template("display_query.html", data=data, column_names=column_names)


@app.route("/mentors-by-country")
def mentors_by_country():
    data = sql_queries.mentors_by_country()
    column_names = ["Country", "Mentors"]
    return render_template("display_query.html", data=data, column_names=column_names)


@app.route("/contacts")
def contacts():
    data = sql_queries.contacts()
    column_names = ["School", "Contact Person"]
    return render_template("display_query.html", data=data, column_names=column_names)


@app.route("/applicants")
def applicants():
    data = sql_queries.applicants()
    column_names = ["Name", "Application number", "Date"]
    return render_template("display_query.html", data=data, column_names=column_names)


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    data = sql_queries.applicants_and_mentors()
    column_names = ["First Name", "Application number", "Mentor"]
    return render_template("display_query.html", data=data, column_names=column_names)


if __name__ == '__main__':
    app.run(debug=True)
