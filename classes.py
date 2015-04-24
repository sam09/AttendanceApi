from config import db
from flask import jsonify
from jsonschema import validate, exceptions,ValidationError
from bson.json_util import dumps

def get_classes(username):
   user = db.users.find_one({"username" : username})
   batch = user["batch"]
   department = user['department']
   tt = db.classes.find_one({'batch' : batch, 'department' : department})
   #print tt["timetable"]["0"]
   return tt

def get_pending_classes(username):
   user = db.users.find_one({"username" :username})
   attendance = user["attendance"]
   pending = []
   spending=[]
   for i in attendance:
      if i['presence'] == "n":
	pending.append(i)
   classes = get_classes(username)
   sub = classes["subjects"]
   for i in sub:
      name = i['name']
      code = i['code']
      occur = i["occurences"]
      for j in occur:
        for k in pending:
	   if j['id'] == k['id']:
             t = {  "name" : name,  "code" : code, "id" : j["id"], "date" : j["date"], "time"  : j["time"] }
             spending.append(t)
   return dumps(spending)
