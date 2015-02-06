#!flask/bin/python
from flask import Flask, jsonify, request
from pymongo import MongoClient
from jsonschema import validate, exceptions,ValidationError

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")

db = client['CrApp']

@app.route('/login', methods=['POST'])
def login():
  if request.method == "POST":
     username = request.form['username']
     return valid_login(username)

def valid_login(username):
  user = db.users.find_one({'username' : username})
  if user is not None:
    return jonify({'logged_in' : 1 })

  return jonify({ 'logged_in' : 0})


@app.route('/signup', methods=['POST'])
def signup():
  if request.method == "POST":
     username = request.form['username']
     batch = request.form['batch']
     dept = request.form['department']
     try:
	batch  = int(batch)
     except:
	return jsonify({'Signed Up' : 0 })
     user = {
	      "username" : username,
	      "batch" : batch,
	      "department" : dept
	     }
     if validateUser(user):
	print user
	db.users.insert(user)
        return jsonify({"Signed Up" : 1})
     return jsonify({ "Signed Up" : 0 })

def validateUser(user):
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
   return True

if __name__ =="__main__":
  app.run(debug=True)
