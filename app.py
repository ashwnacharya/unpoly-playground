from flask import Flask
from flask import Flask, render_template, request

from ex01 import ex01

app = Flask(__name__)
app.register_blueprint(ex01, url_prefix='/ex01')


@app.route('/')
def get_home_page():
    return render_template("index.html")


