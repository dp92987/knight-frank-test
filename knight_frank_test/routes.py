from flask import render_template, request, abort
from wtforms import Form, IntegerField, StringField, validators

from .app import app
from . import database as db


class SearchForm(Form):
    area = IntegerField('Площадь', validators=[validators.Optional(), validators.NumberRange(min=1, max=10000)])
    floor = IntegerField('Этаж', validators=[validators.Optional(), validators.NumberRange(min=1, max=1000)])
    metro = StringField('Найти', validators=[validators.Optional(), validators.Length(max=100)],
                        filters=[lambda s: s or None])


@app.route('/')
@app.route('/catalog/')
def catalog():
    search_form = SearchForm(request.args)
    if search_form.validate():
        args = {element.id: element.data for element in search_form}
    else:
        args = {}
    realties = db.get_realties(**args)
    response = render_template('catalog.html', realties=realties, form=search_form)
    return response


@app.route('/item/<realty_id>/')
def item(realty_id):
    realty = db.get_realty(realty_id)
    if realty:
        metros = [metro[0] for metro in db.get_metros(realty_id)]
        return render_template('item.html', realty=realty, metros=metros)
    else:
        return abort(404)
