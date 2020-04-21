from flask import Markup
from flask.templating import render_template
from flask.views import MethodView
from app.models.Faq import Faq
from app.models.Pages import Pages
from app.models.Slideshow import Slideshow
from app.models.Testimonials import Testimonials
from app.repositories import BaseResource


class HomePage(MethodView):

    def get(self):
        variables = {
            'title': '',
            'body': '',
            'slideshow': [],
            'testimonials': [],
            'faqs': []
        }
        
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


        return render_template('site/home.html', **variables)
