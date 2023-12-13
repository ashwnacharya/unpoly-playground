from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")

@app.route('/other')
def get_other_page():
    return render_template("other.html")

