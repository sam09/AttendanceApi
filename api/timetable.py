from config import db
from flask import jsonify
from jsonschema import validate, exceptions,ValidationError
from bson.json_util import dumps

def get_timetable(username):
   user = db.users.find_one({"username" : username})
   batch = user["batch"]
   department = user['department']
   tt = db.timetable.find_one({'batch' : batch, 'department' : department})
   #print tt["timetable"]["0"]
   return dumps(tt)
