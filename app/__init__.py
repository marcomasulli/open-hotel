import os

from fastapi import FastAPI

from fastapi.middleware.wsgi import WSGIMiddleware

from flask import Flask 

from .config import Config

api = FastAPI()

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = Config.SECRET_KEY

api.mount("/web", WSGIMiddleware(flask_app))

from .api import *
from .flask import *
