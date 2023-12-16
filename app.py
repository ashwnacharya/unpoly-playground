from flask import Flask
from flask import Flask, render_template, request

from ex01 import ex01
from ex02 import ex02

app = Flask(__name__)
app.register_blueprint(ex01, url_prefix='/ex01')
app.register_blueprint(ex02, url_prefix='/ex02')


@app.route('/')
def get_home_page():
    return render_template("index.html")


