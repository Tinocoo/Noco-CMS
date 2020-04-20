from flask_admin import Admin
from app.admin.UserView import UserView
from app.admin.CategoryView import CategoryView
from app.admin.PostView import PostView
from app.admin.MediaView import MediaView
from app.models import db
from app.models.Users import Users
from app.models.Category import Category
from app.models.Posts import Posts
from app.models.Media import Media


admin = Admin(name='Eficácia Tecnologia', template_mode='bootstrap3')

admin.add_view(CategoryView(model=Category, session=db.session, name='Categorias', category='Blog'))
admin.add_view(PostView(model=Posts, session=db.session, name='Postagens', category='Blog'))
admin.add_view(MediaView(model=Media, session=db.session, name='Mídias'))
admin.add_view(UserView(model=Users, session=db.session, name='Gestão de Usuários', category='Configuração'))
