from flask_admin import Admin
from app.admin.UserView import UserView
from app.models import db
from app.models.Users import Users


admin = Admin(name='Eficácia Tecnologia', template_mode='bootstrap3')

admin.add_view(UserView(model=Users, session=db.session, name='Gestão de Usuários', category='Configuração'))
