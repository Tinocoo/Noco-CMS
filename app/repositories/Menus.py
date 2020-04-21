from app.models import db
from app.models.MenuLists import MenuLists
from app.models.MenuSettings import MenuSettings


class Menus(object):

    @classmethod
    def list_menus(self, name):
        query = db.session.query(
            MenuSettings.description,
            MenuLists.description,
            MenuLists.url
        ).join(
            MenuLists
        ).filter(
            MenuSettings.description == name,
            MenuSettings.status == 1
        ).all()

        result = []
        for row in query:
            result.append({
                'menu': row[0],
                'item': row[1],
                'url': row[2]
            })
        
        status = 200 if len(result) > 0 else 404

        return {'result': result, 'status':status}
