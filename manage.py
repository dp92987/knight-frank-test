import sys
import json

import psycopg2

from knight_frank_test import db


def main():
    if len(sys.argv) > 1:
        conn = db.get_connection()
        cur = conn.cursor()
        try:
            if 'create_schema' in sys.argv:
                cur.execute('DROP TABLE IF EXISTS realty_metros;')
                cur.execute('DROP TABLE IF EXISTS metros;')
                cur.execute('DROP TABLE IF EXISTS realties;')
                cur.execute('DROP TABLE IF EXISTS types;')
                cur.execute(open('sql/schema_types.sql').read())
                cur.execute(open('sql/schema_realties.sql').read())
                cur.execute(open('sql/schema_metros.sql').read())
                cur.execute(open('sql/schema_realty_metros.sql').read())
                conn.commit()
                
            if 'copy_demo_data' in sys.argv:
                for item in json.load(open('sql/data_types.json')):
                    cur.execute(f'INSERT INTO types VALUES {tuple(item.values())};')
                for item in json.load(open('sql/data_realties.json')):
                    cur.execute(f'INSERT INTO realties VALUES {tuple(item.values())};')
                for item in json.load(open('sql/data_metros.json')):
                    cur.execute(f'INSERT INTO metros VALUES {tuple(item.values())};')
                for item in json.load(open('sql/data_realty_metros.json')):
                    cur.execute(f'INSERT INTO realty_metros VALUES {tuple(item.values())};')
                    
            conn.commit()
            
        except psycopg2.Error:
            conn.rollback()
            raise
        
        finally:
            cur.close()
            conn.close()


if __name__ == '__main__':
    main()
