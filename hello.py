from flask import Flask
#from flask_restful import Resource, Api
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

#@app.route('/')
#class HelloWorld(Resource):
#	def get(self):
#		return {"Hello, World!"
	#			'list':[1,2,3]}

TODOs = {
	1:{'task': 'take out the garbage'},
	2:{'task': 'take out the garbage again'},
	3:{'task': 'find out why there is so much garbage'},
}

def abort_if_todo_not_found(todo_id):
	if todo_id not in TODOs:
		abort(404, message="TODO {} does not exist".format(todo_id))

def add_todo(todo_id):
	args = parser.parse_args()
	todo = {'task': args['task']}
	TODOs[todo_id] = todo
	return todo

class Todo(Resource):
	def get(self, todo_id):
		abort_if_todo_not_found(todo_id)
		return TODOs[todo_id]

	def delete(self, todo_id):
		abort_if_todo_not_found(todo_ud)
		#no content, successful
		del TODOs[todo_id]
		return '', 204

	def put(self, todo_id):
		#successfully created
		return add_todo(todo_id), 201

class TodoList(Resource):
	def get(self):
		return TODOs

	def post(self):
		todo_id = max(TODOs.key()) + 1
		return add_photo(todo_id), 201



#api.add_resource(HelloWorld,"/")
api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')

# if we are running like python blah.py this will be true
# but if we had imported this file from another file it would be false
if __name__=="__main__":
	app.run(debug=True)

#URL represents an object
#HTTP command modify the verb

# create -- put/post 
	# 201(success)
	# fail: 409 conflict
# read -- GET 
	# success:200
	# fail: 404 DNE
# update -- PUT 
	# sucess: 200(modify+sendback)/204(modify)/202
	# fail: 404/409
# delete -- DELETE 
	# success: 204 
	# fail: 404
