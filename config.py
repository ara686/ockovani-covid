import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://ockovani:ockovani@localhost:5432/ockovani2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
