from orm import db
from pony.orm import *
import json


@db_session
def findAll():
    return json.dumps({"data": [t.to_dict() for t in db.Team.select()]})


@db_session
def findById(id):
    return db.Team.get(id=id)


@db_session
def updateYear(id, year):
    v = db.Team.get(id=id)
    v.set(year=year)
    return v


@db_session
def createTeam(team):
    t = db.Team(name=team["name"], year=team["year"])
    return t.to_dict()
