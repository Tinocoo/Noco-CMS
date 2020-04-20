from flask.blueprints import Blueprint
from .routes import init_module


login = Blueprint('login', __name__)

init_module(login)
