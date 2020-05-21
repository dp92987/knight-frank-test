import json

import psycopg2

with open('secret.json') as file:
    secret = json.load(file)

db_host = secret['db_host']
db_user = secret['db_user']
db_password = secret['db_password']
db_name = secret['db_name']

conn = psycopg2.connect(dbname=db_name, host=db_host, user=db_user, password=db_password)


def get_realties():
    cur = conn.cursor()
    cur.execute('SELECT * FROM realties;')
    query = cur.fetchall()
    return query


def get_realty_by_id(realty_id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM realties WHERE id=%s;', (realty_id, ))
    query = cur.fetchone()
    return query
