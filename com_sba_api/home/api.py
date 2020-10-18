from com_sba_api.ext.db import config
from flask_restful import Resource, Resource

class Home(Resource):
    def get(self):
        return {'message':'Server Start'}