"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from pyflask_web import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='This is contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'page.html',
        title='About',
        year=datetime.now().year,
        message='This is application description page.'
    )
@app.route('/admin')
def admin():
    """Renders the about page."""
    return render_template(
        'page.html',
        title='Admin',
        year=datetime.now().year,
        message='This is Admin page.'
    )

