#!flask/bin/python
from flask import Flask, jsonify, request
from pymongo import MongoClient
from helper import valid_login, validate_user
from config import db
from timetable import get_timetable


app = Flask(__name__)

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
     if validate_user(user):
	print user
	db.users.insert(user)
        return jsonify({"Signed Up" :1})
     return jsonify({"Signed Up" :0})

@app.route('/home/<username>', methods=['GET'])
def getTimeTable(username):
  tt = get_timetable(username) 
  return tt
if __name__ =="__main__":
  app.run(debug=True)
