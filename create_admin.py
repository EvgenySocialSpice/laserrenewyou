from getpass import getpass
import sys
from webapp import create_app
from webapp.db import db
from webapp.user.models import User


app = create_app()

with app.app_context():
    username = input('your name: ')
    if User.query.filter(User.username == username).count():
        print('This name is already exist')
        sys.exit(0)
    password = getpass('your password: ')
    password2 = getpass('repeat your password: ')
    if not password == password2:
        print('password is not the same')
        sys.exit(0)
    new_user = User(username=username, role='admin')
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))
