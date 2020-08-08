from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Feedback(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	email = db.Column(db.String(200))
	title = db.Column(db.String(200))
	text = db.Column(db.String(200))
	upvotes = db.Column(db.Integer)
	downvotes = db.Column(db.Integer)
	name = db.Column(db.String(100))
	ministry_assigned = db.Column(db.String(200))
	userSentiment = db.Column(db.String(200))
	rating =  db.Column(db.String(200))
	policy =  db.Column(db.String(200))
	language = db.Column(db.String(200))
	userAge = db.Column(db.Integer)
	userPincode = db.Column(db.Integer)
	def __init__(self,email,title,text,upvotes,downvotes,name,
		ministry_assigned,userSentiment,rating,policy,language,userAge,userPincode):
		self.email = email
		self.title = title
		self.text = text
		self.upvotes = upvotes
		self.downvotes = downvotes
		self.name = name
		self.ministry_assigned = ministry_assigned
		self.userSentiment = userSentiment
		self.rating = rating
		self.policy = policy
		self.language = language
		self.userAge = userAge
		self.userPincode = userPincode


class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	first_name = db.Column(db.String(200))
	last_name = db.Column(db.String(200))
	email = db.Column(db.String(200))
	password = db.Column(db.String(200))
	def __init__(self,first_name,last_name,email,password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password



class UserSchema(ma.SQLAlchemySchema):
	class Meta:
		model = User
		fields = ("id","first_name","last_name","email","password")

user_schema = UserSchema()
users_schema =  UserSchema(many = True)

class FeedbackSchema(ma.SQLAlchemySchema):
	class Meta:
		model = Feedback
		fields = ("id","email","title","text","upvotes","downvotes","name","ministry_assigned","userSentiment","rating","policy","language","userAge","userPincode")

feedback_schema = FeedbackSchema()
feedbacks_schema =  FeedbackSchema(many = True)

db.create_all()

@app.route('/feedback',methods=['POST'])
def add_feedback():

	email = request.json['email']
	title = request.json['title']
	text = request.json['text']
	upvotes = request.json['upvotes']
	downvotes = request.json['downvotes']
	name = request.json['name']
	ministry_assigned = request.json['ministry_assigned']
	userSentiment = request.json['userSentiment']
	rating = request.json['rating']
	policy = request.json['policy']
	language = request.json['language']
	userAge = request.json['userAge']
	userPincode = request.json['userPincode']


	new_feedback = Feedback(email,title,text,upvotes,downvotes,name,ministry_assigned,userSentiment,rating,policy,language,userAge,userPincode)

	db.session.add(new_feedback)
	db.session.commit()

	return feedback_schema.jsonify(new_feedback)


@app.route('/feedback',methods=['GET'])
def get_feedbacks():
	all_feedbacks = Feedback.query.all()
	result = feedbacks_schema.dump(all_feedbacks)
	return jsonify(result)


@app.route('/feedback/<id>',methods=['GET'])
def get_feedback(id):
	feedback = Feedback.query.get(id)
	return feedback_schema.jsonify(feedback)



@app.route('/feedback/<id>',methods=['PUT'])

def update_feedback(id):
	feedback  = Feedback.query.get(id)

	email = request.json['email']
	title = request.json['title']
	text = request.json['text']
	upvotes = request.json['upvotes']
	downvotes = request.json['downvotes']
	name = request.json['name']
	ministry_assigned = request.json['ministry_assigned']
	userSentiment = request.json['userSentiment']
	rating = request.json['rating']
	policy = request.json['policy']
	language = request.json['language']
	userAge = request.json['userAge']
	userPincode = request.json['userPincode']

	feedback.email = email
	feedback.title = title
	feedback.text = text
	feedback.upvotes = upvotes
	feedback.downvotes = downvotes
	feedback.name = name
	feedback.ministry_assigned = ministry_assigned
	feedback.userSentiment = userSentiment
	feedback.rating = rating
	feedback.policy = policy
	feedback.language = language
	feedback.userAge = userAge
	feedback.userPincode = userPincode
	db.session.commit()

	return feedback_schema.jsonify(feedback)


@app.route('/feedback/<id>',methods=['DELETE'])
def delete_feedback(id):
	feedback = Feedback.query.get(id)
	db.session.delete(feedback)
	db.session.commit()
	return feedback_schema.jsonify(feedback)


@app.route('/user',methods=['POST'])
def add_user():

	first_name = request.json['first_name']
	last_name = request.json['last_name']
	email = request.json['email']
	password = request.json['password']

	new_user = User(first_name,last_name,email,password)

	db.session.add(new_user)
	db.session.commit()

	return user_schema.jsonify(new_user)


@app.route('/user',methods=['GET'])
def get_users():
	all_users = User.query.all()
	result = users_schema.dump(all_users)
	return jsonify(result)


@app.route('/user/<id>',methods=['GET'])
def get_user(id):
	user = User.query.get(id)
	return user_schema.jsonify(user)



@app.route('/user/<id>',methods=['PUT'])

def update_user(id):
	user  = User.query.get(id)

	first_name = request.json['first_name']
	last_name = request.json['last_name']
	email = request.json['email']
	password = request.json['password']

	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.password = password
	db.session.commit()
	return user_schema.jsonify(user)


@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()
	return user_schema.jsonify(user)



if __name__ == "__main__":
	app.run(debug=True)

