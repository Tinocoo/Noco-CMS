from flask import Markup
from flask.templating import render_template
from flask.views import MethodView
from app.models.Faq import Faq
from app.models.Pages import Pages
from app.models.PricePlan import PricePlan
from app.models.Slideshow import Slideshow
from app.models.Testimonials import Testimonials
from app.repositories import BaseResource, Menus


class HomePage(MethodView):

    def get(self):
        variables = {
            'title': '',
            'body': '',
            'slideshow': [],
            'testimonials': [],
            'faqs': [],
            'prices': [],
            'main_menu': []
        }
        
        res_main_menu = Menus.list_menus('Main Menu')
        if res_main_menu['status'] == 200:
            variables.update({ 'main_menu': res_main_menu['result'] })

        res_homepage = BaseResource(Pages).getFirst({'title': 'Homepage', 'status': 1})
        if res_homepage['status'] == 200:
            variables.update({
                'body': Markup(res_homepage['result'][0]['body']),
                'title': res_homepage['result'][0]['title']
            })

        res_slideshow = BaseResource(Slideshow).getAll({'status': 1})
        if res_slideshow['status'] == 200:
            variables.update({ 'slideshow': res_slideshow['result'] })
        
        res_faq = BaseResource(Faq).getAll({'status': 1})
        if res_faq['status'] == 200:
            variables.update({ 'faqs': res_faq['result'] })
        
        res_testimonials = BaseResource(Testimonials).getAll({'status': 1})
        if res_testimonials['status'] == 200:
            variables.update({ 'testimonials': res_testimonials['result'] })

        res_price = BaseResource(PricePlan).getAll({'status': 1})
        if res_price['status'] == 200:
            variables.update({ 'prices': res_price['result'] })

        return render_template('site/home.html', **variables)
