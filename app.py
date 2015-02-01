#!flask/bin/python
from flask import Flask, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/test")

db = client['CrApp']

@app.route('/login', methods=['POST'])
def login():
  if request.method == "POST":
     username = request.form['username']
     return valid_login(username)

def valid_login(username):
  user = db.users.find_one({'username' : username})
  if user is not None:
    return "YES"
  return "NO"

if __name__ =="__main__":
  app.run(debug=True)
