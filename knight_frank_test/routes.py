from .app import app, db


@app.route('/')
@app.route('/catalog.html')
def catalog():
    realties = db.get_realties()
    result = '<html>'
    for realty in realties:
        result = f'{result}<a href=realty/{realty[0]}>{realty}</a><br>'
    result = f'{result}</html>'
    return result


@app.route('/realty/<realty_id>')
def realty(realty_id):
    result = db.get_realty_by_id(realty_id)
    return str(result)
