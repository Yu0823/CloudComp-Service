from flask import Flask
from config import DB, DB_USER, DB_PSWD, DB_PORT, IP_EC2
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

webapp = Flask(__name__)

class DBconfig(object):
    config_str = f'mysql://{DB_USER}:{DB_PSWD}@{IP_EC2}:{DB_PORT}/{DB}'
    print(config_str)
    webapp.config['SQLALCHEMY_DATABASE_URI'] = config_str

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    webapp.config['SQLALCHEMY_ECHO'] = True
    webapp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

webapp.config.from_object(DBconfig)
db = SQLAlchemy(webapp)

from memcache import database

# create tables
# database.creat_tables()

database.get_config()

# config
# capacity in MB
CAPACITY = 100
# 0 - Random; 1 - LRU
POLICY = 0

# key: (image, timestamp)
global memcache
memcache = {}

from memcache import main

