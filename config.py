import os
from os.path import join, dirname
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
ALLOWED_EXTENSIONS = set(['csv', 'txt'])
HOST = "0.0.0.0"
PORT = 2222
SESSION_TYPE = 'filesystem'