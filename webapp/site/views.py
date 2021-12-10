from flask import Blueprint, render_template

blueprint = Blueprint('site', __name__)


@blueprint.route('/')
def index():
    title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
    return render_template('site/index.html', page_title=title)
