#!flask/bin/python
from flask import Flask, jsonify, request
from api import routes

app = routes.app

if __name__ =="__main__":
  app.run(debug=True)


