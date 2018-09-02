from flask import render_template, redirect, session, url_for

from . import main
from .forms import NameForm


@main.route('/', methods=['get', 'post'])
def index():
    name = ''
    name_form = NameForm()

    if name_form.validate_on_submit():
        session['name'] = name_form.name.data
        return redirect(url_for('main.index'))

    return render_template('index.html', name_form=name_form,
                           name=session.get('name'))
