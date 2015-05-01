from config import db
from flask import jsonify
from jsonschema import validate, exceptions,ValidationError
from bson.json_util import dumps
from classes import get_classes
def get_attendance(username, subject):
    user = db.users.find_one({"username" : username})
    attendance = user['attendance']
    sub = get_classes(username)["subjects"]
    req_sub = {}
    for i in sub:
    	if i['name'] == subject:
    		req_sub = i
    tot = len (req_sub["occurences"])
    present = 0
    absent = 0
    for k in req_sub["occurences"]:
    	for i in attendance:
    		if i["id"] == k["id"]:
    			if i["presence"] == "p":
    				present += 1
    			elif i["absent"] == "a":
    				absent +=1
    attendance_sub = { 
    					"subject": subject , 
    				    "attendance": {
    				    				"total" : tot,
    				    				"present": present,
    				    				"absent": absent,
    				    				"pending": tot - absent - present
    				    			   }
    				  }
    print dumps(attendance_sub)
    return dumps( attendance_sub )