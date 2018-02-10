import re, os, shutil
from flask_script import Manager, Server

from app import *

manager = Manager(app)

@manager.command
def create_db():
	db.create_all()
	
@manager.commmand
def fix_img_ext(dry):
    dir = os.listdir(os.getcwd() + '/app/static/images/hs/')
    print 'Files to move: %d' % (len(dir))
    for f in dir:
		name = re.split('\.',f)[0]
		ext = 'jpg'
		fn = '%s.%s' % (name, ext)
		print 'Renaming %s to %s' % (f, fn)
		if dry == False:
		    shutil.move(f,fn)
	
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 5000)))
)

if __name__ == "__main__":
	manager.run()	