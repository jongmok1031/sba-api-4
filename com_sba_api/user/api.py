from typing import List
from flask_restful import Resource, reqparse
from com_sba_api.user.dao import UserDao
from com_sba_api.user.dto import UserDto

class User(Resource):
    def __init__(self):
        parser = reqparse.RequestParser() # only allow price changes, no name changes aloowed
        parser.add_argument('userid', type=str, required=True, help = 'This field cannot be left blank')
        parser.add_argument('password', type=str, required = True, help = 'Must enter the store id')
        parser.add_argument('name', type=str, required = True, help = 'Must enter the store id')
        
    def post(self):
        data = self.parser.parser_args()
        user = UserDto(data['userid'],data['password'],data['name'])
        try: 
            user.save()
        except:
            return {'message' : 'An error occured inserting user'}, 500
        return user.json(), 201

    def get(self,id):
        user = UserDao.find_by_name(id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def put(self,id):
        data = User.parser.parse_args()
        user = UserDao.find_by_id(id)
        user.name = data['name']
        user.password = data['password']
        user.userid = data['userid']
        user.save()
        return user.json

class Users(Resource):
    def get(self):
        return {'users': list(map(lambda user:user.json(), UserDao.find_all()))}
        # return {'users': [user.json() for user in UserDao.find_all()]}