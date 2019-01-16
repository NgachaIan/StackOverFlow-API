from flask import Flask, jsonify
from flask_restful import fields, marshal, Resource, Api, reqparse


from datetime import datetime
import json
from json import dumps

app = Flask(__name__)
api = Api(app)

questions = []

question_fields = {
    "id": fields.Integer,
    "createdBy": fields.Integer,
    "meetup": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "votes": fields.Integer,
}

class Question(Resource):
    def __init__(self):
        self.datetime = datetime.now()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('createdBy', type=int, location='json')
        self.reqparse.add_argument('meetup', type=int, location='json')
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('body', type=str, location='json')
        self.reqparse.add_argument('votes', type=int, location='json')
        super(Question, self).__init__

    def post(self):
        args = self.reqparse.parse_args()
        question = {
            'createdBy': args['createdBy'],
            'meetup': args['meetup'],
            'title': args['title'],
            'body': args['body'],
            'votes': args['votes'],
            'id': len(questions)
        }

        questions.append(question)
        return {'question': marshal(question, question_fields)}, 201
