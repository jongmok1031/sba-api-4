from com_sba_api.ext.db import db

class ItemDao():

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name==name).all()
    
    @classmethod
    def fing_by_id(cls,id):
        return cls.query.filter_by(id==id).first()