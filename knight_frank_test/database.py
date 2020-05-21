import json

import psycopg2
import psycopg2.extras


with open('secret.json') as file:
    secret = json.load(file)

db_host = secret['db_host']
db_user = secret['db_user']
db_password = secret['db_password']
db_name = secret['db_name']

conn = psycopg2.connect(dbname=db_name, host=db_host, user=db_user, password=db_password)


def get_realties():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = '''
          SELECT DISTINCT r.id, r.name, r.area, r.type
          FROM realties as r
          LEFT JOIN realty_metros as rm on r.id=rm.realty_id
          LEFT JOIN metros as m on rm.metro_id=m.id;
          '''
    try:
        cur.execute(sql)
        query = cur.fetchall()
    except:
        conn.rollback()
        raise
    finally:
        cur.close()
    return query
