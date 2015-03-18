from config import db
from flask import jsonify
from jsonschema import validate, exceptions,ValidationError
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
def get_timetable(user):
   timetable = db.timetable.find_one({"department": user['department'], "batch": user['batch']})
   return timetable
   
