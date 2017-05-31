import sql_queries
import os
import string
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def render_home():
    data = sql_queries.question1()
    print(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
