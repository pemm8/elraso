import os
from flask import render_template, request
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from app import app, db, admin
from models import Page, Spotlight
from forms import ContactForm

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def home():
    form = ContactForm()
    if request.method == "POST" and form.validate_on_submit():
        # todo: do something with data entered
        # todo: flash success / error message
        return render_template('index.html',form=form)
	return render_template('index.html',form=form)

# admin views
path = os.path.join(os.path.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
admin.add_view(ModelView(Page, db.session))
admin.add_view(ModelView(Spotlight, db.session))