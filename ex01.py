from flask import Blueprint, render_template

ex01 = Blueprint('ex01', __name__, url_prefix='/ex01')

@ex01.route('/')
def get_home_page():
    return render_template("ex01/home.html")

@ex01.route('/other')
def get_other_page():
    return render_template("ex01/other.html")
