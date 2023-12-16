import os
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345678'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')   