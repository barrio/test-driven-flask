from flask import render_template, redirect, session, url_for, flash

from . import main
from .forms import NameForm


@main.route('/', methods=['get', 'post'])
def index():
    name_form = NameForm()

    if name_form.validate_on_submit():
        name = name_form.name.data
        old_name = session.get('name')

        if old_name and old_name != name:
            flash("You changed your name!")

        session['name'] = name
        return redirect(url_for('main.index'))

    return render_template('index.html', name_form=name_form,
                           name=session.get('name'))
