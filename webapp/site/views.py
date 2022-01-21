from flask import Blueprint, render_template

blueprint = Blueprint('site', __name__)


@blueprint.route('/')
def index():
    title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
    return render_template('site/index.html', page_title=title)


@blueprint.route('/promotions')
def promotions():
    title = 'Specials and promotions of laser treatment'
    return render_template('site/promotions.html', page_title=title)


@blueprint.route('/contact')
def contact():
    title = 'Contact us to make a booking!'
    return render_template('site/contact.html', page_title=title)


@blueprint.route('/faq')
def faq():
    title = 'Frequently asked questions'
    return render_template('site/faq.html', page_title=title)


@blueprint.route('/prices')
def prices():
    title = 'Specials and promotions of laser treatment'
    return render_template('site/prices.html', page_title=title)


@blueprint.route('/blogs_tips')
def blogs_tips():
    title = 'Read our news and tips to make you look gorgeous!'
    return render_template('site/blogs_tips.html', page_title=title)
