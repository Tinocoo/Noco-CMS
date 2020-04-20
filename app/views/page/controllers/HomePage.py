from flask.templating import render_template
from flask.views import MethodView
from app.models.Slideshow import Slideshow
from app.repositories import BaseResource


class HomePage(MethodView):

    def get(self):
        res_slideshow = BaseResource(Slideshow).getAll({'status': 1})
        if res_slideshow['status'] == 200:
            slideshow = res_slideshow['result']
        
        return render_template('site/home.html', slideshow=slideshow)
