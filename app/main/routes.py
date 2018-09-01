from flask import render_template

from . import main
from .forms import NameForm


@main.route('/', methods=['get', 'post'])
def index():
    name = ''
    name_form = NameForm()

    if name_form.validate_on_submit():
        name = name_form.name.data

    return render_template('index.html', name_form=name_form, name=name)
