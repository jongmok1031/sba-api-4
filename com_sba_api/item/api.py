from flask_restful import Resource, reqparse
from com_sba_api.item.dao import ItemDao
from com_sba_api.item.dto import ItemDto

class Item(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',type = int, required = False, help = 'This field cannot be left blank')
        parser.add_argument('name',type = str, required = False, help = 'This field cannot be left blank')
        parser.add_argument('price',type = float, required = False, help = 'This field cannot be left blank')

    def post(self):
        data = self.parser.parse_args()
        item = ItemDto(data['name'], data['price'])
        try:
            item.save()
        except:
            return {'message':'An error occured inserting the item'}, 500
        return item.json() 201

    def get(self,id):
        item = ItemDao.find_by_id(id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def put(self,id):
        data = Item.parser.parse_args()
        item = ItemDao.find_by_id(id)

        item.name = data['name']
        item.price = data['price']
        item.save()
        return item.json


class Items(Resource):
    def get(self):
        return {'items': list(map(lambda item: item.json(), ItemDao.find_all()))}
        # return {'articles' : [article.json() for article in ArticleDao.find_all()]}