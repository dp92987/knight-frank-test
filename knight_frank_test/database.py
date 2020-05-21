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


def get_realties(area=None, floor=None, metro=None):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = '''
          SELECT DISTINCT r.id, r.name, r.area, r.type
          FROM realties as r
          LEFT JOIN realty_metros as rm on r.id=rm.realty_id
          LEFT JOIN metros as m on rm.metro_id=m.id
          WHERE (%(area)s is null or r.area=%(area)s)
            AND (%(floor)s is null or r.floor=%(floor)s)
            AND (%(metro)s is null or m.name ILIKE LOWER(%(metro)s));
          '''
    kwargs = {'area': area, 'floor': floor, 'metro': f'%{metro}%' if metro else None}
    try:
        cur.execute(sql, kwargs)
        query = cur.fetchall()
    except:
        conn.rollback()
        raise
    finally:
        cur.close()
    return query
