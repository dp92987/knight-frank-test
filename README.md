# Knight Frank Test
Test case for Knight Frank.

## Description

Simple realty catalog.

## Built With
* Python 3
  * flask
  * wtforms
  * psycopg2
* PostgreSQL

## Installation

Clone, create virtual environment and install dependencies:
```bash
git clone https://github.com/dp92987/knight-frank-test.git
cd knight-frank-test
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Create ```secret.json``` with database credentials:
```json
{
  "db_host": "host",
  "db_user": "user",
  "db_password": "password",
  "db_name": "name"
}
```

Create database schema:
```bash
python3 manage.py create_schema
```

Copy demo data:
```bash
python3 manage.py copy_demo_data
```

Run application:
```bash
python3 run.py
```

## Schema and demo data

Database schema and demo data are stored in ```sql``` folder.

## Demo

https://deltapapa.io/knight-frank-test/
