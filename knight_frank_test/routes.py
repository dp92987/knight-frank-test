from flask import render_template

from .app import app
from . import database as db


@app.route('/')
@app.route('/catalog/')
def catalog():
    realties = db.get_realties()
    response = render_template('catalog.html', realties=realties)
    return response