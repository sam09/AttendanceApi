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

def valid_login(username):
  user = db.users.find_one({'username' : username})
  if user is not None:
    return jsonify({'logged_in':1})

  return jsonify({'logged_in':0})


