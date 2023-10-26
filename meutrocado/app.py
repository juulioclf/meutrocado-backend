from flask import Flask

from meutrocado.extentions import configuration
from meutrocado.extentions import database
from meutrocado.extentions import commands

from meutrocado.blueprints import restapi

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
commands.init_app(app)
restapi.init_app(app)
