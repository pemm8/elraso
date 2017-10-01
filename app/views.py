import os
from flask import render_template
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from app import app, db, admin
from models import Page, Spotlight

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html')

# admin views
path = os.path.join(os.path.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
admin.add_view(ModelView(Page, db.session))
admin.add_view(ModelView(Spotlight, db.session))