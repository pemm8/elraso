from flask_script import Manager, Server
from app import *

manager = Manager(app)

@manager.command
def create_db():
	db.create_all()
	
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 5000)))
)

if __name__ == "__main__":
	manager.run()	