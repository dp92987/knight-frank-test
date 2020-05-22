import json

import psycopg2
import psycopg2.extras


with open('secret.json') as file:
    secret = json.load(file)

db_host = secret['db_host']
db_user = secret['db_user']
db_password = secret['db_password']
db_name = secret['db_name']


def get_connection():
    conn = psycopg2.connect(dbname=db_name, host=db_host, user=db_user, password=db_password)
    return conn


def get_realties(area=None, floor=None, metro=None):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = '''
          SELECT DISTINCT r.id, r.name, r.address, r.rooms, r.area, t.name as type
          FROM realties AS r
          LEFT JOIN types AS t ON r.type=t.id
          LEFT JOIN realty_metros AS rm ON r.id=rm.realty_id
          LEFT JOIN metros AS m ON rm.metro_id=m.id
          WHERE (%(area)s IS NULL OR r.area=%(area)s)
            AND (%(floor)s IS NULL OR r.floor=%(floor)s)
            AND (%(metro)s IS NULL OR m.name ILIKE %(metro)s);
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
        conn.close()
    return query


def get_realty(realty_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = '''
          SELECT r.id, r.name, r.address, r.rooms, r.floor, r.area, t.name as type
          FROM realties AS r
          LEFT JOIN types AS t ON r.type=t.id
          LEFT JOIN realty_metros AS rm ON r.id=rm.realty_id
          LEFT JOIN metros AS m ON rm.metro_id=m.id
          WHERE r.id=%(id)s;
          '''
    kwargs = {'id': realty_id}
    try:
        cur.execute(sql, kwargs)
        query = cur.fetchone()
    except:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
    return query


def get_metros(realty_id):
    conn = get_connection()
    cur = conn.cursor()
    sql = '''
          SELECT m.name
          FROM realty_metros AS rm
          LEFT JOIN metros AS m on rm.metro_id=m.id
          WHERE rm.realty_id=%(realty_id)s;
          '''
    kwargs = {'realty_id': realty_id}
    try:
        cur.execute(sql, kwargs)
        query = cur.fetchall()
    except:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
    return query
