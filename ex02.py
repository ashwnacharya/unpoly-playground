from flask import Blueprint, render_template, request

ex02 = Blueprint('ex02', __name__, url_prefix='/ex02')

items = []

@ex02.route('/', methods=['GET', 'POST'])
def get_home_page():
    if request.method == 'POST':
        item = request.form.get('name', '')
        description = request.form.get('description', '')
        items.append({'name': item, 'description': description})

    return render_template("ex02/home.html", items=items)

