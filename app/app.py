import os 
from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin

app = Flask(__name__)

# app temp config
SECRET_KEY='uisgiwiuh25982iwnqmfhbsgiu20j201fiofo2'
app.config.from_object(__name__)

# flask admin
admin = Admin(app, template_mode='bootstrap3')
path = os.path.join(os.path.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)