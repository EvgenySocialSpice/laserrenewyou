from flask import Flask, render_template, url_for
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('index.html', page_title=title)

    return app
