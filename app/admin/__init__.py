from flask_admin import Admin
from app.admin.UserView import UserView
from app.admin.CategoryView import CategoryView
from app.admin.PostView import PostView
from app.admin.PagesView import PagesView
from app.admin.MediaView import MediaView
from app.admin.SlideshowView import SlideshowView
from app.admin.FaqsView import FaqsView
from app.admin.TestimonialsView import TestimonialsView
from app.models import db
from app.models.Users import Users
from app.models.Category import Category
from app.models.Posts import Posts
from app.models.Media import Media
from app.models.Pages import Pages
from app.models.Slideshow import Slideshow
from app.models.Faq import Faq
from app.models.Testimonials import Testimonials


admin = Admin(name='Noco\'s CMS', template_mode='bootstrap3')

admin.add_view(PagesView(model=Pages, session=db.session, name='Padrão', category='Páginas'))
admin.add_view(CategoryView(model=Category, session=db.session, name='Categorias', category='Blog'))
admin.add_view(PostView(model=Posts, session=db.session, name='Postagens', category='Blog'))
admin.add_view(MediaView(model=Media, session=db.session, name='Gestão de arquivos', category='Multimidia'))
admin.add_view(SlideshowView(model=Slideshow, session=db.session, name='Slideshow', category='Multimidia'))
admin.add_view(FaqsView(model=Faq, session=db.session, name='FAQS'))
admin.add_view(TestimonialsView(model=Testimonials, session=db.session, name='Testemunhos'))
admin.add_view(UserView(model=Users, session=db.session, name='Gestão de Usuários', category='Configuração'))
