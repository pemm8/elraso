from app import db, app

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ref = db.Column(db.String)
	value = db.Column(db.String)

class Spotlight(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	text = db.Column(db.Text)
	image = db.Column(db.String)