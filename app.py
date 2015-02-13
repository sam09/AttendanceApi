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

@app.route('/signup', methods=['POST'])
def signup():
  if request.method == "POST":
     username = request.form['username']
     batch = request.form['batch']
     dept = request.form['department']
     try:
	batch  = int(batch)
     except:
	return jsonify({'Signed Up':0})
     user = {
	      "username" :username,
	      "batch" :batch,
	      "department" :dept
	     }
     if validateUser(user):
	print user
	db.users.insert(user)
        return jsonify({"Signed Up" :1})
     return jsonify({"Signed Up" :0})


if __name__ =="__main__":
  app.run(debug=True)
