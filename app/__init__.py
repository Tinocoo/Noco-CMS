from flask import Flask
from flask_migrate import Migrate
import importlib
import os
from app.admin import admin
from app.models import db


def create_app():

    app = Flask(__name__)

    environ = {
        'dev': 'app.inc.config.DevelopmentConfig',
        'prod': 'app.inc.config.ProductionConfig'
    }

    conf = environ.get(os.environ.get('FLASK_CONF', default='dev'))
    app.config.from_object(conf)

    db.init_app(app)

    Migrate(app=app, db=db)
    admin.init_app(app)


    mod = importlib.import_module('.'.join(conf.split('.')[:-1]))
    env = getattr(mod, conf.split('.')[-1:][0])

    for module in env.MODULES:
        try:
            package = importlib.import_module('app.views')
            app.register_blueprint(
                getattr(package, module),
                url_prefix='/{}'.format(module)
            )
        except Exception as e:
            print(str(e))

    return app
