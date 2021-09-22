from flask import Flask, render_template, flash, redirect, url_for
from webapp.forms import LoginForm
from webapp.model import db, User
from flask_login import LoginManager, current_user, login_required, login_user, logout_user


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('index.html', page_title=title)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Login'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('you are successfully login')
                return redirect(url_for('index'))
            flash('wrong password or login name')
            return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('you are successfully logout')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hello Admin!'
        else:
            return 'Sorry, you are not Admin!'

    return app
