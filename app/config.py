import os
class Config(object):

    SQLALCHEMY_DATABASE_URL = "sqlite:///../open-hotel.db" # we use sqlite by default, but any db can be bound here
    SECRET_KEY = os.urandom(32)
    LOCAL_URL = 'http://localhost:8000'