from flask import Markup


class Formatters(object):

    def _list_thumbnail(self, view, context, model, name):
        return Markup(f'<img height="100" width="200" src="{model.url_img}">')
    
    def _date_format_br(self, view, context, model, name):
        return model.created_at.strftime('%d/%m/%Y %H:%M:%S')
    