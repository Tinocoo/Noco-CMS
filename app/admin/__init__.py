from flask_admin import Admin
from app.admin.UserView import UserView
from app.admin.CategoryView import CategoryView
from app.admin.PostView import PostView
from app.admin.PagesView import PagesView
from app.admin.MediaView import MediaView
from app.admin.MenuItensView import MenuItensView
from app.admin.MenuSettingsView import MenuSettingsView
from app.admin.SlideshowView import SlideshowView
from app.admin.FaqsView import FaqsView
from app.admin.TestimonialsView import TestimonialsView
from app.admin.PricePlansView import PricePlansView
from app.models import db
from app.models.Users import Users
from app.models.Category import Category
from app.models.Posts import Posts
from app.models.Media import Media
from app.models.MenuLists import MenuLists
from app.models.MenuSettings import MenuSettings
from app.models.Pages import Pages
from app.models.Slideshow import Slideshow
from app.models.Faq import Faq
from app.models.Testimonials import Testimonials
from app.models.PricePlan import PricePlan


admin = Admin(name='Noco\'s CMS', template_mode='bootstrap3')

admin.add_view(PostView(model=Posts, session=db.session, name='Blog', category='Postagens'))
admin.add_view(CategoryView(model=Category, session=db.session, name='Categorias', category='Postagens'))
admin.add_view(PagesView(model=Pages, session=db.session, name='Páginas', category='Postagens'))
admin.add_view(MediaView(model=Media, session=db.session, name='Gestão de arquivos', category='Multimidia'))
admin.add_view(SlideshowView(model=Slideshow, session=db.session, name='Slideshow', category='Multimidia'))
admin.add_view(FaqsView(model=Faq, session=db.session, name='FAQS', category='Extras'))
admin.add_view(TestimonialsView(model=Testimonials, session=db.session, name='Testemunhos', category='Extras'))
admin.add_view(PricePlansView(model=PricePlan, session=db.session, name='Preços e Planos', category='Extras'))
admin.add_view(MenuSettingsView(model=MenuSettings, session=db.session, name='Configuração', category='Menu'))
admin.add_view(MenuItensView(model=MenuLists, session=db.session, name='Itens', category='Menu'))
admin.add_view(UserView(model=Users, session=db.session, name='Gestão de Usuários', category='Configuração'))
