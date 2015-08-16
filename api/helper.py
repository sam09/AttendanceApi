from config import db
from flask import jsonify
import imaplib
from jsonschema import validate, exceptions,ValidationError
IMAP_SERVER = 'webmail.nitt.edu'
def validate_user(user):
   schema = {
	"type" : "object",
	"properties" : {
	    "username" : { "type" : "string" },
	    "batch" : { "type" : "number" },
	    "department" : { "type" : "string" },
	},
    }
   try:
	validate(user,schema)
   except (ValidationError), e :
	print e.message
	return False
   tempUser = db.users.find_one({'username': user["username"]});
   print tempUser
   print user["username"]
   if tempUser is not None:
        return False
   return True

def valid_login(username,password):
 #user = db.users.find_one({'username' : username})
  try:
        imap = imaplib.IMAP4(IMAP_SERVER)
        login = imap.login(username, password)
        success = login[0]
        if(success=='OK'):
        	return jsonify({'logged_in':1})
  except:
  	return jsonify({'logged_in':0})
 # if user is not None:
#    return jsonify({'logged_in':1})

 # return jsonify({'logged_in':0})
