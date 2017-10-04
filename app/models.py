from app import db, app
from datetime import datetime as dt

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ref = db.Column(db.String)
	value = db.Column(db.String)

class Spotlight(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	text = db.Column(db.Text)
	image = db.Column(db.String)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	email = db.Column(db.String)
	message = db.Column(db.Text)
	created = db.Column(db.DateTime, default=dt.utcnow())
