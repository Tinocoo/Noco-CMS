from app.models import db


class BaseResource:

    def __init__(self, model):
        self.model = model

    def getAll(self, params={}):
        try:
            query = self.model.query.filter_by(**params).all()
            result = [r.serialize for r in query]
            if len(result) > 0:
                return {'result': result, 'status':200}
            return {'result': result, 'status':404}
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def getFirst(self, params={}):
        try:
            query = self.model.query.filter_by(**params).first()
            return {'result': [query.serialize], 'status':200}
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def postData(self, data):
        try:
            query = self.model(**data)
            db.session.add(query)
            db.session.commit()

            return {'result': query.serialize, 'msg': 'criado com sucesso', 'status': 201}
        except Exception as error:
            return {'result': None, 'msg': str(error), 'status':406}
    
    def putData(self, params, data):
        try:
            self.model.query.filter_by(**params).update({k: v for k, v in data.items() if v is not None})
            db.session.commit()

            return {'result': 'sucess', 'msg': 'atualizado com sucesso', 'status': 200}
        except Exception as error:
            return {'result': None, 'msg': str(error), 'status':406}
    
    def deleteData(self, params):
        try:
            self.model.query.filter_by(**params).delete()
            db.session.commit()

            return {'result': 'sucess', 'msg': 'apagado com sucesso', 'status': 200}
        except Exception as error:
            return {'result': None, 'msg': str(error), 'status':406}
