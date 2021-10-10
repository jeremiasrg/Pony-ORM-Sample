from pony.orm import *
import os

db_host = 'localhost'
if os.environ.get('DB_HOST') != None:
    db_host = os.environ.get('DB_HOST')
db_user = 'root'
if os.environ.get('DB_USER') != None:
    db_user = os.environ.get('DB_USER')
db_pass = ''
if os.environ.get('DB_PASS') != None:
    db_pass = os.environ.get('DB_PASS')

db = Database()
db.bind(provider='mysql',
        host=db_host,
        user=db_user,
        passwd=db_pass,
        db='soccer_teams')


class Team(db.Entity):
    __table__ = 'team'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    year = Optional(int)


db.generate_mapping(create_tables=True)