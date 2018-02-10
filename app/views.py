import os
from flask import render_template, request, redirect, session, url_for, abort, flash
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from app import app, db, admin
from models import Page, Spotlight, Message
from forms import ContactForm

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def home():
	form = ContactForm()
	if form.validate_on_submit():
		# todo: do something with data entered
		message = Message(
			name=form.name.data,
			email=form.email.data,
			message=form.message.data)
		db.session.add(message)
		db.session.commit()
		# todo: flash success / error message
		flash("Thanks for your message - we'll be in contact")
		return redirect(url_for('home'))
	return render_template('index.html',form=form)

# admin views
path = os.path.join(os.path.dirname(__file__), 'static')
# admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
# admin.add_view(ModelView(Page, db.session))
# admin.add_view(ModelView(Spotlight, db.session))