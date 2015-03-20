from config import db
from flask import jsonify
from jsonschema import validate, exceptions,ValidationError
from bson.json_util import dumps

'''
def set_timetable():
   schema = {
     "type": "object",
     "properties": {
       "department": { "type": "string" },
       "batch": {"type": "number" },
       "timetable": { 
         "type": "object",
         "properties": {
           "day": {
             "type": "array",
             "items": "object",
             "properties": {
               "class": {
                  "type": "array",
                  "items": "object",
                  "properties": { "time": { "type": "string"}, "slot": { "type": "string"} }
                }}
             }}
       }}
   }
'''
def get_timetable(username):
   user = db.users.find_one({"username" : username})
   batch = user["batch"]
   department = user['department']
   tt = db.timetable.find_one({'batch' : batch, 'department' : department})
   print tt
   #tt.ObjectId()
   #timetable = JSONEncoder().encode(tt);
   return dumps(tt)
