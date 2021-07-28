from fastapi import FastAPI

from fastapi.middleware.wsgi import WSGIMiddleware

from flask import Flask 

api = FastAPI()

flask_app = Flask(__name__)

api.mount("/web", WSGIMiddleware(flask_app))

from .api import *
from .flask import *
from .config import Config