# KnightFrankTest
Test case for Knight Frank.

## Description

Simple realty catalog.

## Built With
* Python 3.8
  * flask
  * wtforms
  * psycopg2
* PostgreSQL

## Installation

Clone, create virtual environment and install dependencies:
```bash
git clone https://github.com/dp92987/KnightFrankTest.git
cd KnightFrankTest
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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

Run application:
```bash
python3 run.py
```

## Schema

Database schema and demo data is stored in ```sql``` folder.

## Demo

http://twentythree.ru:5000