from flask.blueprints import Blueprint
from .routes import init_module


page = Blueprint('page', __name__)

init_module(page)
