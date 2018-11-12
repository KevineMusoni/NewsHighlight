from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# initialize bootstrap
bootstrap = Bootstrap()

def create_app(config_name):

    #create the app instance
    app = Flask(__name__)

    #set app configurations
    app.config.from_object(config_options[config_name])

    #initialize bootstrap
    bootstrap.init_app(app)

    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #init requests configurations
    from .requests import configure_request
    configure_request(app)

    return app

