from .controllers import *


def init_module(module):
    module.add_url_rule('/home', view_func=HomePage.as_view('HomePage'), methods=['GET'])
