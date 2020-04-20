from .controllers import *


def init_module(module):
    module.add_url_rule('/', view_func=ManageLogin.as_view('ManageLogin'), methods=['POST', 'GET'])
